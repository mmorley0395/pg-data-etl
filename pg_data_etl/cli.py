import click
from pg_data_etl.settings.make_config_file import (
    make_config_file as _make_config_file,
    DB_CONFIG_FILEPATH,
)


@click.group()
def main():
    "'pg' is used command-line access to the pg_data_etl library"
    pass


@click.command()
@click.option("--overwrite/--no-overwrite", default=False)
@click.option(
    "--filepath",
    default=str(DB_CONFIG_FILEPATH),
    help="Custom file path for the config file",
)
def make_config_file(overwrite, filepath):
    """Make a configuration file from the template"""
    _make_config_file(filepath=filepath, overwrite=overwrite)


all_commands = [make_config_file]

for cmd in all_commands:
    main.add_command(cmd)
