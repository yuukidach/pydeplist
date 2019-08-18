import click

from pydeplist.pydeplist import APP_CONFIG, main

def get_config(**kwargs):
    for key, val in kwargs.items():
        APP_CONFIG[key] = val


@click.command()
@click.option("--mode", "-m",
              default="release", 
              type=click.Choice(["debug", "release"]),
              help="Chose running mode")
@click.option("--dir", "-d",
              default=".",
              help="Folder of the Python package which need to check dependencies.")
@click.option("--user", "-u",
              default="",
              help="User name of GitHub account.")
@click.option("--passwd",
              default="",
              help="Password for GitHub account.")
def run(**kwargs):
    get_config(**kwargs)
    main()