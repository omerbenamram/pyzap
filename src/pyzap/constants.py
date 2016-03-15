# coding=utf-8
# THIS FILE DOSEN'T IMPORT ANY OTHER FILES. EVERYONE IMPORTS IT!

import re

_parser = 'lxml'
try:
    # noinspection PyUnresolvedReferences
    import lxml
except ImportError:
    try:
        # noinspection PyUnresolvedReferences
        import html5lib

        _parser = 'html5lib'
    except ImportError:
        raise


NUMBER_OF_RE = re.compile('\(([\d,]+)\)', re.UNICODE)
CAT_RE = re.compile("/models\.aspx\?sog=([\w-]+)")
MODEL_ID_RE = re.compile("/model\.aspx\?modelid=(\d+)")
WORDS_RE = re.compile('\w+', re.UNICODE)
BAD_CHARS = ', :<>'
PRICE_RE = re.compile('[\d,]+', re.UNICODE)

MAX_CONCURRENT_FETCH_PAGES = 10
