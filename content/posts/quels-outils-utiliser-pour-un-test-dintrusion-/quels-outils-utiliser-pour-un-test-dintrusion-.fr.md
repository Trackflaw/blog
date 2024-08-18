---
title: "Quels outils utiliser pour un test d'intrusion (pentest) ?"
description: "Comment bien choisir ses outils pour effectuer un test d'intrusion ? Plus de détails dans l'article ci-dessous"
date: 2024-07-24T11:58:40+01:00
draft: false
images: [/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.png]
featuredImage: "/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.png"
featuredImagePreview: "/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
---

# 🛠️ Les outils dans le domaine des tests d'intrusion/pentest

## Enjeux des tests d'intrusion (pentest)

Le **test d'intrusion**, également connu sous le nom de **pentest**  et **audit de sécurité** (ou vulgairement test de pénétration), est une pratique essentielle pour **évaluer la sécurité d'un système informatique**. Il consiste à simuler des attaques réelles pour **identifier** et **corriger** les **vulnérabilités** avant de véritables attaquants malveillants.

Pour mener à bien un test d'intrusion, il est crucial de disposer des bons **outils**. Cependant, il est difficile de s'y retrouver au vu de la quantité.

Mais pas de panique, dans cet article, nous avons listé pour vous tous les **outils indispensables pour un pentest** efficace afin de répondre au mieux à vos besoins. 🥳

### Rappels

Mais avant toute chose, pourquoi les tests d'intrusion sont-ils importants ? 🤔

Petit récap' rapide :

Les tests d'intrusion et les audits de sécurité informatique permettent de :

- **Identifier** les vulnérabilités avant qu'elles ne soient exploitées.
- **Évaluer** la résilience des systèmes face à des attaques réelles.
- **Améliorer** la posture de sécurité globale de l'organisation.
- **Se conformer** aux réglementations et aux normes de sécurité.
- **Former** les équipes de sécurité aux dernières techniques d'attaque et de défense.

Bref, tout ce qui est nécessaire à une bonne gestion d'une entreprise 😉

{{< admonition tip "Plus d'infos !" >}}
D'ailleurs pour aller plus loin, plusieurs articles sont disponibles pour vous aider à bien choisir votre test d'intrusion.

- Comment bien choisir un prestataire de tests d’intrusion : disponible [ici 👈](/choisir-son-prestataire-de-test-intrusion/)
- Quelle démarche choisir pour effectuer un test d'intrusion : disponible [👉 juste là](/quelle-démarche-test-intrusion/) ! 
{{< /admonition >}}

### Outils ou pas d'outils ?

{{< admonition warning "Attention aux belles promesses !" >}}
Certaines sociétés ont tendance à proposer de véritables tests d'intrusion via des **outils automatisés**. Malheureusement, un outil automatisé ne peut pas, pour le moment, obtenir la même exhaustivité qu'un auditeur confirmé (mais peut-être très prochainement avec la prochaine innovation de Trackflaw 😉).
{{< /admonition >}}

Il est donc important de retenir qu'un test d'intrusion efficace et responsable est un **mélange équilibré de tests manuels couplés à des tests automatiques**.

Plus de détails sur notre méthodo plus bas 👇

## Outils pour les tests d'intrusion

Les **outils** utilisés pour les tests d'intrusion peuvent être classés en plusieurs catégories : la **reconnaissance**, l'**analyse de vulnérabilités**, l'**exploitation**, et la **post-exploitation**. Chacune de ces catégories contient des outils spécialisés **facilitant** le processus de pentest.

Pour faciliter la lecture, le contexte à prendre en compte ici est un **pentest/test d'intrusion externe web**.

{{< admonition info "1001 outils" >}}
Il existe des milliers d'outils. Il est donc impossible ici d'en parler de façon totalement **exhaustive**. Dans cet article, nous vous parlons que des outils **essentiels pour nous** (et pour vous !) et que nous utilisons au quotidien.
{{< /admonition >}}

### 1. Outils de reconnaissance

![Outils de recon](/images/quels-outils-utiliser-pour-un-test-dintrusion/1.png)

La reconnaissance et la cartographie des services est la **première étape** d'un test d'intrusion web.

