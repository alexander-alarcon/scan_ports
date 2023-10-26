from typing import Optional

import typer
from typing_extensions import Annotated


def main(
    name: Annotated[Optional[str], typer.Argument()] = "World",
) -> None:
    typer.echo(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(main)
