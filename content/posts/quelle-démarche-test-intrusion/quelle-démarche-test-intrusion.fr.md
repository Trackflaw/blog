---
title: "Quelle démarche choisir pour effectuer un test d'intrusion ?"
description: "Cet article détail et explique au lecteur les différentes démarches d'un test d'intrusion ainsi que comment bien faire son choix."
date: 2024-01-23T10:39:40+01:00
draft: false
images: [/images/quelle-démarche-test-intrusion/logo.png]
featuredImage: "/images/quelle-démarche-test-intrusion/logo.png"
featuredImagePreview: "/images/quelle-démarche-test-intrusion/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
---

# 🤔 Comment bien choisir sa démarche pour effectuer un test d'intrusion ?

## Boite noire, boite grise, boite blanche ? 

Dans le monde en constante évolution de la cybersécurité, où les cyberattaques deviennent de plus en plus sophistiquées, la réalisation de tests d'intrusion est **devenue une nécessité** pour les entreprises soucieuses de protéger leurs systèmes informatiques et données sensibles.

Ces tests, souvent désignés sous les termes de tests en **boîte noire**, **boîte grise** et **boîte blanche**, sont des composantes cruciales de toute stratégie de sécurité informatique robuste. Chacun de ces types de tests offre une approche unique pour évaluer la sécurité des systèmes d'information et identifier les vulnérabilités potentielles susceptibles d'être exploitées par des attaquants informatiques.

{{< admonition type=question title="Boite noire, boite grise, boite blanche ?" open=true >}}
Mais quelle est la différence entre ces trois termes ? Et comment choisir lequel vous conviendra le mieux ? Trackflaw vous éclaire juste en dessous 😉
{{< /admonition >}}

## Partie 1 - Les tests en boite noire

![Alt text](/images/quelle-d%C3%A9marche-test-intrusion/boite-noire.png)


### Définition et approche

Commençons par la première approche souvent utilisée, à tort 👎

Mais avant, petit rappel sur les test d'intrusion.

Les tests d'intrusion en **boîte noire** sont menés sans aucune connaissance préalable du système ciblé. Cette méthode simule une attaque extérieure par un attaquant informatique ne possèdant aucune information interne sur les systèmes informatiques de l'entreprise. L'objectif est **d'évaluer la sécurité du système** en se basant **uniquement sur les informations accessibles publiquement** (URL et IP), comme un véritable attaquant le ferait.

### Avantages

Il y a des avantages à utiliser cette méthode...

L'avantage principal des tests en boîte noire réside dans leur capacité à **révéler des vulnérabilités** pouvant être **facilement** exploitées par des attaquants externes. Ces tests fournissent une perspective réaliste de la manière dont un attaquant non informé pourrait s'introduire dans les systèmes.

### Inconvénients

... mais elle aussi des inconvénients (et pas des moindres ) ! 🙁

Cependant, les tests en boîte noire peuvent être plus **limités en termes de profondeur d'analyse**. Sans accès au code source ou à la configuration interne, certains types de vulnérabilités internes pourraient **rester non détectés**.

De plus, cette méthode peut nécessiter plus de temps pour identifier les failles de sécurité, puisque les auditeurs doivent d'abord découvrir et comprendre la structure du système. Et je vous avoue que c'est souvent très frustrant ! 😭

{{< admonition type=tip title="Parfait pour les petits budgets" open=true >}}
L'audit en boite noire est adapté pour parcourir **rapidement des larges périmètres** et pour un **petit budget**. Cependant, il faut prendre conscience du **manque d'exhaustivité** des tests effectués.

**Trackflaw** recommande **la boite noire** pour un audit flash, rapide et régulier sur des périmètres aux **risques limités**. 
{{< /admonition >}}

## Partie 2 - Les tests en boite grise

![Alt text](/images/quelle-d%C3%A9marche-test-intrusion/boite-grise.png)

### Définition et approche

Les tests en boîte grise constituent une **approche intermédiaire**, où le testeur possède un accès limité ou partiel aux informations internes du système. Cette méthode combine des éléments des tests de boîte noire. Elles permettent au testeur de comprendre certains aspects du système tout en explorant les vulnérabilités externes. En règle générale, l'audtieur reçoit en plus de **l'url et des ip**, des **comptes applicatifs** pour se connecter avec parfois de la **documentation**.

### Avantages

Cette méthode est souvent considérée comme **plus efficace en termes de temps et de coût** par rapport aux tests en **boîte noire**. En ayant un accès partiel aux données internes, les auditeurs peuvent cibler plus précisément leurs efforts, ce qui conduit à une identification plus rapide des failles de sécurité potentielles.

🤨 Mais cette méthode présente encore des inconvénients...

