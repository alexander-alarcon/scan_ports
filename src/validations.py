import os
import re
import socket
from typing import Optional

from typer import BadParameter


def is_valid_ipv4_address(address: str) -> str:
    """
    Validates if the given string is a valid IPv4 address.

    Args:
        address (str): The IP address to be validated.

    Returns:
        str: The validated IP address.

    Raises:
        BadParameter: If the given address is not a valid IPv4 address.
    """
    try:
        socket.inet_pton(socket.AF_INET, address)
    except socket.error:
        raise BadParameter(f"{address} is not a valid IPV4 address")
    return address


def is_valid_port(port: int) -> bool:
    """
    Check if the given port number is valid.

    Args:
        port (int): The port number to be validated.

    Returns:
        bool: True if the port number is valid, False otherwise.
    """
    return 1 <= port <= 65535


def is_valid_range(range: str) -> str:
    """
    Check if the given range is valid.

    Args:
        range (str): The range to be validated.

    Raises:
        BadParameter: If the range format is invalid.

    Returns:
        None
    """
    pattern = r"^(((([1-9]\d*)|[1-9]+)-(([1-9]\d*)|[1-9]+))|(([1-9]\d*)|[1-9]+))(,(((([1-9]\d*)|[1-9]+)-(([1-9]\d*)|[1-9]+))|(([1-9]\d*)|[1-9]+))|(([1-9]\d*)|[1-9]+))*$"
    if not re.match(
        pattern,
        range,
    ):
        raise BadParameter("Invalid range format.")

    range_parts: list[str] = range.split(",")

    for part in range_parts:
        if "-" in part:
            start, end = map(int, part.split("-"))
            if not (is_valid_port(start) and is_valid_port(end)):
                raise BadParameter(f"Invalid port range: {part}")
        else:
            port = int(part)
            if not is_valid_port(port):
                raise BadParameter(f"Invalid port number: {port}")

    return range


def is_valid_threads(user_specified_threads: Optional[int]) -> int:
    """
    Determine the number of threads to use for a task, taking into account the
    user-specified thread count and the available CPU cores.

    Args:
        user_specified_threads (Optional[int]): The number of threads specified
            by the user. If None, the function will use a default value.

    Returns:
        int: The number of threads to use, considering the user's preference and
        the available CPU cores.

    Note:
        The function calculates the maximum number of threads based on the
        available CPU cores and adds 4 to it, with a maximum limit of 32 threads.
        If the user specifies a number of threads, it will be capped at the
        maximum limit if it exceeds it.

    """
    available_cores: Optional[int] = os.cpu_count()

    if available_cores is None:
        print("CPU core count is not available. Using default thread count.")
        num_threads = 4
    else:
        max_threads: int = min(32, available_cores + 4)

        if user_specified_threads is None:
            num_threads: int = max_threads
        else:
            num_threads = min(user_specified_threads, max_threads)

    return num_threads


def is_valid_timeout(timeout: float) -> float:
    """
    Check if the given timeout is valid.

    Args:
        timeout (float): The timeout to be validated.

    Raises:
        BadParameter: If the timeout is not a positive number.

    Returns:
        None
    """
    if timeout <= 0:
        raise BadParameter("Timeout must be a positive number.")
    return timeout
