---
title: "Nouvelle faille critique dans la libc & faille Gitlab - Les4ActusCyber : semaine du 29 janvier"
date: 2024-01-29T08:00:00+0000
draft: false
images: [/images/logo.png]
featuredImage: "/images/logo.png"
featuredImagePreview: "/images/logo.png"
hiddenFromHomePage: True
---
    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/kZlDcscXcNA" title="Nouvelle faille critique dans la libc & faille Gitlab - #Les4ActusCyber : semaine du 29 janvier" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

## Lourde sentence pour un ex-ingénieur de la CIA

Joshua Adam Schulte, ancien ingénieur de la CIA, a été condamné à 40 ans de réclusion le 1er février pour avoir divulgué des documents classifiés à WikiLeaks et pour possession de matériel pédopornographique. Cette fuite, qualifiée de "Pearl Harbor numérique", a coûté des centaines de millions de dollars à la CIA et a compromis gravement la sécurité nationale.
Les informations sensibles partagées par Schulte comprenaient une série d'outils de piratage et d'exploits appelés Vault 7 et Vault 8. Elles ont été publiées par WikiLeaks à partir du 7 mars 2017, sur une période de huit mois.


<br>

## Faille critique dans la Glibc des systèmes Linux

Un débordement de tampon basé sur le tas dans la bibliothèque GNU C (CVE-2023-6246, score CVSS 7.8) permet aux attaquants locaux d'obtenir un accès root sur des systèmes Linux. Affectant les principales distributions comme Debian, Ubuntu, et Fedora, cette vulnérabilité nécessite une attention immédiate afin d'éviter des élévations de privilèges.
Cette vulnérabilité a été publiée à la suite d'une autre faille sévère dans la même bibliothèque appelée Looney Tunables (CVE-2023-4911, CVSS score : 7.8) 


<br>

## GitLab corrige (encore une fois!) une nouvelle faille importante

GitLab a émis des correctifs pour une vulnérabilité importante (CVE-2024-0402, score CVSS 9.9) permettant l'écriture de fichiers arbitraires lors de la création d'un espace de travail par un utilisateur authentifié. Les utilisateurs sont priés de mettre à jour leurs installations pour éviter toute exploitation malveillante.
Au score CVSS assez haut, la faiblesse semble beaucoup moins importante que la dernière (CVE-2023-7028). Un attaquant authentifié peut l'utiliser pour effectuer des attaques Dos et de l'injection HTML.


<br>

## Cloudflare cible d'une attaque importante pour vol de code source et à de documents internes

Cloudflare senble avoir été victime d'une attaque orchestrée par un groupe d'attaquants profesionnels, entraînant un accès non autorisé à ses serveurs Atlassian et à une partie de son code source. La société a pris des mesures de sécurité étendues en réponse, bien que l'attaque n'ait pas compromis son réseau mondial ni ses services clients.
L'intrusion aurait eu lieu entre le 14 et le 24 novembre 2023. Pas moins de 120 dépôts de code ont été consultés, dont 76 auraient été exfiltrés par l'attaquant.

