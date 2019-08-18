import click

from pydeplist.pydeplist import APP_CONFIG, main

def get_config(**kwargs):
    for key, val in kwargs.items():
        APP_CONFIG[key] = val


@click.command()
@click.version_option()
@click.option("--mode", "-m",
              default="release", 
              type=click.Choice(["debug", "release"]),
              help="Chose running mode")
@click.option("--dir", "-d",
              default=".",
              help="Folder of the Python package which need to check dependencies.")
@click.option("--user", "-u",
              default="",
              prompt="User account",
              help="User name of GitHub account.")
@click.option("--passwd",
              default="", hide_input=True,
              prompt="Password for GitHub account",
              help="Password for GitHub account.")
def run(**kwargs):
    get_config(**kwargs)
    main()