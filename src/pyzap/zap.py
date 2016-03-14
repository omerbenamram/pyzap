from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
import warnings
# noinspection PyUnresolvedReferences
import sys
from enum import Enum

import logbook
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from pyzap.categories import suggest_category
import urllib
from types import *
from pies.overrides import *

from pyzap.scraper import _get_max_available_page_in_context, products_from_page, _scrape_categories_suggestions_box

if PY2:
    import urlparse

    setattr(urllib, 'parse', urlparse)

if hasattr(sys, '_called_from_test'):
    # called from within a test run
    logger = logbook.Logger("pyzap", level=logbook.DEBUG)
else:
    logger = logbook.Logger("pyzap", level=logbook.INFO)

logger.handlers.append(logbook.StreamHandler(sys.stdout))

BASE_URL = 'http://www.zap.co.il/models.aspx'
NO_CATEGORY_BASE_URL = 'http://www.zap.co.il/search.aspx'


class ZapGalleryType(Enum):
    ProductRows = 0
    ProductBoxGallery = 1


def search(keyword=None, category=None, max_pages=None, show_progress=True, session=None, **kwargs):
    if not any([keyword, category]):
        raise RuntimeError("Must Input at least one argument!")

    session = session or requests.Session()

    with session as s:
        total_results = {}
        params = {'keyword': keyword}

        if not category:
            category = _infer_category(term=keyword, session=s)

        if category:
            params['sog'] = category

        # set baseurl accordingly..
        urlbase = BASE_URL if category else NO_CATEGORY_BASE_URL

        logger.debug('Search Params: {}'.format(params))

        if show_progress:
            progressbar = tqdm()

        reached_page_limit = False
        current_page = 1

        while not reached_page_limit:
            params['pageinfo'] = current_page
            logger.debug("Sending request: {}".format(urlbase))
            response = s.get(url=urlbase, params=params)
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


def suggest_categories(term, session=None):
    return _infer_category(term, return_many=True, session=session)


def _infer_category(term: str, session=None, return_many=False):
    """
    make a request to try and grab category from zap's engine
    """
    session = session or requests.Session()
    logger.debug("trying to infer category for term {}".format(term))
    params = {'keyword': term}

    head_resp = session.get(url=NO_CATEGORY_BASE_URL, params=params)

    # check if we get redirected and extract category
    if head_resp.history:
        if head_resp.history[0].headers.get('Location'):
            category = urllib.parse.urlparse(head_resp.history[0].headers.get('Location')).query.split('=')[1]
            logger.debug("Successfully extracted category {}".format(category))
            return category

    # perhaps there are multiple categories?
    else:
        categories = _scrape_categories_suggestions_box(soup=BeautifulSoup(head_resp.content, 'lxml'))
        if categories:
            if return_many:
                return categories
            logger.warning('Got several categories! {}'.format(list(categories.keys())))
            return None

    logger.error("Could'nt autodetect category.. search will not be filtered!")
    return None
