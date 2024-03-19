# Le reverse tab nabbing, méthode de phishing sous stéroïdes.


# 💉 Le reverse tab nabbing, méthode de phishing sous stéroïdes.

## Connaissez vous le "reverse tab nabbing" ?

🐟 Le reverse tab nabbing est une technique d'attaque par hameçonnage consistant à rediriger la page d'origine d'un onglet vers une page malveillante. Cette technique est particulièrement vicieuse car elle peut tromper les utilisateurs en leur faisant croire qu'ils sont toujours sur le site légitime qu'ils ont initialement visité.

## Un exemple

Pour comprendre cette attaque, voici ci-dessous un scénario réaliste concernant ce type d'attaque.

1️⃣ &nbsp;Une victime navigue sur un site vulnérable et clique sur un lien aguicheur pointant vers https://legit-store.com

2️⃣ &nbsp;Le site legit-store.com propose une superbe réduction sur leurs produits.

3️⃣ &nbsp;Pendant que l'utilisateur est occupé, le site legit-store.com redirige l'onglet du réseau social de l'utisateur vers un site de phishing identique.

4️⃣ &nbsp;L'utilisateur ferme le site legit-store.com (pas si intéressante que ça les réducs).

5️⃣ &nbsp;Il retourne sur son onglet de réseau social... contenant le faux site de phishing.

6️⃣ &nbsp;L'utilisateur ne se doute de rien et se "reconnecte" sur le faux site. 😭

## Comprendre la faille

Le réseau social est trop permissif et permet de de créer des liens de cette façon : 

```html
<a href="SAISIE UTILISATEUR" target="_blank" rel="opener">
```

Mais où est le problème ? 🤔

Dans une situation où un attaquant peut contrôler l'argument `href` d'une balise `<a>` avec les arguments `target="_blank"` et `rel="opener"`, l'attaquant peut faire pointer ce lien vers un site web sous son contrôle (ici le site site web https://legit-store.com).

Une fois que la victime clique sur le lien et accède au site web de l'attaquant, ce site web malveillant est capable de contrôler la page originale via l'objet javascript `window.opener`.

Si la page n'a pas d'attribut `rel="opener"` mais contient uniquement `target="_blank"` , elle est également vulnérable.

## L'exploitation

Une façon facile pour abuser de ce comportement serait de changer l'emplacement du site web original à travers la fonction JavaScript `window.opener.location = https://attacker.com/victim.html`. Cela permettrait de rediriger l'utilisateur victime vers un autre site web contrôlé par l'attaquant ressemblant au site original, de sorte qu'il puisse imiter le formulaire de connexion du site web original et demander des informations d'identification à l'utilisateur.

Cependant, il est intéressant de note que l'attaquant peut maintenant contrôler l'objet window du site web original. Il peut aussi en abuser d'autres façons pour effectuer d'autres attaques (peut-être en modifiant les événements javascript pour exfiltrer des informations vers un serveur qu'il contrôle ?)

Pour reprendre l'animation à la fin de l'article, le site https://legit-store.com va exécuter le code JavaScript ci-dessous sur sa page :

```html
<script>
window.opener.location = "http://fake-good-website.com/login.html";
</script>
```

Ce code permettra réaliser la redirection du premier onglet de la victime.

## Allez plus loin

Comme dis plus haut, l'attaquant maitrise toute les fonctions liées à la variable `windows` du précédent onglet.

Voici quelques actions aussi réalisable :

- `opener.closed` : Renvoie une valeur booléenne indiquant si une fenêtre a été fermée ou non.
- `opener.frames` : Retourne tous les éléments de l'iframe dans la fenêtre courante.
- `opener.length` : Renvoie le nombre d'éléments de l'iframe dans la fenêtre actuelle.
- `opener.opener` : Renvoie une référence à la fenêtre qui a créé la fenêtre.
- `opener.parent` : Renvoie la fenêtre parent de la fenêtre actuelle.
- `opener.self` : Retourne la fenêtre courante.
- `opener.top` : Renvoie la fenêtre de navigateur la plus haute.

Ca en fait des informations ! 😭

## Se protéger

1️⃣ Ne pas utiliser l'attribut target="_blank"

2️⃣ Si il est vraiment nécessaire, rajouter les arguments rel="noopener noreferrer"

Vous pouvez aussi directement modifier la fonction JavaScript `window.open`, et ajouter les valeurs `noopener,noreferrer` dans le paramètre `windowFeatures` de la fonction `window.open`.

Enfin, il est aussi possible d'ajouter l'en-tête de sécurité HTTP `Referrer-Policy: no-referrer` à chaque réponse HTTP envoyée par l'application. Cette configuration garantit qu'aucune information de référence n'est envoyée avec les requêtes de la page.

Plus d'informations : https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#tabnabbing

## TL;DR

👇 Regardez l'animation ci-dessous, tout sera plus clair !

![Alt text](/images/reverse-tabnabbing/reverse-tabnabbing.gif)
