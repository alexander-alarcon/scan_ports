import socket

from rich import print


def scan_port(target_host: str, port: int) -> None:
    """
    Scans a specific port on a target host and prints whether the port is open or not.

    Args:
        target_host (str): The IP address or hostname of the target host.
        port (int): The port number to scan.

    Returns:
        None
    """
    sock = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result: int = sock.connect_ex((target_host, port))

        if result == 0:
            print(f"Port {port} is open.")

    except socket.error as e:
        print(f"Socket error while scanning port {port}: {e}")
    except Exception as e:
        print(f"An error occurred while scanning port {port}: {e}")
    finally:
        if sock is not None:
            sock.close()
