import click


@click.group()
def cli() -> None:
    """
    Command Line Interface for Movie Catalogue.

    Handles operations such as downloading data and boost up the search interface.
    """
    pass


@cli.command()
def serve() -> None:
    """ runs the falcon app in local host """
    pass


@cli.command()
@click.argument("target_year")
def download_by_year(target_year: str) -> None:
    """ download the data by year """
    pass


@cli.command()
def init() -> None:
    """ initialise the database locally"""
    pass


if __name__ == '__main__':
    cli()

