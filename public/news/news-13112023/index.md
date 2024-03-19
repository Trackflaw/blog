# Les4ActusCyber - Semaine du 13 novembre

    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/oNgin3SFvec" title="#Les4ActusCyber - Semaine du 13 novembre" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

## Vulnérabilité non négligeable dans le logiciel de messagerie Zimbra

Une faille de type "zero-day" dans le logiciel de messagerie Zimbra est actuellement exploitée par quatre groupes différents dans des attaques afin de voler des données de messagerie, des identifiants d'utilisateur et des jetons d'authentification.
La faille, répertoriée sous le nom de CVE-2023-37580 (score CVSS : 6.1), est une vulnérabilité XSS réfléchie affectant les versions antérieures à 8.8.15. Elle a été corrigée par Zimbra dans le cadre des correctifs publiés le 25 juillet 2023. Une exploitation réussie de la faille permet de prendre le contrôle du navigateur.


<br>

## Reptar : nouvelle vulnérabilité des processeurs Intel affectant les environnements virtualisés

Intel a publié des correctifs pour corriger une faille sévère, connue sous le nom de code Reptar, affectant ses processeurs. Identifiée sous le nom de CVE-2023-23583 (score CVSS : 8.8), cette faille permet une élevation de privilèges. Une exploitation de la vulnérabilité peut aussi permettre de contourner les limites de sécurité du processeur, selon Google Cloud.
Intel, dans le cadre des mises à jour de novembre 2023, a publié un microcode mis à jour pour tous les processeurs concernés. Pour le moment, il n'y a aucune preuve d'attaques actives utilisant cette vulnérabilité.


<br>

## Rappel du démarrage imminent de la campagne de nettoyage de compte Google

Google a lancé en aout 2023 une campagne d'avertissement à certains utilisateurs de la suppression imminente de leurs comptes inactifs à partir du 1er décembre 2023. Cette action ne concerne que les comptes n'ayant pas été utilisés ou connectés au cours des deux dernières années.
Les comptes inactifs sont davantage susceptibles d'être compromis, ce qui pourrait entraîner des activités malveillantes telles que le phishing ou l'usurpation d'identité.
Certaines exceptions sont prévues par Google, notamment pour les comptes avec une activité YouTube, un solde d'argent, ceux ayant publié des applications sur le Play Store, qui ne seront pas concernés par la suppression de compte.


<br>

## Faiblesse importante lors de la mise à jour de VMware Cloud Director Appliance

VMware Cloud Director Appliance a communiqué sur une nouvelle vulnérabilité permettant le contournement d'authentification dans le cas où VMware Cloud Director Appliance aurait été mis à niveau vers la version 10.5 à partir d'une version antérieure.
Un acteur malveillant disposant d'un accès réseau à l'appliance peut contourner les restrictions de connexion lors de l'authentification sur le port 22 (ssh) ou le port 5480 (console de gestion de l'appliance).
Ce contournement n'est pas présent sur le port 443 et sur une nouvelle installation de VMware Cloud Director Appliance 10.5. Aucun PoC n'est actuellement disponible.


