import click
import pprint
import os
import platform
import shutil

from . import log
from .app import WindowsSpecs, LinuxSpecs

log.info('')

@click.group()
def cli():
    pass

@cli.command()
@click.option('-c', '--copy', default=False, show_default=True, help='Copy returned specs to the clipboard')
def collect():
    systype, sysname = os.name, platform.system()
    if os.name == 'nt':
        log.info(f'{systype}/{sysname} system detected')
        if not shutil.which('msinfo32'):
            log.critical('msinfo32 not detected in path')
            raise click.ClickException('msinfo32 not detected in path - override to use linux OS specs detection via --linux')
        model = WindowsSpecs()
        output = """::: {} Specs :::
                'Motherboard' : {motherboard},
                'Processor' : {cpu},
                'Graphics Card' : {gpu},
                'Drives' : {disks}
                """
        output = output.format(
            motherboard=model.mobo,
            cpu=model.cpu,
            gpu=model.gpu,
            disks=model.disks
        )
        print(output)
    else:
        log.critical(f'Unsupported Platform \"{systype}\/{sysname}" detected, failing')
        return