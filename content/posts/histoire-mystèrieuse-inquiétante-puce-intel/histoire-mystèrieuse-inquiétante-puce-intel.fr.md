---
title: "L'histoire mystèrieuse d'une inquiétante puce Intel"
description: "Découvrez l'histoire de l'Intel Management Engine, une puce cachée dans les processeurs Intel depuis 2008, capable de fonctionner indépendamment du système d'exploitation."
date: 2025-02-03T15:36:37+01:00
draft: false
images: [/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png]
featuredImage: "/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png"
featuredImagePreview: "/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
author: "Thibaud Robin"
---

# Backdoor ou fonctionnalité : le mystère de l'Intel Management Engine

## Introduction

En 2021, le nombre de PC estimé dans le monde était d'environ **1,4 milliard**. Au quatrième trimestre 2022, **Intel détenait environ 62 % du marché** des processeurs x86 pour ordinateurs, soit environ **850 millions de PC équipés de processeurs Intel**.

![Statistiques](/images/histoire-mystèrieuse-inquiétante-puce-intel/0.png)

Imaginez maintenant la possibilité pour une agence gouvernementale d'accéder à n'importe lequel de ces ordinateurs.

Cela représenterait un nombre de machines égal à la population des **États-Unis, de l'Indonésie, du Brésil et du Canada réunis**. 

Une perspective effrayante, digne des scénarios de films de science-fiction. Pourtant, depuis une dizaine d'années, les chercheurs enchaînent les découvertes de plus en plus troublantes. Et si ce mythe était réellement **vrai** ?

## Une découverte... troublante

![Igor Skochinsky](/images/histoire-mystèrieuse-inquiétante-puce-intel/1.png)

**Igor Skochinsky** est un ingénieur en informatique diplômé de la Belarusian State University en Biélorussie.

Diplômé avec mention, il a débuté sa carrière dans une grande entreprise de logiciels, tout en poursuivant ses recherches en ingénierie inverse durant son temps libre. 

Petit à petit, Igor a gagné en notoriété sur Internet en développant des outils permettant de **contourner les protections anti-piratage des fichiers iTunes** et en explorant les systèmes internes du **Kindle d'Amazon**. Autant dire qu'Igor possède un goût assez prononcé pour l'ingénierie inverse pour le moins exotique.

En **2008**, Igor a rejoint Hex-Rays, la société derrière le célèbre désassembleur `IDA Pro`, où il a collaboré au développement de cet outil essentiel pour les professionnels de la sécurité informatique. Mais Igor avait envie d’aller plus loin et souhaitait diffuser davantage ses recherches.

### La conférence Black Hat USA 2009

{{< youtube AZqKVhPiSoc>}}

En **2009**, lors de la conférence Black Hat USA, **deux chercheurs d’Invisible Things Lab** ont présenté une attaque innovante appelée "`Ring -3 Rootkit`", ciblant l’Intel Management Engine (ME).

L'Intel ME est un microcontrôleur intégré dans les processeurs Intel depuis 2008. Il fonctionne indépendamment du système principal et reste actif même si l'ordinateur est éteint, tant qu'il est branché.

Ce composant est conçu pour aider les entreprises et les administrateurs réseau à **gérer les ordinateurs à distance** : réparer, mettre à jour ou redémarrer une machine sans être devant.

Il surveille également l'état des PC : vérifier si tout va bien ou détecter des problèmes matériels, agissant comme un **assistant technique intégré** au processeur.

### Caractéristiques de l'Intel ME

Les caractéristiques de l'Intel ME sont les suivantes, et pour le moins inquiétantes :

- **Système d'exploitation** : Basé sur ThreadX RTOS de la société Express Logic.
- **Accès total** : Accès à la mémoire, au disque dur, au réseau, etc.
- **Fonctionnement indépendant** : Peut continuer à fonctionner même si l'ordinateur est éteint ou si le système d'exploitation ne marche plus.

![Caractéristiques](/images/histoire-mystèrieuse-inquiétante-puce-intel/2.png)

### Exploitation par les chercheurs

L'exploitation présentée par les chercheurs était relativement simple :

1. **Découvrir les zones mémoire** : Utilisées par Intel ME.
2. **Manipuler et écrire** : Dans cette zone pour injecter du code malveillant.
3. **Installer un rootkit** : Programme malveillant permettant la surveillance, l'enregistrement de touches, et l'exfiltration de données.

Même en tentant de désactiver volontairement cette fonctionnalité dans l’ordinateur, l’exploitation était toujours possible.

Les vulnérabilités ont rapidement été corrigées, mais cette conférence a marqué le début de nombreuses recherches, notamment pour Igor sur ce composant très controversé.

## Analyse approfondie

En **2014**, Igor Skochinsky a présenté une analyse approfondie de l'Intel ME lors de la conférence REcon. Cette présentation a marqué un tournant dans la compréhension de cette technologie.

{{< youtube 4kCICUPc9_8 >}}

### Structure du ME

Sa présentation conclue sur les éléments suivants :

- **Microcontrôleur autonome** : Intégré au chipset Intel.
- **Système d'exploitation** : Basé sur Minix, un clone d'Unix utilisé dans un but pédagogique, inspirant Linus Torvalds pour créer le noyau Linux.
- **Fonctionnement indépendant** : Du processeur principal.

Igor a également constaté que le ME dispose d'un accès complet à la mémoire et peut interagir avec les interfaces réseau sans intervention du processeur principal. Le ME est capable d'accéder aux périphériques et aux données sans laisser de trace visible dans le système d'exploitation.