Elle consiste à **collecter des informations** sur la cible comme les services accessibles, les technologies accessibles, etc. Les outils de reconnaissance aident les pentesteurs à obtenir des données précieuses pouvant servir directement ou indirectement au test d'intrusion.

Quelques exemples d'outils :

- `Nmap` : **nmap** est un scanneur de réseau par excellence, il permet d'identifier les hôtes actifs sur un réseau, les services disponibles et les versions des logiciels en cours d'exécution. Nmap est extrêmement flexible et peut être utilisé pour une reconnaissance complète d’une cible en particulier.
  
- `Subfinder` : **subfinder** est un outil de découverte passive de sous-domaines, optimisé pour la rapidité et la légèreté. Il utilise des sources passives pour identifier les sous-domaines valides d'un site web. [GitHub​](https://github.com/projectdiscovery/subfinder).

- `Gau (GetAllUrls)` : **gau** récupère rapidement toutes les URLs possibles pour un domaine donné à partir de diverses sources telles que Wayback Machine et Common Crawl. Nous l'utilisons pour augmenter notre vision du périmètre. [GitHub](https://github.com/lc/gau).

- `TheHarvester` : **theHarvester** est un outil de collecte d'informations permettant de récupérer des emails, des noms, des sous-domaines, des adresses IP et des bannières à partir de sources publiques telles que les moteurs de recherche et les bases de données PGP. Vraiment excellent ! [GitHub](https://github.com/laramies/theHarvester).

- `Wafw00f` : **wafw00f** détecte et identifie les pare-feu d'applications web (WAF) en envoyant des requêtes HTTP et en analysant les réponses pour déterminer les contre-mesures de sécurité déployées par le site cible. [GitHub](https://github.com/EnableSecurity/wafw00f).

