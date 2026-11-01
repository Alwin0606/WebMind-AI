import ipaddress
import socket
from urllib.parse import urlparse

import requests
import trafilatura
from bs4 import BeautifulSoup


MAX_PAGE_SIZE = 2 * 1024 * 1024

def validate_url(url: str):
    parsed = urlparse(url)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only HTTP and HTTPS URLs are allowed")

    if not parsed.hostname:
        raise ValueError("Invalid URL")

    if parsed.username or parsed.password:
        raise ValueError("URLs containing credentials are not allowed")

    expected_port = 443 if parsed.scheme == "https" else 80

    try:
        port = parsed.port or expected_port
    except ValueError:
        raise ValueError("Invalid URL port")

    if port != expected_port:
        raise ValueError("Only standard HTTP and HTTPS ports are allowed")

    hostname = parsed.hostname.lower()

    if hostname == "localhost" or hostname.endswith((".localhost", ".local")):
        raise ValueError("Local network addresses are not allowed")

    try:
        addresses = {
            item[4][0]
            for item in socket.getaddrinfo(
                hostname,
                port,
                type=socket.SOCK_STREAM
            )
        }
    except socket.gaierror:
        raise ValueError("Unable to resolve website hostname")

    if not addresses:
        raise ValueError("Website hostname has no valid address")

    for address in addresses:
        ip = ipaddress.ip_address(address)

        if not ip.is_global:
            raise ValueError("Private or non-public network addresses are not allowed")


def extract_page(url: str) -> dict:
    validate_url(url)

    headers = {
        "User-Agent": "WebMindAI/1.0 (Educational Research Crawler)",
        "Accept": "text/html,application/xhtml+xml"
    }

    with requests.Session() as session:
        session.trust_env = False

        with session.get(
            url,
            headers=headers,
            timeout=(5, 15),
            allow_redirects=False,
            stream=True
        ) as response:

            if 300 <= response.status_code < 400:
                raise ValueError("Website redirects are not followed for security")

            response.raise_for_status()

            content_type = response.headers.get("Content-Type", "").lower()

            if "text/html" not in content_type and "application/xhtml+xml" not in content_type:
                raise ValueError("The requested URL does not contain an HTML page")

            content_length = response.headers.get("Content-Length")

            if content_length and int(content_length) > MAX_PAGE_SIZE:
                raise ValueError("Web page exceeds the 2 MB size limit")

            chunks = []
            total_size = 0

            for chunk in response.iter_content(chunk_size=65536):
                if not chunk:
                    continue

                total_size += len(chunk)

                if total_size > MAX_PAGE_SIZE:
                    raise ValueError("Web page exceeds the 2 MB size limit")

                chunks.append(chunk)

            html = b"".join(chunks).decode(
                response.encoding or "utf-8",
                errors="replace"
            )

    soup = BeautifulSoup(html, "html.parser")

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "Untitled page"
    )

    extracted_text = trafilatura.extract(
        html,
        url=url,
        include_comments=False,
        include_tables=True
    )

    if not extracted_text:
        extracted_text = soup.get_text(" ", strip=True)

    return {
        "url": url,
        "title": title,
        "content": extracted_text,
        "content_length": len(extracted_text),
        "status": "success"
    }
