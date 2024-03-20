---
title: "Pourquoi faire un test d'intrusion sur son site Wordpress en 2024 ?"
description: "WordPress, en tant que l’un des systèmes de gestion de contenu (CMS) les plus utilisés au monde, alimente une part significative des sites web, allant des blogs personnels aux sites d’entreprise."
date: 2024-03-20T10:54:14+01:00
draft: false
images: [/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png]
featuredImage: "/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png"
featuredImagePreview: "/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
---

# Pourquoi un test d'intrusion est OBLIGATOIRE sur votre site Wordpress en 2024 ?

## Introduction

**WordPress**, en tant que l'un des systèmes de gestion de contenu (CMS) **les plus utilisés au monde**, alimente une part significative des sites web, allant des blogs personnels aux sites d'entreprise.

Sa popularité s'accompagne toutefois de risques de sécurité accrus, rendant les tests d'intrusion cruciaux pour protéger ces sites contre les cyberattaques.

📈 Quelques statistiques faramineuses (selon lesmakers.fr) :

- Le CMS **n°1** au monde.
- Plus de **62% part de marché** des CMS.
- Plus de **43% des sites mondiaux** utilisent Wordpress.
- **9 000 thèmes** gratuits.
- **60 000 plugins** gratuits actifs.

<br>

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/1.png" title="Plus de 62% des sites avec un CMS utilisent Wordpress" >}}

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/2.png" title="Plus de 455 millions de sites web dans le monde utilisent WordPress." >}}


## Une popularité à double tranchant

**WordPress** est souvent ciblé par les attaquants en raison de sa large adoption.

Les vulnérabilités, qu'elles soient dans le noyau de WordPress, les thèmes ou les plugins, peuvent être exploitées pour compromettre un site. Les tests d'intrusion permettent d'identifier ces faiblesses avant qu'elles ne soient exploitées par des acteurs malveillants.

Encore quelques statistiques alarmantes 😅

