---
title: "Reverse tab nabbing, a phishing method on steroids."
description: "Dive into the depths of 'reverse tab nabbing,' an incredibly effective phishing technique. Discover how hackers cleverly exploit your browser tabs to redirect you to malicious sites while making you believe you are safely browsing familiar sites. Through a realistic scenario, we show you step-by-step how this attack unfolds and highlight the exploitable vulnerabilities. Learn essential measures to protect yourself, such as avoiding the use of the target=_blank attribute or incorporating rel=noopener noreferrer. This article is a must-read for strengthening your cybersecurity and thwarting modern phishing traps."
date: 2023-11-16T17:44:12+01:00
draft: false
images: [/images/reverse-tabnabbing/main.png]
featuredImage: "/images/reverse-tabnabbing/main.png"
featuredImagePreview: "/images/reverse-tabnabbing/main.png"
tags: ["Phishing", "Pentest", "Hacking"]
author: "Thibaud Robin"
---

# 💉 Reverse tab nabbing, a phishing method on steroids.

## Do you know "reverse tab nabbing"?

🐟 Reverse tab nabbing is a phishing attack technique that redirects the original tab of a browser to a malicious page. This technique is particularly insidious because it can trick users into believing they are still on the legitimate site they initially visited.

## An Example

To understand this attack, here is a realistic scenario:

1️⃣ &nbsp;A victim browses a vulnerable site and clicks on a bait link pointing to https://legit-store.com

2️⃣ &nbsp;The site legit-store.com offers an attractive discount on their products.

3️⃣ &nbsp;While the user is occupied, the site legit-store.com redirects the user's social network tab to an identical phishing site.

4️⃣ &nbsp;The user closes the legit-store.com site (the discounts weren't that interesting).

5️⃣ &nbsp;They return to their social network tab... which now contains the fake phishing site.

6️⃣ &nbsp;The user, unsuspecting, "logs in" to the fake site. 😭

## Understanding the Vulnerability

The social network site is too permissive, allowing links to be created like this:

```html
<a href="USER INPUT" target="_blank" rel="opener">
```

But where's the problem? 🤔

In a situation where an attacker can control the `href` attribute of an `<a>` tag with the attributes `target="_blank"` and `rel="opener"`, the attacker can point this link to a website under their control (in this case, the website https://legit-store.com).

Once the victim clicks on the link and accesses the attacker's website, this malicious site can control the original page via the JavaScript object `window.opener`.

If the page does not have the attribute `rel="opener"` but only contains `target="_blank"`, it is also vulnerable.

## Exploitation

An easy way to exploit this behavior is to change the location of the original website through the JavaScript function `window.opener.location = https://attacker.com/victim.html`. This allows the attacker to redirect the victim to another website under their control that resembles the original site, enabling them to mimic the original site's login form and request the user's credentials.

However, it is interesting to note that the attacker can now control the `window` object of the original website. They can exploit it in other ways to perform additional attacks (perhaps by modifying JavaScript events to exfiltrate information to a server they control?).

To illustrate the animation at the end of the article, the site https://legit-store.com will execute the following JavaScript code on its page:

```html
<script>
window.opener.location = "http://fake-good-website.com/login.html";
</script>
```

This code will perform the redirection of the victim's first tab.

## Going Further

As mentioned earlier, the attacker controls all functions related to the `window` variable of the previous tab.

Here are some other possible actions:

- `opener.closed`: Returns a boolean value indicating whether a window has been closed.
- `opener.frames`: Returns all iframe elements in the current window.
- `opener.length`: Returns the number of iframe elements in the current window.
- `opener.opener`: Returns a reference to the window that created the window.
- `opener.parent`: Returns the parent window of the current window.
- `opener.self`: Returns the current window.
- `opener.top`: Returns the topmost browser window.

That's a lot of information! 😭

## Protection

1️⃣ Do not use the target="_blank" attribute.

2️⃣ If it is absolutely necessary, add the attributes rel="noopener noreferrer".

You can also directly modify the JavaScript function `window.open` and add the values `noopener,noreferrer` in the `windowFeatures` parameter of the `window.open` function.

Finally, it is also possible to add the HTTP security header `Referrer-Policy: no-referrer` to each HTTP response sent by the application. This configuration ensures that no referrer information is sent with the page's requests.

More information: https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#tabnabbing

## TL;DR

👇 Watch the animation below, and everything will become clearer!

![Alt text](/images/reverse-tabnabbing/reverse-tabnabbing.gif)
