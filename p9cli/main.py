import click
import sys
import csv
import json
import pandas as pd

from plotnine import *
from plotnine.data import *

@click.group
def cli():
    pass

@cli.command()
@click.argument('command')
@click.option('-f', 
              '--file', 
              help='data file',
              type=click.File('r'),
              default=None)
@click.option("-h",
              "--height",
              help="output height",
              type=float,
              default=None)
@click.option("-w",
              "--width",
              help="output width",
              type=float,
              default=None)

def plot(command, file, height, width):
    if file:
        try:
            df = pd.read_csv(file)
        except Exception as _:
            df = pd.DataFrame(json.loads(file.read()))
    p = eval(f"({command})", locals(), globals())
    p.save(filename=sys.stdout,format="png", height=height, width=width)

if __name__=="__main__":
    cli()
