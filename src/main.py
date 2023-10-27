from typing import Optional

import typer
from typing_extensions import Annotated

import validations as validations


def main(
    host: Annotated[
        str,
        typer.Argument(
            help="The host (IPv4 address) to scan for open ports.",
            callback=validations.is_valid_ipv4_address,
        ),
    ],
    ports: Annotated[
        str,
        typer.Option(
            "--ports",
            "-p",
            help="The ports to scan, specified as a range (e.g., '1-80'), a single port (e.g., '80'), or a list of ports (e.g., '80,1024,3000').",
            callback=validations.is_valid_range,
        ),
    ] = "1-1024",
    num_threads: Annotated[
        Optional[int],
        typer.Option(
            "--num-threads",
            "-t",
            help="Number of threads to use for the scan. A higher value may speed up the scan, but use it cautiously to avoid overloading your system. If not specified or number of threads are not available, the default will be calculated based on the available CPU cores.",
            callback=validations.is_valid_threads,
        ),
    ] = None,
) -> None:
    """
    Scan a host for open ports.
    """
    print(f"Scanning {host} for ports {ports} using {num_threads} threads.")


if __name__ == "__main__":
    typer.run(main)
