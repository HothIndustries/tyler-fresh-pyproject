"""Minimal package for tyler-fresh-pyproject."""

import ipaddress
import socket
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import urlopen


def _is_private_or_local_address(ip_address_obj) -> bool:
    return (
        ip_address_obj.is_private
        or ip_address_obj.is_loopback
        or ip_address_obj.is_link_local
        or ip_address_obj.is_multicast
        or ip_address_obj.is_reserved
        or ip_address_obj.is_unspecified
    )


def _is_disallowed_host(hostname: str) -> bool:
    if hostname.lower() == "localhost":
        return True

    try:
        return _is_private_or_local_address(ipaddress.ip_address(hostname))
    except ValueError:
        pass

    try:
        addresses = socket.getaddrinfo(hostname, None)
    except socket.gaierror:
        return False

    for address_info in addresses:
        ip = ipaddress.ip_address(address_info[4][0])
        if _is_private_or_local_address(ip):
            return True

    return False


def make_request(url: str, timeout: float = 10.0) -> str:
    parsed_url = urlparse(url)
    if parsed_url.scheme not in {"http", "https"}:
        raise ValueError("Only http and https URLs are supported.")
    if not parsed_url.hostname:
        raise ValueError("A valid URL with a hostname is required.")
    if _is_disallowed_host(parsed_url.hostname):
        raise ValueError("Requests to local or private network hosts are not allowed.")

    try:
        with urlopen(url, timeout=timeout) as response:
            return response.read().decode("utf-8")
    except (HTTPError, URLError) as exc:
        raise ValueError(f"Request failed: {exc}") from exc


def main(argv: list[str] | None = None) -> None:
    cli_args = sys.argv[1:] if argv is None else argv
    if not cli_args:
        print("Hello from tyler-fresh-pyproject!")
        return

    try:
        print(make_request(cli_args[0]))
    except ValueError as exc:
        print(exc, file=sys.stderr)
