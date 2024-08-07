# Vulnérabilité critique chez Gitlab et suite de la compromission de Mandiant - Les4ActusCyber : semaine du 08 janvier

    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/lOCeVpWk3Us" title="#Les4ActusCyber - Semaine du 08 janvier" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

## GitLab corrige des vulnérabilités critiques

GitLab a rectifié deux vulnérabilités majeures, dont une permettant la prise de contrôle de comptes (CVE-2023-7028, score CVSS de 10.0). Cette faille, due à un défaut dans la vérification des courriels, affecte les versions de GitLab Community Edition (CE) et Enterprise Edition (EE) de 16.1 à 16.7.
Le correctif est disponible dans les versions 16.5.6, 16.6.4 et 16.7.2, et rétroporté aux versions antérieures. Une autre faille critique (CVE-2023-5356, score CVSS 9.6) concerne les intégrations Slack/Mattermost. GitLab recommande de mettre à jour immédiatement les instances concernées.


<br>

## Piratage du compte X de Mandiant par une attaque de force brute

Mandiant a subi une attaque de force brute sur son compte X, menée par un groupe ayant acheté l'accès. En raison de lacunes dans l'authentification à deux facteurs, le compte a été compromis le 3 janvier 2023.
L'attaquant a utilisé le compte pour diffuser des liens de phishing, menant à un draineur de crypto-monnaie. Des acteurs malveillants utilisent CLINKSINK depuis décembre 2023 pour siphonner des fonds en crypto-monnaie Solana (SOL), réalisant des profits illicites significatifs.


<br>

## Arrestation d'un Ukrainien de 29 ans, roi du cryptojacking

Un Ukrainien de 29 ans a été arrêté pour avoir établi un système de cryptojacking, générant plus de 2 millions de dollars de profits illicites. L'arrestation a eu lieu à Mykolaiv, en Ukraine, avec le soutien d'Europol et d'un fournisseur de services en ligne.
Le cryptojacking consiste à utiliser les ressources informatiques d'autrui pour extraire des crypto-monnaies. L'opération impliquait des comptes compromis, des mineurs clandestins et parfois, de l'élevation de privilèges pour un accès accru.


<br>

## Juniper corrige une vulnérabilité RCE critique dans ses pare-feu et commutateurs

Juniper Networks a corrigé une vulnérabilité RCE (CVE-2024-21591, score CVSS 9.8) dans ses pare-feu SRX et commutateurs EX Series. Cette faille permettrait à un attaquant de provoquer un déni de service ou d'exécuter du code à distance.
La vulnérabilité, causée par une fonction non sécurisée, affecte plusieurs versions de Junos OS. Les utilisateurs sont invités à mettre à jour leurs systèmes ou à désactiver J-Web pour limiter l'accès aux hôtes de confiance.


