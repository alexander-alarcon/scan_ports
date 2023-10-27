import concurrent.futures
from typing import Optional

import typer
from rich import print
from rich.progress import track
from typing_extensions import Annotated

import validations as validations
from scanner import scan_port


def parse_range(range_str: str) -> list[int]:
    """
    Parses a string representation of a range of integers and returns a list of integers.

    Args:
        range_str (str): The string representation of the range of integers.

    Returns:
        list[int]: A list of integers representing the range.
    """
    integers: list[int] = []
    for range_part in range_str.split(","):
        if "-" in range_part:
            start, end = map(int, range_part.split("-"))
            integers.extend(range(start, end + 1))
        else:
            integers.append(int(range_part))
    return integers


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
    print(f"Scanning {host} for open ports...")

    port_list: list[int] = parse_range(ports)

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for port in track(port_list, description="Port scanning: "):
            executor.submit(scan_port, host, port)


if __name__ == "__main__":
    typer.run(main)
