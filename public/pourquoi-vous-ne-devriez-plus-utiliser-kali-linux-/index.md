# Pourquoi vous ne devriez PLUS utiliser Kali Linux ?


# Exegol : la meilleure alternative moderne à Kali Linux


## L'histoire de Kali Linux : une montée en puissance

**Kali Linux** est une distribution **incontournable** que l'on ne présente plus destinée aux professionnels de la sécurité et nottament aux **pentesters** et **auditeurs en sécurité offensive**. 

Or, avec l'avènement de nouvelles technologies et des alternatives plus légères, **faut-il encore utiliser Kali Linux** ? A travers cet article, revivez l'évolution de cet OS, ses alternatives, et comment des solutions comme **Exegol**, basées sur Docker, redéfinissent l'usage des environnements de hacking.

### Les origines de Kali

**Kali Linux**, tel qu’on le connaît aujourd’hui, est le résultat de plusieurs projets ayant évolué au fil du temps.

Deux distributions pionnières ont joué un rôle essentiel dans sa création :

- **WHAX** : Créé par Mati Aharoni, WHAX était une distribution dédiée aux tests d'intrusion.
- **Auditor Security Collection** : Développée par Max Moser, cette distribution était également dédiée à la sécurité.

Ces deux projets étaient basés sur **Knoppix**, une distribution Linux nottament célèbre pour sa bonne stabilité de son mode live, c’est-à-dire sans installation sur le disque dur.

### La naissance de BackTrack

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/1.png)


Le **26 mai 2006**, **BackTrack**, un nouveau système d'exploitation voit le jour avec sa version 1.0. Conçu pour être un OS complet pour les **tests d'intrusion**, il intégrait des outils phares tels que **Metasploit** ou **Nmap**.

**BackTrack 2.0** arrive en **mars 2007** avec des améliorations majeures, notamment l'intégration des **versions 2 et 3 de Metasploit Framework** (msf) et une restructuration du menu pour une meilleure accessibilité des outils.

En **juin 2008**, **BackTrack** passe à sa **version 3.0** avec des fonctionnalités supplémentaires comme **Maltego**, un outil d'analyse de données et de renseignements.

**BackTrack 4 R2** en **novembre 2010** améliore encore la compatibilité matérielle.

### Un coup de neuf

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/2.png)

En **août 2012**, avec la version **BackTrack 5 R3**, une restructuration importante s'opère avec une base **Ubuntu**. Cependant, c’est le **13 mars 2013** que le tournant majeur a lieu : **BackTrack devient Kali Linux**.

Sous l’égide **d'Offensive Security**, **Kali** est reconstruit à partir de Debian et s'appuie sur un système de paquets **Debian**, rendant sa gestion et son développement plus fluides.

### Kali Linux aujourd’hui

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/3.png)

Depuis, Kali n’a cessé de se développer :

- En **2019**, l’interface passe de GNOME à XFCE, allégeant l'OS.
- En **2020**, le shell par défaut devient **zsh**, offrant une meilleure ergonomie aux utilisateurs.

De nombreuses autres fonctionnalités suivent les années suivantes.

**Kali Linux** est aujourd'hui disponible sous diverses formes : **ISO**, **machine virtuelle (VM)**, **live USB**, et même sur mobile avec **Kali NetHunter**. Une version spéciale pour Windows est également disponible via le Windows Subsystem for Linux (WSL).

La nouveauté la plus récente est **Kali Purple**, proposant un ensemble d'outils pour la défense en cybersécurité, en complément des outils d’attaque.

## Alternatives à Kali Linux : d’autres OS pour le hacking

Même si **Kali** reste populaire, il existe plusieurs alternatives tout aussi performantes :

- **BackBox** : Une distribution basée sur Ubuntu, avec un focus particulier sur la simplicité et la légèreté.
- **BlackArch** : Basé sur ArchLinux, BlackArch offre une vaste collection d’outils pour les pentests.
- **Parrot OS** : Construit sur Debian, Parrot OS se distingue par son interface élégante et son orientation vers la sécurité et la vie privée.

## Exegol : la nouvelle révolution dans le hacking éthique (pentest)

![Exegol](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/4.png)

### Problématique

Les environnements de pentesting comme **Kali Linux** ou ses alternatives nécessitent souvent des **installations complexes**, des **configurations manuelles**, et peuvent être **lourds** pour certaines machines. C’est là **qu’Exegol**, une solution innovante basée sur Docker, **entre en jeu**.

