import click
import cpuinfo

from . import log

log.info('')

@click.group()
def cli():
    pass

@cli.command()
@clic.option('-c', '--copy', default=False, show_default=True, help='Copy returned specs to the clipboard')
def run():
    log.info('specs.run')