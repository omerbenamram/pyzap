from __future__ import absolute_import, unicode_literals, print_function, division

# -*- coding: utf-8 -*-
import os
import re

import pytest
import requests
from betamax import Betamax
from bs4 import BeautifulSoup

from pyzap.zap import products_from_page, search

SAMPLE_URL = 'http://www.zap.co.il/models.aspx?sog=c-monitor'

with Betamax.configure() as config:
    config.cassette_library_dir = os.path.join(__file__, os.pardir, 'fixtures', 'cassettes')


@pytest.fixture
def test_session(request):
    test_session = requests.Session()
    betamax = Betamax(test_session, cassette_library_dir=config.cassette_library_dir)
    betamax.use_cassette(request.function.__name__, match_requests_on=['uri', 'body'], record='new_episodes')
    betamax.start()
    request.addfinalizer(betamax.stop)
    return test_session


@pytest.fixture
def products_page(test_session):
    r = test_session.get(SAMPLE_URL)
    return BeautifulSoup(r.content, 'lxml')


def test_gets_resutls(products_page):
    page_results = products_from_page(products_page)
    assert len(page_results) > 0


def test_categories_extracted_correctly(products_page):
    page_results = products_from_page(products_page)
    # when columns are extracted badly - we get out of split results such as dates as columns.

    title, details = next(iter(page_results.items()))
    assert set(details.keys()) == \
           {'יצרן', 'גודל מסך', 'רזולוציה מקסימלית', 'סוג פאנל', 'זמן תגובה', 'סוג המסך', 'רמקולים', '\u200fPivot',
            'תלת מימד', 'חיבורים',
            'תאריך כניסה לזאפ', 'min_price', 'max_price'}


def test_gets_result_when_no_category(test_session):
    results = search('מסך מחשב', session=test_session)
    assert len(results) > 0
