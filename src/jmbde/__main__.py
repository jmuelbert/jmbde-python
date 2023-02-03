"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:

    if __name__ == "__main__":
        main(prog_name="jmbde-python")  # pragma: no cover
        print("Hello, world!")
