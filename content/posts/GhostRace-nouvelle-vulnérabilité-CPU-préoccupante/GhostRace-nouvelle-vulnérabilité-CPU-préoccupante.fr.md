---
title: "GhostRace : nouvelle vulnérabilité CPU préoccupante"
description: "Une nouvelle classe de vulnérabilités d'exécution spéculative a été découverte courant mars 2024, appelée GhostRace."
date: 2024-03-19T15:39:17+01:00
draft: false
images: [/images/GhostRace-nouvelle-vulnérabilité-CPU-préoccupante/logo.fr.png]
featuredImage: "/images/GhostRace-nouvelle-vulnérabilité-CPU-préoccupante/logo.fr.png"
featuredImagePreview: "/images/GhostRace-nouvelle-vulnérabilité-CPU-préoccupante/logo.fr.png"
tags: ["Spectre-Meltdown", "GhostRace", "CPU"]
---

# 👻 GhostRace : Spectre v2.0 ?

## TL;DR

Une nouvelle classe de vulnérabilités **d'exécution spéculative** a été découverte courant mars 2024, appelée **GhostRace**. Cette attaque est particulièrement dangereuse car elle peut être utilisée pour exploiter un grand nombre de logiciels, y compris les navigateurs web, les systèmes d'exploitation et les applications critiques.

## En théorie

Mais comment fonctionne l'attaque **GhostRace** ? 🤔

L'attaque **GhostRace** ([CVE-2024-2193](https://www.cve.org/CVERecord?id=CVE-2024-2193)) repose sur l'exploitation de failles dans les primitives de synchronisation, qui sont des outils logiciels utilisés pour coordonner l'exécution de plusieurs processus ou threads.

Elle repose dons sur le fait que les processeurs modernes peuvent exécuter de manière spéculative du code **avant de s'assurer qu'il soit réellement nécessaire.**

Cela permet à un attaquant de contourner les protections mises en place par les primitives de synchronisation, comme les mutex, et d'accéder à des données sensibles qui ne devraient pas être accessibles.

## En pratique

### Exemple

🤔 Complexe la théorie. Lisez cet exemple concret :

Imaginez un navigateur web affichant une page web malveillante. Cette page web peut **exécuter du code JavaScript** pouvant créer un thread malveillant. Ce thread malveillant va ensuite inciter le navigateur à **partager une ressource mémoire avec lui**, par exemple un tampon contenant des données sensibles.

Le thread malveillant va ensuite utiliser des **instructions spécifiques** pour influencer l'ordre d'exécution des instructions dans le pipeline du processeur. Cela lui permettra **d'accéder aux données sensibles du tampon** avant que le navigateur ait eu le temps de les protéger.

Dans les grandes lignes et pour résumer :

1. L'attaquant incite la victime à partager une ressource mémoire avec un **thread malveillant**.
2. Le thread malveillant utilise des **instructions spécifiques** pour influencer l'ordre d'exécution des instructions dans le pipeline du processeur.
3. En exploitant les failles des primitives de synchronisation, l'attaquant peut accéder à des données sensibles qui ne devraient pas être accessibles avant la fin de l'exécution du thread victime.

### Exploitation

L'article GhostRace: https://www.vusec.net/projects/ghostrace/ présente un exemple d'attaque contre le noyau Linux.

L'attaque exploite une faille de synchronisation dans le pilote de périphérique `tty`. L'attaquant peut utiliser cette faille pour influencer l'exécution spéculative du noyau et ainsi divulguer le contenu de la mémoire du noyau.

Les chercheurs détaillent un PoC minimaliste illustrant le concept de SRC étape par étape sur leur GitHub : https://github.com/vusec/ghostrace leur permettant de faire fuir la mémoire du noyau à `12 Ko/s`.

## Différences avec Spectre et Meltdown

![spectre meltdown](/images/GhostRace-nouvelle-vulnérabilité-CPU-préoccupante/Meltdown-spectre.jpg)

Mais du coup, cette vulnérabilité semble très proche de **Spectre** et de **Meltdown** non ? 🤔

Petit rappel :

- **Spectre** et **Meltdown** sont deux vulnérabilités de sécurité majeures qui ont été découvertes en 2018. Elles affectent la plupart des processeurs modernes fabriqués par Intel, AMD et ARM.
- Ces deux attaques exploitent des failles dans la conception des processeurs modernes pour **accéder à des données qui devraient être inaccessibles**.

### Spectre

- **Exploite la prédiction de branche du processeur** pour induire l'exécution spéculative de code malveillant.
- Permet à l'attaquant de lire des données sensibles dans la mémoire du processus victime.

### Meltdown

- **Exploite la spéculation de charge du processeur** pour contourner les protections de la mémoire virtuelle.
- Permet à l'attaquant de lire des données sensibles du noyau du système d'exploitation.

### Similarités

L'attaque **GhostRace** est similaire aux attaques **Spectre** et **Meltdown**, mais elle exploite une **faille différente** dans les architectures modernes. Spectre et Meltdown exploitaient des failles dans la **prédiction de branche**, tandis que GhostRace exploite des failles dans **les primitives de synchronisation**.

## Les risques !

Quelles sont les implications de GhostRace ? Faut il paniquer ? 😱

**Non !** Pour plusieurs raisons :

- L'attaque **GhostRace** est encore en cours de recherche et il n'y a pas encore de preuve qu'elle ait été exploitée dans la nature.
- Des **solutions existent pour atténuer l'attaque**, comme la mise à jour des microarchitectures des processeurs et le développement de nouvelles techniques de compilation.
- Des **logiciels de sécurité** peuvent également être utilisés pour détecter et bloquer les attaques GhostRace.

L'attaque GhostRace est une menace sérieuse pour la sécurité informatique. Elle affecte un grand nombre de logiciels et il n'y a pas encore de solution miracle pour se protéger contre cette attaque.

## Les protections

Que faire pour se protéger ? 🛡️

Quelques conseils (un peu bateau oui mais il n'y a pas mieux pour le moment 😅) :

- Installez les dernières mises à jour de sécurité pour votre système d'exploitation et vos logiciels.
- Utilisez un antivirus et un pare-feu performants.
- Soyez prudent lorsque vous visitez des sites web ou ouvrez des pièces jointes suspectes.
- Restez informé des dernières menaces en matière de cybersécurité.

## Sources

- Article scientifique sur GhostRace: https://download.vusec.net/papers/ghostrace_sec24.pdf
- PoC : https://github.com/vusec/ghostrace 