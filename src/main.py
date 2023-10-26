import typer
from typing_extensions import Annotated


def main(
    host: Annotated[str, typer.Argument(help="The host to scan for ports")],
    ports: Annotated[str, typer.Option(help="The ports to scan")] = "1-1024",
    num_threads: Annotated[int, typer.Option(help="Number of threads to use")] = 1,
) -> None:
    print(f"Scanning {host} for ports {ports} using {num_threads} threads.")


if __name__ == "__main__":
    typer.run(main)
