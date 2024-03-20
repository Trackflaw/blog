---
title: "Why do an intrusion test on its WordPress site"
description: "WordPress, as one of the most widely used content management systems (CMS) in the world, powers a significant portion of websites, ranging from personal blogs to corporate sites."
date: 2024-03-20T10:54:14+01:00
draft: false
images: [/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png]
featuredImage: "/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png"
featuredImagePreview: "/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/logo.png"
tags: ["Test d'intrusion", "Pentest", "Audit"]
---

# Why a Penetration Test is MANDATORY for Your Wordpress Site in 2024?

## Introduction

**WordPress**, as one of the **most widely used content management systems (CMS) in the world**, powers a significant portion of websites, ranging from personal blogs to corporate sites.

However, its popularity comes with increased security risks, making penetration testing crucial for safeguarding these sites against cyber attacks.

📈 Some staggering statistics (according to lesmakers.fr):

- The **#1** CMS in the world.
- Over **62% market share** among CMS.
- More than **43% of global websites** use WordPress.
- **9,000** free themes.
- **60,000** free active plugins.

<br>

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/1.png" title="More than 62% of sites using a CMS opt for WordPress" >}}

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/2.png" title="Over 455 million websites worldwide use WordPress." >}}


## A double-edged sword of popularity

**WordPress** is often targeted by attackers due to its widespread use.

Vulnerabilities in WordPress core, themes, or plugins can be exploited to compromise a site. Penetration testing helps identify these weaknesses before they can be exploited by malicious actors.

More alarming statistics 😅

