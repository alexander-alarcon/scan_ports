# Port Scanner

This is a simple Python script for scanning a host for open ports. It allows you to specify a target host (IPv4 address) and a range of ports to scan. The script uses multithreading to speed up the scanning process.

## Usage

To use the port scanner, you'll need to have Python installed on your system. Here are the available options and how to use them:

### Installation

1. Clone this repository to your local machine or download the script.

2. Initialize a Poetry project inside the repository directory:

```shell
poetry init
```

Follow the prompts to create a pyproject.toml file.

3. Install the required dependencies:

```shell
poetry install
```

### Running the scanner

You can run the scanner from the command line with the following syntax:

```shell
poetry run scan-ports [OPTIONS] HOST
```

Options:

  **HOST** (required): The target host (IPv4 address) to scan for open ports.

  **--ports** or **-p** (optional): The ports to scan, specified as a range (e.g., '1-80'), a single port (e.g., '80'), or a list of ports (e.g., '80,1024,3000'). By default, it scans ports 1-1024.

  **--num-threads** or **-t** (optional): Number of threads to use for the scan. A higher value may speed up the scan, but use it cautiously to avoid overloading your system. If not specified or if the specified number of threads is not available, the script will use the default number of threads based on available CPU cores.

  **--timeout** or **-T** (optional): The timeout for each port scan in seconds. If not specified or if the specified timeout is not available, the script will use the default timeout of 1 second.

### Example

```shell
poetry run scan-ports 192.168.0.1 -p 80-100 -t 4
```

This command will scan the host with IP address 192.168.0.1 for open ports in the range 80-100 using 4 threads.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
