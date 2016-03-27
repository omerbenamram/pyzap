# coding=utf-8
import re
from enum import Enum

import logbook
from pies import itertools
from pies.overrides import *

from pyzap.constants import NUMBER_OF_RE, CAT_RE, MODEL_ID_RE
from pyzap.utils import _clean_string, one, re_first_or_none, _handle_price

logger = logbook.Logger(__name__)


def _detect_gallery_type(soup):
    if soup.find(attrs={'class': 'ProductBox CompareModel'}):
        return ZapGalleryType.ProductRows.value
    elif soup.find(attrs={'class': 'GalleryProductBox'}):
        return ZapGalleryType.ProductBoxGallery.value


def _handle_gallery_page(soup):
    results = soup.find_all(attrs={'class': 'GalleryProductBox CompareModel'})
    results_dict = {}

    for box in results:
        product_name_element = box.find(attrs={"class": "ProdName"})
        title, model_id = product_name_element.a.text, MODEL_ID_RE.findall(product_name_element.a.get('href'))
        if model_id:
            model_id = model_id[0]

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

        results_dict[title]['id'] = model_id
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
        product_name_element = info.find(attrs={"class": "ProdInfoTitle"})
        title, model_id = product_name_element.a.text, MODEL_ID_RE.findall(product_name_element.a.get('href'))
        if model_id:
            model_id = model_id[0]

        logger.debug("Got ID {} - {}".format(model_id, title))
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
        results_dict[title]['id'] = model_id
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


def _scrape_categories_suggestions_box(soup):
    filters_box = soup.find_all(attrs={'class': 'Filters'})
    if filters_box:
        filters_box = one(filters_box)
        # get all category links
        items = filters_box.find_all('a', href=CAT_RE)
        # create category / number of items dict
        results = {re_first_or_none(CAT_RE, i.get('href'))
                   : int(re_first_or_none(NUMBER_OF_RE, i.text)) for i in items}
        return results
    else:
        logger.debug('Categories filterbox is unavailable..')
        return {}


class ZapGalleryType(Enum):
    ProductRows = 0
    ProductBoxGallery = 1
