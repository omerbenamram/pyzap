from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-

import os

import pytest
import requests
from betamax import Betamax
from bs4 import BeautifulSoup

from pyzap.zap import products_from_page, search, ZapGalleryType, _detect_gallery_type, \
    _scrape_categories_suggestions_box

SAMPLE_ROWS_URL = 'http://www.zap.co.il/models.aspx?sog=c-monitor'
SAMPLE_BOX_URL = 'http://www.zap.co.il/models.aspx?sog=p-shoe'
BROAD_TERM_PAGE = 'http://www.zap.co.il/search.aspx?keyword=cisco'

with Betamax.configure() as config:
    cassette_path = os.path.abspath(os.path.join(__file__, os.pardir, 'fixtures', 'cassettes'))
    config.cassette_library_dir = cassette_path
    if not os.path.exists(cassette_path):
        os.makedirs(cassette_path)


@pytest.fixture
def test_session(request):
    session = requests.Session()
    betamax = Betamax(session, cassette_library_dir=config.cassette_library_dir)
    betamax.use_cassette(request.function.__name__, match_requests_on=['uri', 'body'], record='new_episodes')
    betamax.start()
    request.addfinalizer(betamax.stop)
    return session


@pytest.fixture
def rows_products_page(test_session):
    r = test_session.get(SAMPLE_ROWS_URL)
    return BeautifulSoup(r.content, 'lxml')


@pytest.fixture
def gallery_products_page(test_session):
    r = test_session.get(SAMPLE_BOX_URL)
    return BeautifulSoup(r.content, 'lxml')


@pytest.fixture
def broad_term_page(test_session):
    r = test_session.get(BROAD_TERM_PAGE)
    return BeautifulSoup(r.content, 'lxml')


def test_detect_page_correctly(rows_products_page, gallery_products_page):
    assert _detect_gallery_type(rows_products_page) == ZapGalleryType.ProductRows.value
    assert _detect_gallery_type(gallery_products_page) == ZapGalleryType.ProductBoxGallery.value


def test_rows_page_gets_resutls(rows_products_page):
    page_results = products_from_page(rows_products_page)
    assert len(page_results) > 0


def test_gallery_page_gets_resutls(gallery_products_page):
    page_results = products_from_page(gallery_products_page)
    assert len(page_results) > 0


def test_categories_extracted_correctly(rows_products_page):
    page_results = products_from_page(rows_products_page)
    # when columns are extracted badly - we get out of split results such as dates as columns.

    details = page_results['מסך מחשב Philips 246V5LHAB  ‏24 ‏אינטש']

    assert set(details.keys()) == \
           {'יצרן', 'גודל מסך', 'רזולוציה מקסימלית', 'סוג פאנל', 'זמן תגובה', 'סוג המסך', 'רמקולים', '\u200fPivot',
            'תלת מימד', 'חיבורים',
            'תאריך כניסה לזאפ', 'min_price', 'max_price', 'id'}


def test_gets_result_when_no_category(test_session):
    results = search('מסך מחשב', session=test_session, max_pages=1)
    assert len(results) > 0


def test_extracts_multiple_categories_from_broad_term(broad_term_page):
    categories_suggestions = _scrape_categories_suggestions_box(broad_term_page)
    assert categories_suggestions == {'e-telephone': 9, 'c-router': 32, 'c-controller': 4,
                                      'c-harddrive': 1, 'c-hub': 273, 'c-repeater': 26, 'c-switching': 17,
                                      'e-headphone': 1, 'g-recordingsystem': 2}
