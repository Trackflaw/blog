---
title: "What tools to use for a Penetration Test?"
description: "How to choose the right tools for an intrusion test? Read more in the article below"
date: 2024-05-24T11:58:40+01:00
draft: false
images: [/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.en.png]
featuredImage: "/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.en.png"
featuredImagePreview: "/images/quels-outils-utiliser-pour-un-test-dintrusion/logo.en.png"
tags: ["Penetration Test", "Pentest", "Audit"]
---

# 🛠️ Tools in the Field of Penetration Testing

## Importance of Penetration Testing

**Penetration testing**, also known as **pentesting** (or colloquially as penetration testing), is an essential practice for **evaluating the security of an IT system**. It involves simulating real attacks to **identify** and **fix** **vulnerabilities** before actual malicious attackers exploit them.

To conduct a successful penetration test, it's crucial to have the right **tools**. However, navigating the plethora of available tools can be overwhelming.

Don't worry, in this article, we've **listed all the essential tools** for an effective pentest to best meet your needs. 🥳

### Recap

But first, why are penetration tests important? 🤔

Quick recap:

Penetration tests allow you to:

- **Identify** vulnerabilities before they are exploited.
- **Evaluate** the resilience of systems against real attacks.
- **Improve** the overall security posture of the organization.
- **Comply** with security regulations and standards.
- **Train** security teams on the latest attack and defense techniques.

In short, everything necessary for good business management 😉

{{< admonition tip "More Info!" >}}
To go further, several articles are available to help you choose your penetration test well.

- How to choose a penetration test provider: available [here 👈](/choisir-son-prestataire-de-test-intrusion/)
- What approach to choose for a penetration test: available [👉 right here](/quelle-démarche-test-intrusion/)!
{{< /admonition >}}

### Tools or No Tools?