### Inconvénients

Bien que les tests en boîte grise offrent **un équilibre entre les deux autres méthodes**, ils peuvent ne pas être aussi complets que les tests en boîte blanche en termes de détection des vulnérabilités internes. De plus, cette méthode suppose que le testeur ait un certain niveau de connaissance préalable, ce qui peut ne pas refléter entièrement une attaque externe.

{{< admonition type=tip title="Le bonne équilibre" open=true >}}
La **boite grise** garantit un bon équilibre entre l'exhaustivité et l'économie.

**Trackflaw** recommande **la boite grise** pour l'audit d'une application web de façon rapide et exhaustif tout en respectant un budget limité. 
{{< /admonition >}}

## Partie 3 - Les tests en boite blanche

![Alt text](/images/quelle-d%C3%A9marche-test-intrusion/boite-blanche.png)

### Définition et approche

Les tests en **boîte blanche**, souvent appelés tests de "pénétration" basés sur le code. Il à noter que ce terme est à éviter. Il est conseillé de favoriser le terme test d'intrusion dans le langage courant français. Les élements de la boite blanche reprennent les élements de la **boite grise** soit les **url**, les **ip** ainsi que les **comptes applicatifs** en plus du **code source**.

Ce test implique une **connaissance complète du code source**, de l'architecture, et de la documentation du système. Les auditeurs utilisent cette information pour effectuer une analyse approfondie de la sécurité interne du système.

### Avantages

L'avantage principal des tests en **boîte blanche** est leur capacité à identifier les vulnérabilités **profondément** ancrées dans le code source et la configuration du système. Cette méthode permet une **évaluation complète de la sécurité interne**, y compris des aspects tels que la logique du code, la gestion des données sensibles, et les mesures de sécurité intégrées.

### Inconvénients

Cependant, les tests en **boîte blanche** peuvent être très complexes et chronophages, nécessitant une **expertise approfondie** en matière de programmation et d'architecture de systèmes.

{{< admonition type=tip title="Le choix de Trackflaw" open=true >}}
😊 Cette prestation est surement la meilleure à choisir !

**Trackflaw** recommande systématiquement **la boite blanche** pour un audit complet et exhaustif. 
{{< /admonition >}}

## Tableau récapitulatif

Pour conclure, voici un tableau récapitulatif des **3 démarches**.

| Critères                | **◼️ Boîte Noire**                                                            | **🔳 Boîte Grise**                                                                                    | **◻️ Boîte Blanche**                                                                                  |
| --------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Connaissance du système** | Aucune connaissance préalable du système.                                  | Connaissance partielle de l'application via des comptes.                                           | Connaissance complète du système, code source et documentation.                                    |
| **Avantages**               | - Réalisme élevé<br>- Identifie les vulnérabilités visibles de l'extérieur | - Équilibre entre profondeur et réalisme<br>- Efficacité en termes de temps et coût                | - Analyse en profondeur<br>- Identifie une grande majorité des vulnérabilités                      |
| **Limites**                 | - Moins de profondeur<br>- Peut manquer de nombreuses vulnérabilités       | - Moins détaillé que la boîte blanche<br>- Nécessite un certain niveau de connaissance préalable   | - Chronophage<br>- Couteux financièrement                                                          |
| **Temps et coût**           | Relativement faible : **2 à 4 jours**.                                     | Moyen : **4 à 6 jours**                                                                            | Elevé : **minimum 5 jours**                                                                        |
| **Contextes recommandés**   | - Test de la résilience externe<br>- Scénarios d'attaques réalistes        | - Quand une connaissance partielle est disponible<br>- Pour des tests équilibrés                   | - Audits internes approfondis<br>- Vérification de la conformité et des standards de développement |
| **Type d'attaque simulée**  | Attaquant externe sans connaissance spécifique.                            | Attaquant avec une connaissance limitée de l'entreprise.                                           | Attaquant interne ou audit de conformité.                                                          |
| **Exemple de scénario**     | Test de sécurité d'un ou plusieurs périmètres externes.                    | Test de la sécurité d'une application avec des informations d'identification utilisateur limitées. | Audit complet du code et des configurations de sécurité d'une application.                         |

Si vous avez des questions sur cet article n'hésitez pas à contacter Trackflaw sur les réseaux ou par email !

⬇️ **Suivez nous sur les réseaux :**

🔴 Toutes nos vidéos sur YouTube : youtube.com/@trackflaw<br>
📸 L'actualité Cyber sur Instagram et TikTok : instagram.com/trackflaw/ et tiktok.com/@trackflaw<br>
👉 En savoir plus sur Trackflaw : https://trackflaw.com<br>
📨 Evaluez votre sécurité dés maintenant : commande (at) trackflaw.com