from __future__ import absolute_import, unicode_literals, print_function, division

# -*- coding: utf-8 -*-
import itertools
import re
import sys
import urllib
import warnings

import logbook
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pies.overrides import *

if hasattr(sys, '_called_from_test'):
    # called from within a test run
    logger = logbook.Logger(level=logbook.DEBUG)
else:
    logger = logbook.Logger(level=logbook.INFO)

logger.handlers.append(logbook.StreamHandler(sys.stdout))

PRICE_RE = re.compile('[\d,]+', re.UNICODE)
BASE_URL = 'http://www.zap.co.il/models.aspx'
NO_CATEGORY_BASE_URL = 'http://www.zap.co.il/search.aspx'
WORDS_RE = re.compile('\w+', re.UNICODE)
BAD_CHARS = ', :<>'


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


def products_from_page(soup):
    """
    :param soup:
    :type soup BeautifulSoup
    :return:
    """
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


def get_max_available_page_in_context(soup):
    pages = soup.find_all(attrs={'class': 'NumRow'})
    if pages:
        # basically gets the biggest int out of a bunch of strings
        return int(max(list(filter(lambda x: re.match('\d+', x),
                                   itertools.chain.from_iterable([p.strings for p in pages]))), key=int))
    else:
        return 1


def search(keyword=None, category=None, max_pages=10, show_progress=True, **kwargs):
    if not any([keyword, category]):
        raise RuntimeError("Must Input at least one argument!")

    session = requests.Session() or kwargs.get('session')

    with session as s:
        total_results = {}
        params = {'keyword': keyword}
        if category:
            params['sog'] = category
            urlbase = BASE_URL
        else:
            # this part is a little ugly - it handles a case where we have to infer category from redirection
            urlbase = NO_CATEGORY_BASE_URL
            # check if we get redirected
            head = requests.Request(method='get', url=urlbase, params=params)
            head_resp = s.send(head.prepare())
            if head_resp.history:
                if head_resp.history[0].headers.get('Location'):
                    category = urllib.parse.urlparse(head_resp.history[0].headers.get('Location')).query.split('=')[1]
                    params['sog'] = category
                    urlbase = BASE_URL
                    params.pop('keyword')
            else:
                urlbase = BASE_URL

        base = requests.Request(method='get', url=urlbase, params=params)
        logger.debug('Search Params: {}'.format(base.params))

        if show_progress:
            progressbar = tqdm()

        for page in range(1, max_pages + 1):
            params['pageinfo'] = page
            logger.debug("Sending request: {}".format(base.prepare().url))
            response = s.send(base.prepare())
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "lxml")

            total_results.update(products_from_page(soup))
            max_page = get_max_available_page_in_context(soup)

            if show_progress:
                progressbar.total = max_page
                progressbar.update()

            if max_page <= page:
                logger.debug('Hit max pages at {}, breaking'.format(page))
                break
        else:
            logger.info("Hit page limit at page {} out of {}!".format(max_pages, progressbar.n))

        logger.debug("Got total {} results".format(len(total_results)))

        if not total_results:
            warnings.warn('No results! Did you forget to enter a category..?')

    return total_results