{{< admonition warning "Beware of False Promises!" >}}
Some companies tend to offer genuine penetration tests via **automated tools**. Unfortunately, an automated tool cannot, for now, achieve the same comprehensiveness as a confirmed auditor (but maybe very soon with Trackflaw's next innovation 😉).
{{< /admonition >}}

It is therefore important to remember that an effective and responsible penetration test is a **balanced mix of manual tests coupled with automated tests**.

More details on our methodology below 👇

## Tools for Penetration Testing

The **tools** used for penetration testing can be classified into several categories: **reconnaissance**, **vulnerability analysis**, **exploitation**, and **post-exploitation**. Each of these categories contains specialized tools **facilitating** the pentest process.

To make reading easier, the context to consider here is an **external web penetration test/pentest**.

{{< admonition info "1001 Tools" >}}
There are thousands of tools. It is therefore impossible to talk about them all exhaustively here. In this article, we only discuss the **essential tools for us** (and for you!) that we use daily.
{{< /admonition >}}

### 1. Reconnaissance tools

![Recon Tools](/images/quels-outils-utiliser-pour-un-test-dintrusion/1.png)

Reconnaissance and service mapping is the **first step** in a web penetration test.

It involves **collecting information** about the target, such as accessible services, accessible technologies, etc. Reconnaissance tools help pentesters gather valuable data that can be directly or indirectly useful for the penetration test.

Some examples of tools:

- `Nmap`: **nmap** is the network scanner par excellence, it allows identifying active hosts on a network, available services, and running software versions. Nmap is extremely flexible and can be used for complete reconnaissance of a particular target.
  
- `Subfinder`: **subfinder** is a passive subdomain discovery tool, optimized for speed and lightness. It uses passive sources to identify valid subdomains of a website. [GitHub](https://github.com/projectdiscovery/subfinder).

- `Gau (GetAllUrls)`: **gau** quickly retrieves all possible URLs for a given domain from various sources such as Wayback Machine and Common Crawl. We use it to enhance our perimeter view. [GitHub](https://github.com/lc/gau).

- `TheHarvester`: **theHarvester** is an information-gathering tool that retrieves emails, names, subdomains, IP addresses, and banners from public sources such as search engines and PGP databases. Truly excellent! [GitHub](https://github.com/laramies/theHarvester).

- `Wafw00f`: **wafw00f** detects and identifies web application firewalls (WAF) by sending HTTP requests and analyzing the responses to determine the security countermeasures deployed by the target site. [GitHub](https://github.com/EnableSecurity/wafw00f).

- `CORScanner`: **CORScanner** checks the CORS (Cross-Origin Resource Sharing) configurations of websites to identify poorly configured policies that could allow cross-origin attacks. [GitHub](https://github.com/chenjj/CORScanner).

- `Feroxbuster`: **feroxbuster** is a brute force tool for web directories, allowing you to quickly discover hidden files and directories on a server by sending HTTP requests. Our little **favorite** at Trackflaw 🥰 [GitHub](https://github.com/epi052/feroxbuster).

{{< admonition success "Our Top 3 Reconnaissance Tools at Trackflaw" >}}
If you only had to keep 3 tools, we recommend keeping the following 3 tools for your reconnaissance phase:

1. `Nmap`: essential for service discovery.
   
2. `Feroxbuster`: a little gem written in Go for quickly discovering hidden directories and files.
   
3. `Gau`: a gem for finding forgotten application routes that are hard to find both passively and actively.
{{< /admonition >}}

### 2. Vulnerability scanning tools

![Recon Tools](/images/quels-outils-utiliser-pour-un-test-dintrusion/2.png)

These tools help **identify security flaws** in systems and applications. They automate much of the vulnerability detection process.

1. `Burp Suite`: **Burp Suite** is a comprehensive set of tools for testing the security of web applications. It allows for both manual and automated analyses to identify various vulnerabilities, such as SQL injections, XSS flaws, and more. It has a very powerful scanning module in its paid version. [Website](https://portswigger.net/burp).

2. `Nuclei`: **Nuclei** is a fast and customizable vulnerability scanner based on simple YAML templates. It is extensible and easy to use, allowing for the detection, prioritization, and correction of security vulnerabilities. A must-have! 🥰 [GitHub](https://github.com/projectdiscovery/nuclei).

3. `ZAP (Zed Attack Proxy)`: **ZAP** is a tool for attacking and detecting vulnerabilities in web applications. It offers a variety of features to automate security testing, including active scanning, passive analysis, and manual penetration testing. Often criticized (wrongly), the ZAP scan module is very effective compared to the BurpPro scanner. And all this **for free**! [GitHub](https://github.com/zaproxy/zaproxy).

4. `Nikto`: **Nikto** is a somewhat outdated web server scanner and less efficient than its competitors. But it can sometimes yield good surprises [GitHub](https://github.com/sullo/nikto).

5. `{WP|Droope|Joom|Moodl}Scan`: **WPScan**, **Droopescan**, **Joomscan**, and **Moodlscan** are security scanners for their respective CMS (you can easily guess each CMS I think 😉). Powerful and comprehensive, they are interesting to run during a specific audit. [GitHub of WPScan for example](https://github.com/wpscanteam/wpscan).

6. `testssl.sh`: **testssl.sh** is a command-line tool for analyzing SSL/TLS configurations. Very practical! [GitHub](https://github.com/drwetter/testssl.sh).

{{< admonition failure "What We Do Not Recommend" >}}
Among all these tools, some stand out while others are not very interesting. Here are a few to avoid 😟

- `Nessus`: an effective vulnerability scanner for internal penetration tests, but it is very little useful and effective externally compared to its prohibitive price.
  
- `Qualys`: a vulnerability scanner specialized in external environments, it is an expert in false positives and loves to overrate all the "_vulnerabilities_" detected (if we can call them that...) because, no, a TLS configuration supporting version 1.1 is not a critical flaw (bad memory sorry, give the money back) 😡 

- `OpenVAS`: known in the collective imagination as the reference free vulnerability scanning tool, the results are very disappointing, incomprehensible, and very messy. It struggles to renew itself but remains an interesting tool due to its free nature.
{{< /admonition >}}

{{< admonition success "Our Top 3 Scanning Tools at Trackflaw" >}}
Here are the 3 must-have tools for effectively locating vulnerabilities:

1. `Nuclei`: Probably the most revolutionary tool of the lot, both for its comprehensiveness and its price (free!). However, it requires some technical prerequisites to achieve good results.
   
2. `BurpSuite Pro`: BurpSuite is certainly the most essential tool during a web penetration test. The comprehensiveness of its scanner in its paid version makes it very effective in discovering vulnerabilities and provides real support to the pentester.
   
3. `Zap`: The scan module of ZapProxy is impressive. By comparison, it finds a large majority of the vulnerabilities discovered by its paid big brother BurpSuite Pro. But it has the advantage of being completely free.
{{< /admonition >}}

### 3. Exploitation tools

![Exploit Tools](/images/quels-outils-utiliser-pour-un-test-dintrusion/3.png)

Once vulnerabilities are identified, exploitation tools allow verification of whether these flaws can be exploited to gain unauthorized access.

{{< admonition warning "Caution When Using" >}}
Be cautious when using these tools!

They can cause significant damage and service disruptions if misused. Always research the tool's consequences before executing it on your target!
{{< /admonition >}}

Some examples of the most well-known tools:

1. `Metasploit`: **Metasploit** is a modular penetration testing framework that allows for developing, testing, and executing exploits. It is widely used for detecting and exploiting vulnerabilities. [GitHub](https://github.com/rapid7/metasploit-framework).

2. `SQLMap`: **SQLMap** is an automated SQL injection tool that allows testing and exploiting SQL injections in web applications. It supports various databases and provides features for data extraction, bypassing WAFs, and more. [GitHub](https://github.com/sqlmapproject/sqlmap).

3. `SSRFmap`: **SSRFmap** is a tool for exploiting Server-Side Request Forgery (SSRF) vulnerabilities, helping find and exploit SSRF vulnerabilities by automating attacks and providing advanced data exfiltration features. [GitHub](https://github.com/swisskyrepo/SSRFmap).

4. `NoSQLMap`: **NoSQLMap** is a tool used to test and exploit NoSQL databases. It supports several types of NoSQL databases and offers features for NoSQL injections, detection of injections, and other attacks specific to NoSQL databases. [GitHub](https://github.com/codingo/NoSQLMap).

5. `SearchSploit`: **SearchSploit** is a command-line utility for searching exploits in the Exploit-DB database. It allows pentesters to quickly access public exploits without needing a constant internet connection. [GitHub](https://github.com/offensive-security/exploitdb).

{{< admonition success "Our Favorite Exploitation Tools at Trackflaw" >}}
Here are the 3 must-have tools for effectively exploiting vulnerabilities:

1. `Metasploit`: A true historical toolbox in the field of security, this framework allows for all kinds of offensive actions, from scanning to post-exploitation, making it indispensable for any offensive engagement. A must-have!
   
2. `SearchSploit`: In addition to Metasploit, this little search tool allows you to easily consult the large Exploit-DB database without having to use a web browser. Very practical!
{{< /admonition >}}

### 4. Post-exploitation Tools

![Post-Exploitation Tools](/images/quels-outils-utiliser-pour-un-test-dintrusion/4.png)

Finally, post-exploitation tools are used after **gaining initial access** to maintain persistent access and further explore the compromised system.

{{< admonition danger "Caution (Again!) When Using" >}}
Like the previous tools, post-exploitation tools can cause **significant damage** if not mastered. They can also greatly degrade the initial security level of the target.

It is therefore **strongly** advised to obtain the commander's authorization before any use!
{{< /admonition >}}

A small non-exhaustive list:

1. `Weevely`: **Weevely** is a web shell designed for post-exploitation. It offers over 30 modules to assist with administrative tasks, maintain access, provide situational awareness, elevate privileges, and spread within the target network. [GitHub](https://github.com/epinna/weevely3).

2. `Cobalt Strike`: **Cobalt Strike** is a commercial post-exploitation tool used to assess the resilience of systems against advanced persistent threats (APT). It allows for simulating real attacks, controlling compromised systems, and conducting reconnaissance and exploitation activities. [Official site](https://www.cobaltstrike.com/).

3. `Sliver`: **Sliver** is an open-source command and control (C2) framework. It offers a variety of features for executing commands, managing sessions, and handling payloads. [GitHub](https://github.com/BishopFox/sliver).

4. `Havoc`: **Havoc** is a modern red teaming and post-exploitation framework allowing simulation of advanced attacks against networks and systems. It offers an intuitive user interface and easy integration with various security tools. [GitHub](https://github.com/HavocFramework/Havoc).

5. `Mythic`: **Mythic** is a flexible and extensible C2 framework used for penetration testing and red teaming operations. It allows managing multiple agents, creating custom payloads, and controlling compromised systems via a web interface. [GitHub](https://github.com/its-a-feature/Mythic).

{{< admonition success "Our Favorite Post-Exploitation Tools at Trackflaw" >}}
Here are our 3 favorite tools during our post-exploitation steps:

1. `Weevely`: Greatly facilitates managing web shells on PHP applications. Unfortunately, it does not work on other languages (the `kraken` tool might be a new alternative).
   
2. `Sliver`: Very functional, free, and practical C2. To be used in addition to Mythic.

3. `Mythic`: Same as Sliver. To be used in addition to Sliver.
{{< /admonition >}}

{{< admonition failure "Cobalt Strike or Not?" >}}
Cobalt Strike is probably the most well-known and widespread C2 system among Red Teamers but also among attackers.

Although it is a **very effective** product, it is **difficult to obtain** legally, and its license is **very expensive** (around €3,500). We do not recommend its use outside of a commercial Red Team activity.
{{< /admonition >}}

## Our Advice

Phew 🥵! So much information!

But don't leave yet; we still have some tips for you 👇

### Optimizing Your Penetration Test

Some (not so trivial!) tips for conducting and optimizing your penetration test:

1. **Planning and Preparation**: Before starting a penetration test, make sure to plan and define the objectives well. This includes identifying targets and obtaining the necessary permissions.

2. **Correlate Tools**: Using a combination of tools to increase your audit's comprehensiveness can be an excellent solution. For example, combine `Nmap` NSE scripts with `Nuclei` templates while using the right `Metasploit` auxiliary modules.

3. **Regular Tool Updates**: Penetration testing tools should be updated regularly to ensure they can detect and exploit the latest vulnerabilities. That's why we recommend using `Exegol` (more details later in the article).

4. **Detailed Reports**: A detailed report of the penetration test results is essential. It should include identified vulnerabilities, proof of concepts, and recommendations for fixing security flaws.

5. **Continuous Training**: Auditors should continuously train and stay informed about the latest security techniques and tools. Participating in conferences, workshops, and online training can be beneficial.

Using the **right tools** and following **best practices**, penetration tests can significantly improve your organization's security. 🎯

### Going Further

As mentioned earlier, there is a much more practical solution than traditional pentesting operating systems like `KaliLinux` or `BlackArch`: [Exegol](https://exegol.readthedocs.io/en/latest/).

A small excerpt from the documentation:

> **Exegol** is a powerful, yet simple-to-use, community-driven hacking environment for anyone to use in their daily activities.
>
> **Exegol** is the best solution for deploying powerful pentesting environments safely, easily, and professionally. No more unstable, insecure systems lacking major offensive tools. Kali Linux (and similar alternatives) are excellent toolboxes for learners, students, and junior pentesters. But professionals have different needs, and their context requires an entirely new design.

And to learn more, a dedicated video is available on Trackflaw's YouTube channel: 👇

{{< youtube RxGkG8HFFHs >}}

## Conclusion

A lot of information... But only the essentials! 😅

Penetration tests are an **essential** component of any organization's security strategy.

Using a combination of reconnaissance, vulnerability analysis, exploitation, and post-exploitation tools, pentesters can identify and fix security flaws before they are exploited by malicious attackers.

Trackflaw is available to help you in this endeavor. Contact us: https://trackflaw.com/commande/
