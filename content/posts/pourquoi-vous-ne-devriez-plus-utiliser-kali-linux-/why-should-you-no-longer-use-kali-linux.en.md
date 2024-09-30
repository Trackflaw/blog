---
title: "Why You Should STOP Using Kali Linux"
description: "Kali Linux is probably the most widely used operating system in the offensive security world... but wrongly so! In fact, there are much better alternatives!"
date: 2024-09-30T15:21:12+01:00
draft: false
images: [/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/logo.png]
featuredImage: "/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/logo.png"
featuredImagePreview: "/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/logo.png"
tags: ["Penetration Testing", "Pentest", "Audit"]
---

# Exegol: The Best Modern Alternative to Kali Linux

## The History of Kali Linux: A Rise to Power

**Kali Linux** is a **must-have** distribution, widely recognized by professionals in the security field, especially for **pentesters** and **offensive security auditors**.

However, with the emergence of new technologies and lighter alternatives, **should you still use Kali Linux**? In this article, we revisit the evolution of this OS, explore its alternatives, and see how solutions like **Exegol**, based on Docker, are redefining hacking environments.

### The Origins of Kali

**Kali Linux**, as we know it today, is the result of several projects that have evolved over time.

Two pioneering distributions played an essential role in its creation:

- **WHAX**: Created by Mati Aharoni, WHAX was a distribution dedicated to penetration testing.
- **Auditor Security Collection**: Developed by Max Moser, this distribution was also focused on security.

Both projects were based on **Knoppix**, a Linux distribution particularly known for its live mode stability, meaning it could run without installation on the hard drive.

### The Birth of BackTrack

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/1.png)

On **May 26, 2006**, **BackTrack**, a new operating system, was born with version 1.0. Designed to be a comprehensive OS for **penetration testing**, it included key tools such as **Metasploit** and **Nmap**.

**BackTrack 2.0** arrived in **March 2007** with major improvements, including the integration of **versions 2 and 3 of the Metasploit Framework** (msf) and a restructured menu for better tool accessibility.

In **June 2008**, **BackTrack** reached **version 3.0**, introducing additional features like **Maltego**, a data analysis and intelligence tool.

**BackTrack 4 R2** in **November 2010** further improved hardware compatibility.

### A New Look

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/2.png)

In **August 2012**, with the release of **BackTrack 5 R3**, a major restructuring occurred, using an **Ubuntu** base. However, the real turning point came on **March 13, 2013**: **BackTrack became Kali Linux**.

Under the guidance of **Offensive Security**, **Kali** was rebuilt from Debian and adopted the **Debian** package system, making its management and development more fluid.

### Kali Linux Today

![BackTrack](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/3.png)

Since then, Kali has continued to evolve:

- In **2019**, the interface switched from GNOME to XFCE, lightening the OS.
- In **2020**, the default shell became **zsh**, providing better ergonomics for users.

Many other features have followed in the subsequent years.

**Kali Linux** is now available in various forms: **ISO**, **virtual machine (VM)**, **live USB**, and even on mobile with **Kali NetHunter**. A special version is also available for Windows via the Windows Subsystem for Linux (WSL).

The latest addition is **Kali Purple**, offering a set of tools for cybersecurity defense, complementing offensive tools.

## Alternatives to Kali Linux: Other Hacking OS Options

Although **Kali** remains popular, there are several equally powerful alternatives:

- **BackBox**: A distribution based on Ubuntu, with a particular focus on simplicity and lightness.
- **BlackArch**: Based on ArchLinux, BlackArch offers a vast collection of pentesting tools.
- **Parrot OS**: Built on Debian, Parrot OS stands out for its elegant interface and emphasis on security and privacy.

## Exegol: The New Revolution in Ethical Hacking (Pentest)

![Exegol](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/4.png)

### The Problem

Pentesting environments like **Kali Linux** or its alternatives often require **complex installations**, **manual configurations**, and can be **heavy** for certain machines. This is where **Exegol**, an innovative Docker-based solution, **comes into play**.

### Docker: A Revolutionary Containerization System

![Docker](/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/5.png)

**Docker** is a containerization system that allows applications to run in isolated environments. It offers several advantages:

- **Security**: Each container operates independently of the others, thanks to strict isolation.
- **Portability**: Containers are lightweight and can be easily deployed on any system.
- **Automation**: Container management is simple and can be fully automated.

### Introducing Exegol

**[Exegol](https://github.com/ThePorgs/Exegol)** is a Docker-based pentesting environment offering **unmatched** flexibility and ease of use. It works for any user and creates a container for each client.

{{< figure src="/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/archi.webp" title="Exegol Project Architecture" >}}

The benefits of Exegol are numerous:

- All tools are easily accessible, with preconfigured aliases and command histories.
- File sharing between the host and container is possible.
- Shell session logging is automated, providing a complete operation history.
- Task automation is easy at container startup.
- VNC graphical access is available through the browser.

{{< admonition success "What We Love! 🥰" >}}
1. The detailed descriptions of the installed tools in [the documentation](https://exegol.readthedocs.io/en/latest/exegol-image/tools.html).
2. The **pre-recorded** commands (what a time saver!). By the way, do you know [Arsenal](https://github.com/Orange-Cyberdefense/arsenal) to never lose a command? 🔥
3. The functional use of graphical applications like **Firefox**, **Burp**, or **BloodHound**!
4. VNC access simulating a remote desktop.
5. Automatic VPN mounting at container startup.
{{< /admonition >}}

### How Exegol Works

Exegol is based on **three main repositories**:

- **Exegol**: A Python wrapper to simplify usage.
- **Resources**: A repository containing all necessary resources.
- **Dockerfiles**: Docker files for creating tool containers.

There's also a **[Discord](https://discord.gg/cXThyp7D6P)** server and a website for **[documentation](https://exegol.readthedocs.io/en/latest/)**.

Here’s a quick diagram below 👇

{{< figure src="/images/pourquoi-vous-ne-devriez-plus-utiliser-kali-linux-/techs.webp" title="Exegol Project Technologies" >}}

Exegol offers several specialized images like:

- **Web**: For web security testing.
- **OSINT**: For open-source intelligence.
- **AD**: For Active Directory environments.
- **Light and Full**: Lighter or complete versions depending on needs.

Exegol is an open project for developers and is regularly featured in major conferences. There's also a Discord server available for community exchanges.

### Demonstration and Use

Installing Exegol is very simple:

1. Install Docker with the appropriate command.
2. Install the Exegol wrapper via pip or from the sources. More info on the [installation page](https://exegol.readthedocs.io/en/latest/getting-started/install.html).
3. That’s it: `exegol start master` 😃

And by the way, check it out on Trackflaw's YouTube channel 👇

{{< youtube RxGkG8HFFHs >}}

## Conclusion: To the Dark Side, You Must Go!

While **Kali Linux** remains a reference, the future seems to be turning towards lighter and more **portable** solutions like Exegol.

Using **Kali in a VM** is increasingly obsolete compared to the advantages offered by Docker: increased performance, portability, and flexibility.

Exegol thus establishes itself as an everyday tool for pentesting professionals, offering an optimized and modern experience.

Project link: https://github.com/ThePorgs/Exegol