- En 2023, il y a eu plus de **90 millions d'attaques** contre des sites WordPress. (source : https://www.wordfence.com/)
- Plus de **50% des sites WordPress** sont attaqués chaque année. (source : https://sucuri.net/)
- Plus de **90% des attaques** contre les sites WordPress ciblent des vulnérabilités dans les plugins, les thèmes ou le noyau de WordPress lui-même. (https://www.wordfence.com/)

<br>

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/3.png" title="Proportion de l'état des vulnérabilités du CMS Wordpress (source : wpscan.com)." >}}

{{< admonition type=warning title="Attention" open=true >}}
Ces chiffres sont à prendre avec précaution. En effet, il est très difficile de connaitre les proportions exactes des vulnérabilités exploitées.
{{< /admonition >}}


## Pourquoi se protéger ?

Question évidente penserez-vous ? 😉

Pour plusieurs raisons :

- **Protéger ses données sensibles** : les sites WordPress hébergent très souvent des données sensibles, telles que les informations personnelles des utilisateurs et les détails de paiement. 
- **Se conformer aux normes de sécurité** : pour les entreprises, la conformité aux normes de sécurité comme GDPR ou PCI DSS n'est pas une option mais une obligation.
- **Améliorer sa réputation et sa confiance** : Un site sécurisé renforce la confiance des utilisateurs et des clients. En revanche, un site compromis peut nuire gravement à la réputation d'une entreprise. 
- **Prévenir les pertes financières** : les cyberattaques peuvent entraîner des pertes financières considérables, dues au vol de données, à la rançon pour récupérer des données chiffrées, ou aux coûts de rétablissement des services.
- **Assurer sa continuité** : une cyberattaque réussie peut perturber les opérations d'un site WordPress, entraînant des temps d'arrêt et affectant la continuité des activités.

## Le test d'intrusion : une protection par l'attaque

![Faire un test d'intrusion](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/4.png)

Un test d'intrusion, également appelé pentest, est un moyen efficace de simuler une attaque et d'identifier les failles de sécurité de votre site **WordPress**.

### Réponse aux enjeux

Reprenons les enjeux précédents et appliquons les au domaine des tests d'intrusion :

- **Protéger ses données sensibles** : un test d'intrusion aide à évaluer la robustesse des mécanismes de protection de ses données, garantissant leur intégrité et leur confidentialité.
- **Se conformer aux normes de sécurité** : un test d'intrusion révèle si un site WordPress répond aux exigences, évitant ainsi les sanctions potentielles liées à la non-conformité.
- **Améliorer sa réputation et sa confiance** : les tests d'intrusion contribuent à préserver sa réputation en assurant la sécurité de son site.
- **Prévenir les pertes financières** : les tests d'intrusion permettent de prévenir les incidents en détectant les vulnérabilités susceptibles d'être exploitées.
- **Identifier les faiblesses dans les configurations personnalisées** : de nombreux sites WordPress sont fortement personnalisés, avec des thèmes sur mesure et des plugins spécifiques. Ces personnalisations peuvent introduire des failles de sécurité uniques, que seul un test d'intrusion peut efficacement identifier et évaluer.
- **Assurer sa continuité** : les tests d'intrusion aident à maintenir la disponibilité et la fiabilité du site, essentielles pour les activités commerciales en ligne.

### Méthodologie

![Méthodologie d'un test d'intrusion Wordpress](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/5.png)

Chez **Trackflaw**, nous sommes en mesure de procéder à un audit complet de votre site Wordpress pour éliminer tous risques (c'est votre jour de chance) ! 😉

Cette méthodologie s'articule autour de grandes étapes. Elle commence par une **phase de reconnaissance**.

#### Reconnaissance

L'auditeur commence par effectuer une **collecte des informations de base** :

   1. Déterminer la version de WordPress, les plugins et les thèmes utilisés.
   2. Identifier les technologies et les frameworks utilisés (`JavaScript`, `PHP`, etc.).
   3. Analyser les en-têtes `HTTP` pour d'éventuelles informations sensibles.

Par exemple, pour vérifier qu'un site web fonctionne sous Wordpress :

```bash
curl https://victim.com/ | grep 'content="WordPress'
```

Ou sinon, vous pouvez aussi utiliser l'excellente extension [Wappalyzer](https://www.wappalyzer.com/) comme sur le screen ci-dessous (pas très sécurisé le Wordpresse de la capture d'ailleurs...) ! 😀

![Wappalyser](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/wappalizer.png)


Par la suite, le pentester peut tenter de **récupérer des fichiers** :

   1. Tenter de télécharger des fichiers potentiellement sensibles, par exemple en libre accès dans le répertoire `wp-contents`.
   2. Rechercher des fichiers de sauvegarde ou des fichiers de configuration non protégés.

Petit exemple pour obtenir la liste des plugins et thèmes (lorsque cela est possible)

**Plugins**

```bash
curl -H 'Cache-Control: no-cache, no-store' -L -ik -s https://vuln.trackflaw.com/support/article/pages/ | grep -E 'wp-content/plugins/' | sed -E 's,href=|src=,THIIIIS,g' | awk -F "THIIIIS" '{print $2}' | cut -d "'" -f2
```

**Thèmes**

```bash
curl -s -X GET https://vuln.trackflaw.com/support/article/pages/ | grep -E 'wp-content/themes' | sed -E 's,href=|src=,THIIIIS,g' | awk -F "THIIIIS" '{print $2}' | cut -d "'" -f2
```

Enfin, l'auditeur **énumère les utilisateurs** :

   1. Identifier les utilisateurs et les rôles existants sur le site.
   2. Tenter de deviner les noms d'utilisateurs et les mots de passe par des attaques par force brute ou par dictionnaire.

Plusieurs moyens pour effectuer cette action :

- Par force brute des identifiants : `curl -s -I -X GET http://vuln.trackflaw.com/?author=1`.
- Via la route `wp-json` : `curl http://vuln.trackflaw.com/wp-json/wp/v2/users`.
- Via de l'énumération sur la page `wp-login.php`. 

#### Exploitation

Par la suite, l'auditeur est amené à étudier les vulnérabilités impactant le site, ses plugins et ses thêmes.

Quelques exemples de vulnérabilités :

- **Tests d'injection SQL** : exploiter des failles de sécurité dans les plugins ou le thème pour injecter du code SQL malveillant.
- **Cross-Site Scripting (XSS)** : injecter du code `JavaScript` malveillant dans le site pour détourner les utilisateurs.
- **Cross-Site Request Forgery (CSRF)** : forcer un utilisateur authentifié à effectuer des actions non désirées.

Pour cette partie, nous la laissons en exercice au lecteur. Nous n'allons quand même pas dévoiler tous nos secrets ! 😉

#### Outillage

Il existe des outils permettant **d'automatiser l'exploitation** et de **faciliter la tâche du pentester** durant le test d'intrusion comme par exemple :

- `Cmsmap`
- `Wpscan`

Quelques exemples ci-dessous 👇

```bash
cmsmap -s http://localhost -t 2 -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
wpscan --rua -e ap,at,tt,cb,dbe,u,m --url http://localhost --api-token <API_TOKEN> --passwords /usr/share/wordlists/external/SecLists/Passwords/probable-v2-top1575.txt
```

## Se protéger après le test d'intrusion

![Se protéger](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/6.png)

Une fois après avoir effectué votre test d'intrusion, il est important de suivre certaines étapes pour **sécuriser** votre site web :

1. Activer les mises à jour automatiques avec le code ci-dessous :

```php
define( 'WP_AUTO_UPDATE_CORE', true );
add_filter( 'auto_update_plugin', '__return_true' );
add_filter( 'auto_update_theme', '__return_true' );
```

2. Installer des plugins de sécurité comme [Wordfence](https://wordpress.org/plugins/wordfence/), [Sucuri Security](https://wordpress.org/plugins/sucuri-scanner/) ou [iThemes Security](https://wordpress.org/plugins/better-wp-security/).

**Quelques autres recommandations :**

1. Supprimer l'utilisateur administrateur par défaut.
2. Utiliser des mots de passe forts avec du 2FA.
3. Réviser périodiquement les permissions des utilisateurs.
4. Limiter les tentatives de connexion pour prévenir les attaques par force brute.
5. Renommer `wp-admin.php` et n'autoriser l'accès qu'en interne ou à partir de certaines adresses IP.
6. Désactiver le directory listing.

## Conclusion

Faire un test d'intrusion sur son site WordPress n'est pas un luxe mais une **nécessité dans l'environnement numérique actuel**. En identifiant proactivement les **vulnérabilités** et en **renforçant la sécurité du site**, vous pouvez protéger vos actifs numériques, maintenir la confiance des utilisateurs et assurer la continuité de vos opérations commerciales.

Face à la menace croissante des cyberattaques, les tests d'intrusion sont un investissement indispensable dans la sécurité d'un site **WordPress**. Prenez contact dés maintenant avec **Trackflaw** !

## Sources 

### Statistiques 

- https://lesmakers.fr/statistique-wordpress
- https://wpscan.com/statistics/

### Ressources

- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/wordpress