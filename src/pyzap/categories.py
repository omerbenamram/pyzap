from __future__ import absolute_import, unicode_literals, print_function, division

# -*- coding: utf-8 -*-
from fuzzywuzzy import process
from pies import itertools


class ZapCategories:
    class Electronics:
        TV = 'e-tv'
        EBookReaders = 'e-digitalbook'
        Ovens = 'e-oven'
        Freezer = 'e-freezer'
        Projectros = 'e-slideprojector'
        Refrigerator = 'e-fridge'
        TVGaming = 'e-tvgame'

    class Computers:
        CardReader = 'c-cardreader'
        Monitors = 'c-monitor'


def _get_attrs_dict(x):
    return {attr: getattr(x, attr) for attr in dir(x) if not callable(attr) and not attr.startswith("__")}


all_attrs = itertools.chain.from_iterable(
    [_get_attrs_dict(cat).values() for cat in _get_attrs_dict(ZapCategories).values()])


def suggest_category(category):
    return process.extract(category, all_attrs, limit=3)
