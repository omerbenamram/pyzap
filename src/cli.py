from __future__ import absolute_import, unicode_literals, print_function, division
# -*- coding: utf-8 -*-
import click
import logbook
import sys

import pyzap
import pandas as pd
from fuzzywuzzy import process
from pies import itertools

CATEGORY_FUZZ_THRESHOLD = 70

if hasattr(sys, '_called_from_test'):
    # called from within a test run
    logger = logbook.Logger(level=logbook.DEBUG)
else:
    logger = logbook.Logger(level=logbook.INFO)


def _get_attrs_dict(x):
    return {attr: getattr(x, attr) for attr in dir(x) if not callable(attr) and not attr.startswith("__")}


all_attrs = itertools.chain.from_iterable([_get_attrs_dict(cat).values() for cat in _get_attrs_dict(pyzap.ZapCategories).values()])


@click.command()
@click.argument('keyword', nargs=1, type=click.STRING)
@click.option('-c', '--category', help='Category to search')
@click.option('--csv', help='Use CSV instead of excel for output')
@click.option('-o', '--output', type=click.Path(), help='Output path', required=True)
def cli_main(keyword, category, output, csv):

    if category:
        while True:
            categories = process.extract(category, all_attrs, limit=3)
            if categories:
                match = categories[0]
                if match[1] > CATEGORY_FUZZ_THRESHOLD:
                    category = match[0]
                    break

            category = click.prompt("Couldn't match any known category.. Closest matches:\n"
                                    "{}\n"
                                    "Re enter category please".format([x[0] for x in categories]))

    df = pd.DataFrame(pyzap.search(keyword=keyword, category=category)).transpose()
    if csv:
        df.to_csv(output)
        return

    df.to_excel(output)
    return
