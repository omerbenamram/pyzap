from __future__ import absolute_import, unicode_literals, print_function, division

# -*- coding: utf-8 -*-
import os

import click
import pyzap
from pyzap.categories import suggest_category
import pandas as pd

CATEGORY_FUZZ_THRESHOLD = 70


@click.command()
@click.option('-k', '-keyword')
@click.option('-c', '--category', help='Category to search')
@click.option('--csv', help='Use CSV instead of excel for output', is_flag=True)
@click.option('-o', '--output', type=click.Path(resolve_path=True, dir_okay=True, file_okay=True,
                                                writable=True), help='Output path',
              required=True, prompt="Where should I save the results?")
@click.option('--max-pages', help='Max pages to scrape', type=click.INT)
def cli_main(keyword, category, output, csv, max_pages):
    # this supports windows shell :)!
    # ? happens when we get surrogate escape :(
    stdin = click.get_text_stream('stdin')
    if not keyword:
        click.echo('Keyword: ', nl=False)
        keyword = stdin.readline()

    if '?' in keyword:
        click.echo('Sorry, received bad input from argv, please enter input keyword here instead:')
        keyword = stdin.readline()

    if category:
        while True:
            categories = suggest_category(category)
            if categories:
                match = categories[0]
                if match[1] > CATEGORY_FUZZ_THRESHOLD:
                    category = match[0]
                    break

            category = click.prompt("Couldn't match any known category.. Closest matches:\n"
                                    "{}\n"
                                    "Re enter category please".format([x[0] for x in categories]))

    if os.path.isdir(output):
        output = os.path.join(output, keyword.strip('\n') + ('.xlsx' if not csv else '.csv'))

    df = pd.DataFrame(pyzap.search(keyword=keyword, category=category, max_pages=max_pages)).transpose()
    if csv:
        df.to_csv(output)
        return

    df.to_excel(output)
    return