## L’arrivée d’un nouvel acteur

Les travaux d’Igor n’ont pas échappé à la communauté. De nombreux chercheurs ont saisi l’opportunité de travailler en équipe sur ce sombre composant, notamment pour le désactiver.

Cependant, la tâche est loin d’être aisée, et Intel ne souhaite pas faciliter la tâche.

### Le bit HAP (High Assurance Platform)

![Bit HAP](/images/histoire-mystèrieuse-inquiétante-puce-intel/3.png)

En explorant le firmware ME, Igor a découvert la présence d’un bit HAP, conçu à l’origine pour répondre aux besoins des agences gouvernementales comme la NSA. Ce bit agit comme un "killswitch" permettant de désactiver partiellement ou totalement le ME. Cependant, cette fonctionnalité n’a jamais été documentée pour le grand public et n’est pas disponible pour les utilisateurs ou les entreprises commerciales.

## L’ombre d’une backdoor

Le doute grandit dans la communauté. Pourquoi ce composant est-il toujours présent depuis tant d’années ? Pourquoi Intel fait-il la sourde oreille à ce sujet ?

Igor commence à s’apercevoir que de plus en plus de chercheurs s’intéressent à ce sujet et que des études abondantes ont déjà été publiées avant 2014, voire plusieurs années avant.

### Vulnérabilités découvertes

![Backdoor ?](/images/histoire-mystèrieuse-inquiétante-puce-intel/4.png)

De nombreuses autres vulnérabilités verront le jour, notamment en :

- **2010** : Vassilios Ververis, un étudiant suédois, publie sa thèse sur la sécurité du protocole AMT d’Intel, utilisé par notre puce.
- **2013** : Attaque précurseur présentée par Patrick Stewin et Yuri Bystrov au Chaos Communication Congress (CCC), démontrant les faiblesses de la puce Intel ME.
- **Mai 2017** : Vulnérabilité "Silent Bob is Silent", impactant toute les marques du monde.
- **Août 2023** : Vulnérabilité "Downfall", permettant la lecture de données sensibles.

## Tout supprimer ?

Mais est-ce vraiment impossible de supprimer cette puce parasite de son ordinateur ? La réponse est non ! Mais il va falloir vous accrocher.

### Solutions possibles

Il existe plusieurs solutions plus ou moins complexes pour désactiver ou supprimer Intel ME :

1. **Projet me_cleaner** : Utiliser le projet open-source [me_cleaner](https://github.com/corna/me_cleaner) de Nicola Corna pour modifier le firmware ME en supprimant les partitions non essentielles.
2. **Activation du bit HAP** : Via des outils de programmation du firmware ou certaines configurations BIOS spécifiques.
3. **Firmware alternatif** : Coreboot/Libreboot, des alternatives open-source au BIOS propriétaire, remplaçant le firmware du fabricant par un logiciel léger et désactivant ou éliminant Intel ME.
4. **Suppression physique des modules ME** : Neutraliser physiquement le ME en modifiant ou supprimant des composants matériels spécifiques.

## Conclusion

Il est fort probable que vous vous sentiez observé maintenant. Mais il ne faut pas tomber dans la paranoïa. Igor Skochinsky continue son combat contre la puce avec de nombreuses nouvelles recherches et conférences. 

Ce qu’on peut retenir :

- Pas de preuve que Intel ME soit une backdoor intentionnelle.
- Intel ME n’est pas entièrement désactivable via le BIOS.
- Intel ME peut fonctionner indépendamment du matériel réseau.
- Le ME ne surveille pas activement les activités de l'utilisateur.
- Intel ME n’est pas un outil malveillant créé pour espionner les utilisateurs.
- Le ME n’est pas inutile pour les utilisateurs individuels, assurant des tâches critiques comme la gestion du démarrage, les diagnostics matériels, et les mises à jour du microcode.

Malgré toutes les controverses, cette puce cache encore beaucoup de mystères et n’attend que vous pour découvrir tous ses secrets.

L'histoire complète est disponible au format vidéo sur [la chaine Youtube de Trackflaw](https://www.youtube.com/watch?v=8wC5BfsSQFw) :

{{< youtube 8wC5BfsSQFw >}}

## Sources

- [YouTube - Igor Skochinsky](https://www.youtube.com/watch?v=wsmHmYxyoxg)
- [YouTube - REcon 2014](https://www.youtube.com/watch?v=4kCICUPc9_8&t=1826s)
- [YouTube - CCC 2013](https://www.youtube.com/watch?v=LzWy49LeI3U)
- [YouTube - Silent Bob is Silent](https://www.youtube.com/watch?v=Zda7yMbbW7s)
- [YouTube - Downfall](https://www.youtube.com/watch?v=2_aokrfcoUk)
- [SOS PC - Nombre d'ordinateurs par système d'exploitation dans le monde](https://sospc.name/nombre-ordinateurs-par-systeme-exploitation-monde/)
- [Statista - Parts de marché des processeurs PC](https://fr.statista.com/statistiques/739026/processeurs-pc-fabricants-parts-de-marche-monde/)
- [Black Hat - How To Hack A Turned Off Computer](https://www.blackhat.com/docs/eu-17/materials/eu-17-Goryachy-How-To-Hack-A-Turned-Off-Computer-Or-Running-Unsigned-Code-In-Intel-Management-Engine-wp.pdf)
- [GitHub - me_cleaner](https://github.com/corna/me_cleaner)
- [Libreboot - FAQ](https://libreboot.org/faq.html#intelme)