- `CORScanner` : **CORScanner** vérifie les configurations CORS (Cross-Origin Resource Sharing) des sites web pour identifier les politiques mal configurées qui pourraient permettre des attaques de cross-origin. [GitHub](https://github.com/chenjj/CORScanner).

- `Feroxbuster` : **feroxbuster** est un outil de force brute pour les répertoires web, permettant de découvrir rapidement des fichiers et des répertoires cachés sur un serveur en envoyant des requêtes HTTP. Notre petit **préféré** chez Trackflaw 🥰 [GitHub](https://github.com/epi052/feroxbuster).

{{< admonition success "Nos 3 outils de reconnaissance préférés chez Trackflaw" >}}
Si vous ne deviez garder que 3 outils, nous vous conseillons de garder que les 3 outils suivants pour votre phase de reconnaissance :

1. `Nmap` : incontournable pour la découverte de services.
   
2. `Feroxbuster` : un petit bonbon écrit en golang pour découvrir rapidement les répertoires et fichiers cachés.
   
3. `Gau` : petit bijou pour retrouver des routes applicatives oubliées et difficilement trouvables passivement et activement. 
{{< /admonition >}}

### 2. Outils de recherche de vulnérabilités

![Outils de recon](/images/quels-outils-utiliser-pour-un-test-dintrusion/2.png)

Ces outils aident à **identifier les failles de sécurité** dans les systèmes et les applications. Ils automatisent une grande partie du processus de détection des vulnérabilités.

1. `Burp Suite` : **Burp Suite** est un ensemble complet d'outils pour tester la sécurité des applications web. Il permet de réaliser des analyses manuelles et automatisées pour identifier diverses vulnérabilités, telles que les injections SQL, les failles XSS, etc. Il possède un module de scan très puissant dans sa version payante. [Site web](https://portswigger.net/burp).

2. `Nuclei` : **Nuclei** est un scanneur de vulnérabilités rapide et personnalisable basé sur des modèles YAML simples. Il est extensible et facile à utiliser, permettant de détecter, prioriser et corriger les vulnérabilités de sécurité. Un must have ! 🥰 [GitHub](https://github.com/projectdiscovery/nuclei)

3. `ZAP (Zed Attack Proxy)` : **ZAP** est un outil d'attaque et de détection de vulnérabilités pour les applications web. Il offre une variété de fonctionnalités pour automatiser les tests de sécurité, y compris le scanner actif, l'analyse passive et les tests d'intrusion manuels. Souvent critiqué (à tort), le module de scan de ZAP est très performant comparé au scanner de BurpPro. Et tout ça **gratuitement** ! [GitHub](https://github.com/zaproxy/zaproxy).

4. `Nikto` : **Nikto** est un scanner de serveur web un peu obsolète et moins performant que ses concurrents. Mais il peut parfois donner de bonnes surprises [GitHub](https://github.com/sullo/nikto).

5. `{WP|Droope|Joom|Moodl}Scan` : **WPScan**, **Droopescan**, **Joomscan** et **Moodlscan** sont des scanners de sécurité pour leur CMS respectif (vous devinerez facilement chacun des CMS je pense 😉). Puissant et exhaustif, ils sont intéressant à lancer lors d'un audit spécifique. [GitHub de WPScan par exemple](https://github.com/wpscanteam/wpscan).

6. `testssl.sh` : **testssl.sh** est un outil en ligne de commande permettant d'analyser les configurations SSL/TLS. Très pratique ! [GitHub](https://github.com/drwetter/testssl.sh).

{{< admonition failure "Ce que nous ne vous recommandons pas" >}}
Parmi tous ces outils, certains sortent du lot alors que d'autres ne sont vraiment pas intéressant. Voici quelques un à éviter 😟

- `Nessus` : scan de vulnérabilité efficace sur des tests d'intrusion interne, il se montre cependant très peu utile et effice sur de l'externe comparé à son prix prohibitf.
  
- `Qualys` : scan de vulnérabilité spécialisé sur l'externe, il est expert en faux positif et adore surnoter toute les "_vulnérabilités_" décelées (si on peut appeler ça comme ça...) car, non, une configuration TLS supportant la version 1.1 n'est pas une faille critique (mauvais souvenir désolé, rendez l'argent) 😡 

- `OpenVAS` : connu dans l'imaginaire collectif comme étant l'outil gratuit de référence en matière de scan de vulnérabilité, les résultats sont très décevants, peu compréhensibles et très brouillon. Il a du mal à se renouveler mais reste un outil intéressant de par sa gratuité.
{{< /admonition >}}

{{< admonition success "Nos 3 outils de scans préférés chez Trackflaw" >}}
Voici les 3 outils must-have pour localiser efficacement des vulnérabilités :

1. `Nuclei` : surement l'outil le plus révolutionnaire du lot, tant par son exhaustivité que son prix (gratuit !). Il nécessite cependant quelques prérequis techniques pour obtenir de bons résultats.
   
2. `BurpSuite Pro` : BurpSuite est surement l'outil le plus incontournable lors d'un test d'intrusion web. L'exhaustivité de son scanner dans sa version payante le rend très efficace dans la découverte de vulnérabilité et offre un vrai soutien au pentester.
   
3. `Zap` : le module de scan de ZapProxy est bluffant. A titre de comparaison, il trouve une grande majorité des vulnérabilités trouvées par son grand frère payant BurpSuite Pro. Mais à l'avantage d'être totalement gratuit.
{{< /admonition >}}


### 3. Outils d'exploitation

![Outils de recon](/images/quels-outils-utiliser-pour-un-test-dintrusion/3.png)

Une fois les vulnérabilités identifiées, les outils d'exploitation permettent de vérifier si ces failles peuvent être exploitées pour obtenir un accès non autorisé.

{{< admonition warning "Attention à l'utilisation" >}}
Attention lors de l'utilisation de ces outils !

Ils peuvent causer des dégats importants et engendrer des perturbations de service en cas de mauvaise utilisation. Renseignez vous toujours sur les conséquences de l'outil avant de l'exécuter sur votre cible !
{{< /admonition >}}

Quelques exemples avec les outils les plus connus :

1. `Metasploit` : **Metasploit** est un framework de tests d'intrusion modulaire permettant de développer, tester et exécuter des exploits. Il est largement utilisé pour la détection et l'exploitation des vulnérabilités. [GitHub](https://github.com/rapid7/metasploit-framework)

2. `SQLMap` : **SQLMap** est un outil d'injection SQL automatisé permettant de tester et d'exploiter les injections SQL dans les applications web. Il prend en charge diverses bases de données et fournit des fonctionnalités pour l'extraction de données, le contournement des WAFs, et plus encore. [GitHub](https://github.com/sqlmapproject/sqlmap).

3. `SSRFmap` : **SSRFmap** est un outil d'exploitation de Server-Side Request Forgery (SSRF) aidant à trouver et à exploiter les vulnérabilités SSRF en automatisant les attaques et en fournissant des fonctionnalités avancées d'exfiltration de données. [GitHub](https://github.com/swisskyrepo/SSRFmap).

4. `NoSQLMap` : **NoSQLMap** est un outil utilisé pour tester et exploiter les bases de données NoSQL. Il prend en charge plusieurs types de bases de données NoSQL et propose des fonctionnalités pour les injections NoSQL, les détections d'injections, et d'autres attaques spécifiques aux bases de données NoSQL. [GitHub](https://github.com/codingo/NoSQLMap).

5. `SearchSploit` : **SearchSploit** est un utilitaire de ligne de commande permettant de rechercher des exploits dans la base de données Exploit-DB. Il permet aux pentesteurs d'accéder rapidement aux exploits publics sans avoir besoin d'une connexion internet constante. [GitHub](https://github.com/offensive-security/exploitdb).

{{< admonition success "Nos outils d'exploitation préférés chez Trackflaw" >}}
Voici les 3 outils must-have pour localiser efficacement des vulnérabilités :

1. `Metasploit` : véritable boite à outils historique dans le domaine de la sécurité, ce framework permet de réaliser tout type d'actions offensives du scan à la post exploitation le rendant indispensable pour n'importe quel prestation offensive. Un must-have !
   
2. `SearchSploit` : en complément à Métasploit, ce petit outil de recherche vous permettra de consulter très facilement la grande base de données de Exploit-DB sans devoir utiliser un navigateur web. Très pratique !
{{< /admonition >}}

### 4. Outils de post-exploitation

![Outils de recon](/images/quels-outils-utiliser-pour-un-test-dintrusion/4.png)

Enfin pour terminé, les outils de post-exploitation sont utilisés après avoir **obtenu un accès initial** afin de maintenir un accès persistant et explorer davantage le système compromis.

{{< admonition danger "Encore une fois, attention à l'utilisation !!!" >}}
Comme pour les outils précédents, les outils de post-exploitation peuvent causer de **très gros dégâts** s'ils sont mal maîtrisés.

Il est donc **fortement** conseillé d'obtenir l'autorisation du commanditaire avant tout utilisation !
{{< /admonition >}}

Petite liste non exhaustive :

1. `Weevely` : **Weevely** est une web shell conçue pour la post-exploitation. Elle offre plus de 30 modules pour aider aux tâches administratives, maintenir l'accès, fournir une connaissance situationnelle, élever les privilèges et se propager dans le réseau cible. [GitHub](https://github.com/epinna/weevely3)

2. `Cobalt Strike` : **Cobalt Strike** est un outil commercial de post-exploitation utilisé pour évaluer la résilience des systèmes face aux menaces avancées persistantes (APT). Il permet de simuler des attaques réelles, de contrôler les systèmes compromis, et de mener des activités de reconnaissance et d'exploitation. [Site officiel](https://www.cobaltstrike.com/).

3. `Sliver` : **Sliver** est un framework de commande et de contrôle (C2) open-source. Il offre une variété de fonctionnalités pour l'exécution de commandes, la gestion de sessions et la manipulation de payloads. [GitHub](https://github.com/BishopFox/sliver).

4. `Havoc` : **Havoc** est un framework de red teaming et de post-exploitation moderne permettant de simuler des attaques avancées contre des réseaux et des systèmes. Il offre une interface utilisateur intuitive et une intégration facile avec divers outils de sécurité. [GitHub](https://github.com/HavocFramework/Havoc).

5. `Mythic` : **Mythic** est un framework C2 flexible et extensible utilisé pour les tests d'intrusion et les opérations de red teaming. Il permet de gérer plusieurs agents, de créer des payloads personnalisés, et de contrôler des systèmes compromis via une interface web. [GitHub](https://github.com/its-a-feature/Mythic).

{{< admonition success "Nos outils de post-exploitation préférés chez Trackflaw" >}}
Voici nos 3 outils préférés lors de nos étapes de post-exploitation :

1. `Weevely` : permet de faciliter grandement la gestion des webshells sur les applications PHP. Ne fonctionne malheureusement pas sur d'autres langages (l'outil `kraken` peut être une nouvelle alternative).
   
2. `Sliver` : C2 très fonctionnel, gratuit et pratique. A utiliser en complément de Mythic.

3. `Mythic` : Idem que Sliver. A utiliser en complément de Sliver.
{{< /admonition >}}

{{< admonition failure "Cobalt Strike ou pas ?" >}}
Cobalt Strike est surement le système C2 le plus connu et le plus répandu chez les Red Teamers mais aussi chez les attaquants.

Bien qu'il soit un produit **très efficace**, il est **difficile de l'obtenir** légalement et sa licence coute **très cher** (environ 3 500€). Nous ne conseillons pas son utilisation en dehors d'une activité commerciale de Red Team.
{{< /admonition >}}

## Nos conseils

Ouf 🥵 ! Que d'infos !

Mais ne partez pas tout de suite, nous avons encore quelques conseils pour vous 👇

### Optimiser votre test d'intrusion

Quelques conseils (pas si triviaux que ça !) pour bien réaliser et optimiser votre test d'intrusion :

1. **Planification et préparation** : Avant de commencer un test d'intrusion, pensez à bien planifier et définir les objectifs. Cela inclut l'identification des cibles et l'obtention des autorisations nécessaires.

2. **Correler les outils** : Utiliser une combinaison d'outils pour augmenter l’exhaustivité de votre audit peut être une excellente solution. Par exemple, combiner les scripts nse de `Nmap` avec les templates de `Nuclei` tout en utilisant les bons modules d'auxiliary de `Metasploit`.

3. **Mise à jour régulière des outils** : Les outils de pentest doivent être mis à jour régulièrement pour s'assurer qu'ils peuvent détecter et exploiter les dernières vulnérabilités. C'est pour cela que nous vous recommandons d'utiliser `Exegol` (plus de détails plus bas dans l'article).

4. **Rapports détaillés** : Un rapport détaillé des résultats du test d'intrusion est essentiel. Il doit inclure les vulnérabilités identifiées, les preuves de concept, et des recommandations pour corriger les failles de sécurité.

5. **Formation continue** : Les auditeurs doivent continuellement se former et se tenir informés des nouvelles techniques et outils de sécurité. Participer à des conférences, des ateliers, et des formations en ligne peut être bénéfique.

En utilisant les **bons outils** et en suivant les **meilleures pratiques**, les tests d'intrusion peuvent grandement améliorer la sécurité de votre organisation. 🎯

### Aller plus loin

On en parlait plus haut mais il existe une solution bien plus pratique que les traditionnels systèmes d'exploitation de pentest type `KaliLinux` ou `BlackArch` : [Exegol](https://exegol.readthedocs.io/en/latest/).

Petit extrait de la documentation :

> **Exegol** est un environnement de hacking communautaire, puissant et pourtant suffisamment simple pour être utilisé par n'importe qui dans ses activités quotidiennes.
>
> **Exegol** est la meilleure solution pour déployer des environnements de pentesting puissants de manière sûre, facile et professionnelle. Fini les systèmes instables, peu sécurisés et dépourvus d'outils offensifs majeurs. Kali Linux (et les alternatives similaires) sont d'excellentes boîtes à outils pour les apprenants, les étudiants et les pentesters juniors. Mais les professionnels ont des besoins différents, et leur contexte nécessite une toute nouvelle conception.

Et pour en savoir plus, une vidéo dédiée est disponible sur la chaine YouTube de Trackflaw : 👇

{{< youtube RxGkG8HFFHs >}}


## Conclusion

Beaucoup d'infos... Mais uniquement l'essentiel ! 😅

Les tests d'intrusion et les audits de sécurité informatique en général sont des composantes **essentielles** de la stratégie de sécurité de toute organisation.

En utilisant une combinaison d'outils de reconnaissance, d'analyse de vulnérabilités, d'exploitation et de post-exploitation, les pentesteurs peuvent identifier et corriger les failles de sécurité avant qu'elles ne soient exploitées par des attaquants malveillants.

Trackflaw est disponible pour vous aider dans cette démarche. Prenez contact avec nous : https://trackflaw.com/commande/

