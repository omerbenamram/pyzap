from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-

import re
import sys
import warnings
from enum import Enum
import logbook
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pyzap.categories import suggest_category
import urllib

from pies.overrides import *
from pies import itertools

if PY2:
    import urlparse

    setattr(urllib, 'parse', urlparse)

if hasattr(sys, '_called_from_test'):
    # called from within a test run
    logger = logbook.Logger("pyzap", level=logbook.DEBUG)
else:
    logger = logbook.Logger("pyzap", level=logbook.INFO)

logger.handlers.append(logbook.StreamHandler(sys.stdout))

PRICE_RE = re.compile('[\d,]+', re.UNICODE)
BASE_URL = 'http://www.zap.co.il/models.aspx'
NO_CATEGORY_BASE_URL = 'http://www.zap.co.il/search.aspx'
WORDS_RE = re.compile('\w+', re.UNICODE)
BAD_CHARS = ', :<>'


class ZapGalleryType(Enum):
    ProductRows = 0
    ProductBoxGallery = 1


def _handle_price(price_str):
    # handle price vs price range (2500 or '₪2500-3000')
    if not price_str:
        return None
    prices = PRICE_RE.findall(price_str)

    # numbers are formatted as 2,500 sometimes..
    prices = list(map(lambda x: int(x.replace(',', '')), prices))
    return min(prices), max(prices)


def _clean_string(info_string):
    return info_string.strip(BAD_CHARS)


def _detect_gallery_type(soup):
    if soup.find(attrs={'class': 'ProductBox CompareModel'}):
        return ZapGalleryType.ProductRows.value
    elif soup.find(attrs={'class': 'GalleryProductBox CompareModel'}):
        return ZapGalleryType.ProductBoxGallery.value


def _handle_gallery_page(soup):
    results = soup.find_all(attrs={'class': 'GalleryProductBox CompareModel'})
    results_dict = {}

    for box in results:
        title = box.find(attrs={"class": "ProdName"}).a.text
        num_of_stores = int(box.find(attrs={'class': 'num'}).text) or 0
        num_of_reviews = ''.join(box.find(attrs={"class": "ReviewsLink"}).strings).strip('\n')

        # handle reviews
        match = re.findall("(\d+)", num_of_reviews, re.UNICODE)
        if match:
            num_of_reviews = match[0]
        elif re.findall('אחת', num_of_reviews, re.UNICODE):
            num_of_reviews = 1
        else:
            num_of_reviews = 0

        results_dict[title] = {}
        price_info, min_price, max_price = box.parent.find(attrs={'class': 'prices'}), None, None
        if price_info:
            min_price, max_price = _handle_price(price_info.text)

        results_dict[title]['min_price'] = min_price
        results_dict[title]['max_price'] = max_price
        results_dict[title]['num_of_stores'] = num_of_stores
        results_dict[title]['reviews'] = num_of_reviews

    return results_dict


def _handle_rows_page(soup):
    results = soup.find_all(attrs={'class': 'ProdInfo'})
    results_dict = {}

    for info in results:
        # extract some general stuff
        title = info.find(attrs={'class': 'ProdInfoTitle'}).a.text
        price_info, min_price, max_price = info.parent.find(attrs={'class': 'pricesTxt'}), None, None
        if price_info:
            min_price, max_price = _handle_price(price_info.text)

        general_info = info.find(attrs={"class": "ProdGeneralInfo"})
        details = {}
        if general_info:
            for pair in general_info.find_all(attrs={"class": "pair"}):
                category, detail = pair.text.split(':')
                details[_clean_string(category)] = _clean_string(detail)

        results_dict[title] = details
        results_dict[title]['min_price'] = min_price
        results_dict[title]['max_price'] = max_price
    return results_dict


def _get_max_available_page_in_context(soup):
    pages = soup.find_all(attrs={'class': 'NumRow'})
    if pages:
        # basically gets the biggest int out of a bunch of strings
        return int(max(list(filter(lambda x: re.match('\d+', x),
                                   itertools.chain.from_iterable([p.strings for p in pages]))), key=int))
    else:
        return 1


def products_from_page(soup):
    """
    :param soup:
    :type soup BeautifulSoup
    :return:
    """
    page_type = _detect_gallery_type(soup)

    if page_type == ZapGalleryType.ProductBoxGallery.value:
        return _handle_gallery_page(soup)

    else:
        return _handle_rows_page(soup)


def search(keyword=None, category=None, max_pages=None, show_progress=True, session=None, **kwargs):
    if not any([keyword, category]):
        raise RuntimeError("Must Input at least one argument!")

    session = requests.Session() or session

    with session as s:
        total_results = {}
        params = {'keyword': keyword}
        urlbase = BASE_URL

        if category:
            params['sog'] = category

        if not category:
            # this part is a little ugly - it handles a case where we have to infer category from redirection
            # check if we get redirected
            logger.debug("No Category received, trying to infer category from redirection")
            urlbase = NO_CATEGORY_BASE_URL
            head = requests.Request(method='get', url=urlbase, params=params)
            head_resp = s.send(head.prepare())

            if head_resp.history:
                if head_resp.history[0].headers.get('Location'):
                    category = urllib.parse.urlparse(head_resp.history[0].headers.get('Location')).query.split('=')[1]
                    params['sog'] = category
                    params.pop('keyword')
                    logger.debug("Successfully extracted category {}".format(category))
                    urlbase = BASE_URL
            else:
                # even if no category is available we will get misc results
                logger.error("Could'nt autodetect category.. search will not be filtered!")
                urlbase = NO_CATEGORY_BASE_URL

        base = requests.Request(method='get', url=urlbase, params=params)
        logger.debug('Search Params: {}'.format(base.params))

        if show_progress:
            progressbar = tqdm()

        reached_page_limit = False
        current_page = 1

        while not reached_page_limit:
            params['pageinfo'] = current_page
            logger.debug("Sending request: {}".format(base.prepare().url))
            response = s.send(base.prepare())
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "lxml")

            total_results.update(products_from_page(soup))
            max_available_page_from_scope = _get_max_available_page_in_context(soup)
            if (max_available_page_from_scope == current_page) or (max_pages == current_page):
                reached_page_limit = True
                logger.debug('Hit last page at {}, breaking'.format(current_page))

            if show_progress:
                progressbar.total = max_available_page_from_scope
                progressbar.update()

            current_page += 1

        logger.debug("Got total {} results".format(len(total_results)))

        if not total_results:
            if not category:
                warnings.warn('No results! Did you forget to enter a category..?')
            else:
                warnings.warn(
                    'No results! maybe try one of the following categories:')
                print(suggest_category(category), file=sys.stderr)

    logger.info("Total {} results".format(len(total_results)))
    return total_results
