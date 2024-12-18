# Les4ActusCyber - Semaine du 04 décembre

    
<div class="flex-container">
   <div class="flex-items">
   <iframe width="456" height="811" src="https://www.youtube.com/embed/R2mn9isxvaM" title="#Les4ActusCyber - Semaine du 04 décembre" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
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

## Meta renforce la sécurité avec le chiffrement par défaut sur Messenger :

Meta introduit le chiffrement de bout en bout (E2EE) par défaut sur Messenger pour les appels et messages personnels. Cette initiative majeure, fruit d'une refonte, vise à protéger les conversations, mais exclut encore l'E2EE pour la messagerie de groupe, toujours en test.
Malgré l'introduction des "conversations secrètes" en 2016, Instagram de Meta propose également l'E2EE, mais de manière limitée géographiquement et non activée par défaut. Meta insiste sur le renforcement de la confidentialité des échanges avec cette couche supplémentaire de sécurité.


<br>

## WordPress corrige un mécanisme pouvant mener à des failles critiques

La version 6.4.2 de WordPress corrige une vulnérabilité majeure permettant une attaque combinée, menant à l'exécution de code PHP arbitraire. Cependant, cette faille nécessite la présence d'une fonctionnalité de désérialisation non maitrisée afin d'être exploitée. La classe WP_HTML_Token agit comme gadget lors d'une exploitation de type POP chain.
Les utilisateurs sont invités à vérifier manuellement leurs sites pour s'assurer qu'ils utilisent la dernière version et éviter l'utilisation de fonctions de désérialisation dans le code au profit d'autres comme l'encodage/décodage JSON.

<br>

## LogoFail : vulnérabilités UEFI exposant les appareils à des attaques importantes

Les failles "LogoFAIL" dans le code UEFI de divers fournisseurs indépendants de micrologiciels et de systèmes d'exploitation (IBV) permettent des attaques importantes comme le déploiement de logiciels malveillants, le contournement du Secure Boot et de l'Intel Boot Guard.
Ces vulnérabilités affectent x86 et ARM et sont spécifiques à l'UEFI et à l'IBV. La méthode d'exploitation a été publiée durant la conférence Black Hat Europe et concerne des failles basées sur un débordement de mémoire tampon. L'exploitation nécessite cependant de gros prérequis.


<br>

## Atlassian publie des correctifs critiques concernant des vulnérabilités de type RCE

Atlassian a sorti des correctifs pour quatre failles majeures dans ses logiciels, potentiellement exploitables pour exécuter du code à distance. Ces vulnérabilités affectent plusieurs produits, notamment Confluence, Jira Service Management, et Atlassian Companion pour macOS. Ces vulnérabiliés varient de la désérialization à l'injection de template.
Il est fortement recommandéde mettre à jour vers les versions corrigées afin d'éviter les risques d'exploitation de ces failles de sécurité. Le détail des versions est disponible sur le site du constructeur.


