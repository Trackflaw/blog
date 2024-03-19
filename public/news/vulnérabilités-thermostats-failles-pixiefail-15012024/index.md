# Ransomware sur les thermostats connectés et faille PixieFail impactant l'UEFI - Les4ActusCyber : semaine du 15 janvier

    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/KEBLewfxv28" title="#Les4ActusCyber - Semaine du 15 janvier" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

## Vulnérabilités critiques dans les thermostats et systèmes intelligents Bosch

Des failles de sécurité majeures ont été découvertes dans les thermostats Bosch BCC100 et les systèmes intelligents Rexroth NXA015S-36V-B de Bosch. Ces vulnérabilités permettraient l'exécution de code arbitraire par des attaquants. Bosch a corrigé ces failles, notamment la CVE-2023-49722 (score CVSS 8.3), en fermant un port réseau utilisé pour le débogage.
Ces failles concernent le microcontrôleur WiFi des thermostats et peuvent entraîner des opérations malveillantes comme le détournement de trafic ou l'installation de rançongiciels sur les boulonneuses Rexroth Nexo.



<br>

## GitHub effectue un changement de clés suite à une vulnérabilité majeure

GitHub a procédé à un changement de clés en réponse à une vulnérabilité critique (CVE-2024-0200 au score CVSS 7.2) qui aurait pu exposer des informations d'identification. Cette vulnérabilité touchait également GitHub Enterprise Server (GHES) et a été corrigée dans plusieurs versions de GHES.
GitHub a aussi rectifié un autre bug (CVE-2024-0507, score CVSS 6.5), permettant une élévation de privilèges. La firme recommande aux utilisateurs d'importer les nouvelles clés et de mettre à jour leurs systèmes.


<br>

## Les failles PixieFail de l'UEFI menacent des millions d'ordinateurs

Les failles PixieFail, trouvées dans la pile TCP/IP de l'UEFI par Quarkslab, exposent les ordinateurs à des risques de RCE, de DoS et de vol de données. Ces vulnérabilités, présentes dans le TianoCore EFI II (EDK II), affectent les microprogrammes UEFI de plusieurs fabricants.
Ces failles, dont la CVE-2023-45229 (score CVSS 6.5), peuvent être exploitées pour réaliser des attaques DNS et DHCP, des fuites d'informations et des dénis de service. L'exploitation nécessite plusieurs prérequis dont le fait d'être présent sur le même réseau local des victimes. L'impact et l'exploitabilité de ces vulnérabilités dépendent aussi de la version spécifique du micrologiciel et de la configuration par défaut du démarrage PXE.


<br>

## Chrome corrige (encore) une vulnérabilité 0day activement exploitée

Google a mis à jour Chrome pour corriger une vulnérabilité de jour zéro (CVE-2024-0519) dans le moteur V8 JavaScript et WebAssembly. Cette faille permettait l'accès à la mémoire hors limites et était activement exploitée.
Il est conseillé aux utilisateurs de Chrome et de navigateurs basés sur Chromium de mettre à jour vers les dernières versions pour se protéger contre cette menace et d'autres problèmes de sécurité récemment corrigés.


Cet article vous a intéressé ?