- In 2023, there were over **90 million attacks** against WordPress sites. (source: https://www.wordfence.com/)
- More than **50% of WordPress sites** are attacked each year. (source: https://sucuri.net/)
- Over **90% of attacks** on WordPress sites target vulnerabilities in plugins, themes, or WordPress core itself. (https://www.wordfence.com/)

<br>

{{< figure src="/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/3.png" title="Proportion of CMS WordPress vulnerabilities (source: wpscan.com)." >}}

{{< admonition type=warning title="Caution" open=true >}}
These figures should be taken with caution. Indeed, it is very difficult to know the exact proportions of exploited vulnerabilities.
{{< /admonition >}}


## Why protect yourself?

Might seem like an obvious question, right? 😉

For several reasons:

- **To protect sensitive data**: WordPress sites often host sensitive data, such as user personal information and payment details.
- **To comply with security standards**: For businesses, compliance with security standards like GDPR or PCI DSS is not an option but a requirement.
- **To improve reputation and trust**: A secure site enhances user and customer trust. Conversely, a compromised site can severely damage a company's reputation.
- **To prevent financial losses**: Cyber attacks can lead to significant financial losses due to data theft, ransom for decrypting data, or the costs of restoring services.
- **To ensure business continuity**: A successful cyber attack can disrupt a WordPress site's operations, leading to downtime and affecting business continuity.

## Penetration testing: protection through attack

![Conducting a penetration test](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/4.png)

A penetration test, also known as a pentest, is an effective way to simulate an attack and identify security flaws in your **WordPress** site.

### Addressing the challenges

Let's revisit the previous challenges and apply them to the realm of penetration testing:

- **Protecting sensitive data**: A penetration test helps assess the robustness of data protection mechanisms, ensuring their integrity and confidentiality.
- **Complying with security standards**: A penetration test reveals whether a WordPress site meets requirements, thus avoiding potential penalties related to non-compliance.
- **Improving reputation and trust**: Penetration tests help preserve reputation by ensuring site security.
- **Preventing financial losses**: Penetration tests help prevent incidents by detecting vulnerabilities that could be exploited.
- **Identifying weaknesses in custom configurations**: Many WordPress sites are heavily customized, with bespoke themes and specific plugins. These customizations can introduce unique security flaws that only a penetration test can effectively identify and evaluate.
- **Ensuring business continuity**: Penetration tests help maintain site availability and reliability, essential for online business activities.

### Methodology

![Wordpress penetration testing methodology](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/5.png)

At **Trackflaw**, we are equipped to conduct a comprehensive audit of your WordPress site to eliminate all risks (lucky you)! 😉

This methodology revolves around major steps, beginning with a **reconnaissance phase**.

#### Reconnaissance

The auditor starts by collecting **basic information**:

   1. Determine the WordPress version, plugins, and themes used.
   2. Identify the technologies and frameworks used (`JavaScript`, `PHP`, etc.).
   3. Analyze `HTTP` headers for possible sensitive information.

For example, to verify if a website runs on WordPress:

```bash
curl https://victim.com/ | grep 'content="WordPress'
```

For example, to check if a website is running on WordPress:


Or else, you can also use the excellent [Wappalyzer](https://www.wappalyzer.com/) extension as shown in the screenshot below (the WordPress in the capture is not very secure, by the way...)! 😀

![Wappalyzer](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/wappalizer.png)


Subsequently, the pentester may attempt to **retrieve files**:

   1. Try to download potentially sensitive files, for example, those freely accessible in the `wp-contents` directory.
   2. Look for backup files or unprotected configuration files.

A small example to obtain the list of plugins and themes (when possible)

**Plugins**

```bash
curl -H 'Cache-Control: no-cache, no-store' -L -ik -s https://vuln.trackflaw.com/support/article/pages/ | grep -E 'wp-content/plugins/' | sed -E 's,href=|src=,THIIIIS,g' | awk -F "THIIIIS" '{print $2}' | cut -d "'" -f2
```

**Thèmes**

```bash
curl -s -X GET https://vuln.trackflaw.com/support/article/pages/ | grep -E 'wp-content/themes' | sed -E 's,href=|src=,THIIIIS,g' | awk -F "THIIIIS" '{print $2}' | cut -d "'" -f2
```

Finally, the auditor **enumerates users**:

   1. Identify existing users and roles on the site.
   2. Attempt to guess usernames and passwords through brute force or dictionary attacks.

Several methods to perform this action:

- By brute-forcing credentials: `curl -s -I -X GET http://vuln.trackflaw.com/?author=1`.
- Via the `wp-json` route: `curl http://vuln.trackflaw.com/wp-json/wp/v2/users`.
- Through enumeration on the `wp-login.php` page.

#### Exploitation

Subsequently, the auditor is tasked with studying vulnerabilities impacting the site, its plugins, and its themes.

Some examples of vulnerabilities:

- **SQL Injection Tests**: Exploit security flaws in plugins or themes to inject malicious SQL code.
- **Cross-Site Scripting (XSS)**: Inject malicious `JavaScript` code into the site to redirect users.
- **Cross-Site Request Forgery (CSRF)**: Force an authenticated user to perform unwanted actions.

For this part, we leave it as an exercise to the reader. We can't reveal all our secrets! 😉

#### Tooling

There are tools available that **automate exploitation** and **ease the pentester's task** during penetration testing, such as:

- `Cmsmap`
- `Wpscan`

Some examples below 👇

```bash
cmsmap -s http://localhost -t 2 -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"
wpscan --rua -e ap,at,tt,cb,dbe,u,m --url http://localhost --api-token <API_TOKEN> --passwords /usr/share/wordlists/external/SecLists/Passwords/probable-v2-top1575.txt
```

## Protecting yourself after the penetration test

![Protecting yourself](/images/pourquoi-faire-un-test-intrusion-sur-son-site-Wordpress/6.png)

Once you have performed your penetration test, it is important to follow certain steps to **secure** your website:

1. Enable automatic updates with the code below:
   
```php
define( 'WP_AUTO_UPDATE_CORE', true );
add_filter( 'auto_update_plugin', '__return_true' );
add_filter( 'auto_update_theme', '__return_true' );
```

1. Install security plugins like [Wordfence](https://wordpress.org/plugins/wordfence/), [Sucuri Security](https://wordpress.org/plugins/sucuri-scanner/), or [iThemes Security](https://wordpress.org/plugins/better-wp-security/).

**Some other recommendations:**

1. Remove the default admin user.
2. Use strong passwords with 2FA.
3. Periodically review user permissions.
4. Limit login attempts to prevent brute-force attacks.
5. Rename `wp-admin.php` and restrict access to it internally or from certain IP addresses.
6. Disable directory listing.

## Conclusion

Conducting a penetration test on your WordPress site is not a luxury but a **necessity in the current digital environment**. By proactively identifying **vulnerabilities** and **enhancing site security**, you can protect your digital assets, maintain user trust, and ensure the continuity of your business operations.

In the face of the growing threat of cyberattacks, penetration tests are an essential investment in the security of a **WordPress** site. Contact **Trackflaw** now!

## Sources

### Statistics

- https://lesmakers.fr/statistique-wordpress
- https://wpscan.com/statistics/

### Resources

- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/wordpress