### Docker : Un système de conteneurisation révolutionnaire

![Docker](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/5.png)

**Docker** est un système de conteneurisation qui permet d'exécuter des applications dans des environnements isolés. Il présente plusieurs avantages :

- **Sécurité** : Grâce à une isolation stricte, chaque conteneur fonctionne indépendamment des autres.
- **Portabilité** : Les conteneurs sont légers et peuvent être facilement déployés sur n’importe quel système.
- **Automatisation** : La gestion des conteneurs est simple et peut être entièrement automatisée.

### Présentation d’Exegol

**[Exegol](https://github.com/ThePorgs/Exegol)** est un environnement de pentesting basé sur Docker, offrant une flexibilité et une facilité d'utilisation **incomparables**. Il fonctionne pour n'importe quel utilisateur et crée un conteneur pour chaque client.

{{< figure src="/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/archi.webp" title="Architecture du projet d'Exegol" >}}

Les avantages d'Exegol sont multiples :

- Tous les outils sont facilement accessibles, avec des alias et des historiques préconfigurés.
- Le partage de fichiers entre l'hôte et le conteneur est possible.
- La journalisation des sessions de shell est automatisée, offrant un suivi complet des opérations.
- L'automatisation de tâche est aisée au lancement du conteneur.
- Un accès VNC graphique est disponible à travers le navigateur.

{{< admonition success "Ce qu'on adore ! 🥰" >}}
1. La description des différents outils installés sur [la documentation](https://exegol.readthedocs.io/en/latest/exegol-image/tools.html).
2. Les commandes **déjà enregistrées** (quel gain de temps !). Petit plus, connaissez vous [Arsenal](https://github.com/Orange-Cyberdefense/arsenal) pour ne perdre aucune commande ? 🔥
3. L'utilisation fonctionnelle d'applications graphiques comme **Firefox**, **Burp** ou encore **BloodHound** !
4. L'accès VNC simulant un bureau distant.
5. Le montage automatique d'un VPN au lancement d'un conteneur.
{{< /admonition >}}

### Fonctionnement d’Exegol

Exegol repose sur **trois dépôts principaux** :

- **Exegol** : Un wrapper Python pour simplifier l’utilisation.
- **Ressources** : Un dépôt contenant toutes les ressources nécessaires.
- **Dockerfiles** : Des fichiers Docker pour la création des conteneurs d’outils.

On y retrouve aussi un serveur **[Discord](https://discord.gg/cXThyp7D6P)** et un site internet pour la **[documentation](https://exegol.readthedocs.io/en/latest/)**.

Petit schéma juste en dessous 👇

{{< figure src="/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/techs.webp" title="Technologies du projet d'Exegol" >}}


Exegol propose plusieurs images spécialisées comme :

- **Web** : Pour les tests de sécurité web.
- **OSINT** : Pour l’intelligence en sources ouvertes.
- **AD** : Pour les environnements Active Directory.
- **Light et Full** : Des versions allégées ou complètes en fonction des besoins.

Exegol est un projet ouvert aux contributions des développeurs et est régulièrement présenté dans de grandes conférences. Un serveur Discord est également disponible pour échanger avec la communauté.

### Démonstration et utilisation

L'installation d'Exegol est vraiment très simple

1. Installez Docker avec la commande appropriée.
2. Installez le wrapper Exegol via pip ou depuis les sources. Plus d'infos sur la [page d'installation](https://exegol.readthedocs.io/en/latest/getting-started/install.html).
3. Et c'est tout : `exegol start master` 😃

Et d'ailleurs, on en parle juste la sur la chaine YouTube de Trackflaw 👇

{{< youtube RxGkG8HFFHs >}}


## Conclusion : aller vers le côté obscur, tu dois !

Si **Kali Linux** reste une référence, l'avenir semble se tourner vers des solutions plus **légères** et **portables** comme Exegol.

Utiliser **Kali en VM** est de plus en plus révolu face aux avantages offerts par Docker : performances accrues, portabilité, et flexibilité.

Exegol s’impose ainsi comme un outil du quotidien pour les professionnels du pentesting, offrant une expérience optimisée et moderne.

Lien vers le projet : https://github.com/ThePorgs/Exegol
