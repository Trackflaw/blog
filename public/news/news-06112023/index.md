# Les4ActusCyber - Semaine du 06 novembre

    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/cRulsXkn-2c" title="#Les4ActusCyber - Semaine du 06 novembre" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
   </div>

   <div class="flex-items">
      <p>Tous les lundis, Trackflaw revient sur les 4 actualités cyber et techniques importantes de la semaine précédente.</p>
      <br>
      <p><strong>Plus d’informations sur nos réseaux :</strong></p>
      <p>🔴 Pour s’abonner à la chaine <a href="https://www.youtube.com/@trackflaw" target="_blank" rel="noopener noreffer ">YouTube</a> de Trackflaw.</p>
      <p>📸 Pour suivre l’actualité Cyber sur <a href="https://www.instagram.com/trackflaw/" target="_blank" rel="noopener noreffer ">Instagram</a>.</p>
      <p>👉 Pour visiter le site web de <a href="https://trackflaw.com" target="_blank" rel="noopener noreffer ">Trackflaw</a>.</p>
   </div>
</div>

    
<br>

## WhatsApp introduit une nouvelle fonctionnalité de confidentialité

WhatsApp déploie officiellement une nouvelle fonction de confidentialité dans son service de messagerie, appelée "Protect IP Address in Calls", permettant de masquer les adresses IP des utilisateurs à d'autres parties en relayant les appels via ses serveurs.
Cette fonctionnalité rend plus difficile la déduction de la localisation d'un utilisateur. Toutefois, l'activation de l'option de confidentialité a pour contrepartie une légère baisse de la qualité de l'appel.
Ce système existe déjà chez Apple sous le nom de iCloud Private Relay.


<br>

## Failles critiques dans le logiciel de supervision informatique Veeam ONE

Veeam a publié des mises à jour de sécurité pour corriger quatre failles dans sa plateforme de surveillance ONE, dont deux sont jugées critiques.
Pour le moment, les descriptions sont assez floues. La première faiblesse CVE-2023-38547, au score CVSS de 9.9, permet à un utilisateur non authentifié d'accéder au serveur SQL et d'y exécuter des commandes. La deuxième, CVE-2023-38548 au score CVSS  de 9.8, permet de récupérer le condensat NTLM du compte utilisé par Veeam.
Des correctifs pour ces vulnérabilités sont disponibles.


<br>

## Lace Tempest exploite activement le logiciel d'assistance informatique SysAid

L'acteur malveillant Lace Tempest a été associé à l'exploitation d'une faille de type "zero-day" dans le logiciel d'assistance informatique SysAid.
Lace Tempest, connu pour avoir diffusé le ransomware Cl0p, a par le passé exploité des failles critiques dans les serveurs MOVEit Transfer et PaperCut.
Le problème, répertorié sous le nom de CVE-2023-47246, concerne une faille de traversée de chemin permettant d'entraîner une exécution de commande via l'application. Cette faiblesse a été corrigée par SysAid dans la version 23.3.36 du logiciel.
Des PoC sont facilement obtenables sur Internet.


<br>

## Google Agenda : nouveau mécanisme de Command&Control utilisé par les attaquants

Google a communiqué concernant un PoC public exploitant son service Agenda afin d'héberger une infrastructure de commande et de contrôle (C2).
L'outil, appelé Google Calendar RAT (GCR), utilise les événements de Google Calendar pour le C2 à l'aide d'un compte Gmail. Il a été publié pour la première fois sur GitHub en juin 2023.
GCR, exécuté sur une machine compromise, interroge périodiquement la description de l'événement Calendar à la recherche de nouvelles commandes. Il exécute ces commandes sur l'appareil cible, puis met à jour la description de l'événement avec la sortie de la commande.


