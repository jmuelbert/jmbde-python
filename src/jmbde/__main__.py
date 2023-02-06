"""Command-line interface."""
import click


@click.command()
@click.help_option()
def main() -> None:
    print("Hello, world!")


main()

