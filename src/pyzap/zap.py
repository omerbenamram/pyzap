from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
from ._compat import urllib
import warnings
import requests
import grequests
# noinspection PyUnresolvedReferences
import sys

import logbook

from bs4 import BeautifulSoup
from tqdm import tqdm
from pyzap.categories import suggest_category
from pies.overrides import *

from pyzap.scraper import _get_max_available_page_in_context, products_from_page, _scrape_categories_suggestions_box
from pyzap.constants import _parser

logger = logbook.Logger("pyzap", level=logbook.DEBUG)

logger.handlers.append(logbook.StreamHandler(sys.stdout))

BASE_URL = 'http://www.zap.co.il/models.aspx'
NO_CATEGORY_BASE_URL = 'http://www.zap.co.il/search.aspx'


def search(keyword=None, category=None, max_pages=None, show_progress=False, session=None):
    if not any([keyword, category]):
        raise RuntimeError("Must Input at least one argument!")

    # noinspection PyUnresolvedReferences
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

        # first page
        params['pageinfo'] = current_page
        response = s.get(url=urlbase, params=params)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, _parser)

        total_results.update(products_from_page(soup))
        max_available_page_from_scope = _get_max_available_page_in_context(soup)
        logger.debug('Max Available pages for page {} - {}'.format(current_page, max_available_page_from_scope))

        while not reached_page_limit:
            # create batch
            batch_urls = []
            # move range to be 1-based
            for i in range(current_page + 1, max_available_page_from_scope + 1):
                params.update({'pageinfo': i})
                url = urlbase + '?' + urllib.parse.urlencode(params)
                batch_urls.append(url)

            if max_pages:
                batch_urls = batch_urls[:max_pages]

            responses = grequests.map((grequests.get(u) for u in batch_urls))
            # evil generator - i will cage you in this list!
            responses = list(responses)

            logger.debug('Got {} responses'.format(len(responses)))

            for response in responses:
                soup = BeautifulSoup(response.content, _parser)
                total_results.update(products_from_page(soup))

            current_page += len(responses)
            logger.debug('Current new page - {}'.format(current_page))

            # TODO: optimize this?
            max_available_page_from_scope = _get_max_available_page_in_context(
                BeautifulSoup(responses[-1].content, _parser))
            logger.debug('Current new max available - {}'.format(max_available_page_from_scope))

            if show_progress:
                progressbar.total = max_available_page_from_scope
                progressbar.update()

            if (max_available_page_from_scope <= current_page) or (max_pages and (max_pages <= current_page)):
                reached_page_limit = True
                logger.debug('Hit last page at {}, breaking'.format(current_page))

            logger.info("Total {} results".format(len(total_results)))

        if not total_results:
            if not category:
                warnings.warn('No results! Did you forget to enter a category..?')
            else:
                warnings.warn(
                    'No results! maybe try one of the following categories:')
                print(suggest_category(category), file=sys.stderr)

    return total_results


def suggest_categories(term, session=None):
    return _infer_category(term, return_many=True, session=session)


def _infer_category(term, session=None, return_many=False):
    """
    make a request to try and grab category from zap's engine
    """
    session = session or requests.Session()
    logger.debug("trying to infer category for term {}".format(term))
    params = {'keyword': term}

    first_page = session.get(url=NO_CATEGORY_BASE_URL, params=params)

    # check if we get redirected and extract category
    if first_page.history:
        if first_page.history[0].headers.get('Location'):
            # eww..
            category = urllib.parse.urlparse(first_page.history[0].headers.get('Location')).query.split('=')[1]
            logger.debug("Successfully extracted category {}".format(category))
            return category

    # perhaps there are multiple categories?
    else:
        categories = _scrape_categories_suggestions_box(soup=BeautifulSoup(first_page.content, _parser))
        if categories:
            if return_many:
                return categories
            logger.warning('Got several categories! {}'.format(list(categories.keys())))
            return None

    logger.error("Could'nt autodetect category.. search will not be filtered!")
    return None
