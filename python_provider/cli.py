
"""CLI for python_provider."""

import click

from python_provider.main import main


@click.command()
def cli():
    """CLI entrypoint for the python_provider module."""
    main()
