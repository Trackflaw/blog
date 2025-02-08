---
title: "The Mysterious Story of a Troubling Intel Chip"
description: "Discover the story of the Intel Management Engine, a hidden chip in Intel processors since 2008, capable of operating independently of the operating system."
date: 2025-02-03T15:36:37+01:00
draft: false
images: [/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png]
featuredImage: "/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png"
featuredImagePreview: "/images/histoire-mystèrieuse-inquiétante-puce-intel/logo.png"
tags: ["Penetration Testing", "Pentest", "Audit"]
author: "Thibaud Robin"
---

# Backdoor or Feature: The Mystery of the Intel Management Engine

## Introduction

In 2021, the estimated number of PCs worldwide was about **1.4 billion**. By the fourth quarter of 2022, **Intel held approximately 62% of the x86 processor market** for computers, equating to around **850 million PCs equipped with Intel processors**.

![Statistics](/images/histoire-mystèrieuse-inquiétante-puce-intel/0.png)

Now imagine the possibility of a government agency accessing any one of these computers.

That would be a number of machines equal to the combined population of the **United States, Indonesia, Brazil, and Canada**.

A chilling prospect, straight out of a sci-fi movie. Yet, for over a decade, researchers have been uncovering increasingly unsettling findings. What if this myth was actually **true**?

## A Troubling Discovery

![Igor Skochinsky](/images/histoire-mystèrieuse-inquiétante-puce-intel/1.png)

**Igor Skochinsky** is a computer engineer who graduated from the Belarusian State University in Belarus.

Graduating with honors, he began his career at a major software company while pursuing reverse engineering research in his free time.

Gradually, Igor gained notoriety on the internet by developing tools to **bypass iTunes file piracy protections** and exploring the internal systems of **Amazon's Kindle**. Suffice it to say, Igor has a keen taste for rather unconventional reverse engineering.

In **2008**, Igor joined Hex-Rays, the company behind the famous disassembler `IDA Pro`, where he contributed to the development of this essential tool for cybersecurity professionals. But Igor wanted to go further and share his research more widely.

### Black Hat USA 2009 Conference

{{< youtube AZqKVhPiSoc >}}

In **2009**, at the Black Hat USA conference, **two researchers from Invisible Things Lab** presented an innovative attack called the "`Ring -3 Rootkit`," targeting the Intel Management Engine (ME).

The Intel ME is a microcontroller embedded in Intel processors since 2008. It operates independently of the main system and remains active even when the computer is turned off, as long as it is plugged in.

This component is designed to help businesses and network administrators **remotely manage computers**: repairing, updating, or restarting a machine without being physically present.

It also monitors the PC's status: checking if everything is running smoothly or detecting hardware issues, acting as a **technical assistant built into the processor**.

### Features of the Intel ME

The Intel ME's features are as follows, and they are quite concerning:

- **Operating System**: Based on ThreadX RTOS by Express Logic.
- **Full Access**: Can access memory, the hard drive, network, etc.
- **Independent Operation**: Can continue running even if the computer is turned off or if the operating system fails.

![Features](/images/histoire-mystèrieuse-inquiétante-puce-intel/2.png)

### Exploitation by Researchers

The attack demonstrated by researchers was relatively simple:

1. **Identify memory regions**: Used by Intel ME.
2. **Modify and write**: In this area to inject malicious code.
3. **Install a rootkit**: Malicious software enabling surveillance, keylogging, and data exfiltration.

Even when deliberately attempting to disable this feature on a computer, exploitation was still possible.

The vulnerabilities were quickly patched, but this conference marked the beginning of extensive research, particularly for Igor, into this highly controversial component.

## In-Depth Analysis

In **2014**, Igor Skochinsky presented an in-depth analysis of the Intel ME at the REcon conference. This presentation was a turning point in understanding this technology.

{{< youtube 4kCICUPc9_8 >}}

### Structure of the ME

His presentation concluded with the following key points:

- **Standalone Microcontroller**: Integrated into the Intel chipset.
- **Operating System**: Based on Minix, a Unix-like system originally designed for educational purposes, which inspired Linus Torvalds to create the Linux kernel.
- **Independent Operation**: Functions separately from the main processor.

Igor also discovered that the ME has full access to memory and can interact with network interfaces without the main processor's involvement. The ME can access peripherals and data without leaving any visible traces in the operating system.

## The Arrival of a New Player

Igor’s work did not go unnoticed in the community. Many researchers seized the opportunity to collaborate on this dark component, particularly to disable it.

However, the task is far from easy, and Intel is not making it any simpler.

### The HAP Bit (High Assurance Platform)

![HAP Bit](/images/histoire-mystèrieuse-inquiétante-puce-intel/3.png)

While exploring the ME firmware, Igor discovered the existence of an HAP bit, originally designed to meet the needs of government agencies like the NSA. This bit acts as a "kill switch" allowing partial or complete deactivation of the ME. However, this feature has never been documented for the general public and is not available to users or commercial enterprises.

## The Shadow of a Backdoor

Doubt grows within the community. Why has this component remained in place for so many years? Why is Intel turning a blind eye to the issue?

Igor starts realizing that more and more researchers are becoming interested in this topic and that extensive studies had already been published before 2014, sometimes several years earlier.

### Discovered Vulnerabilities

![Backdoor?](/images/histoire-mystèrieuse-inquiétante-puce-intel/4.png)

Many other vulnerabilities have surfaced, notably in:

- **2010**: Vassilios Ververis, a Swedish student, published his thesis on the security of Intel’s AMT protocol, used by the ME.
- **2013**: A precursor attack presented by Patrick Stewin and Yuri Bystrov at the Chaos Communication Congress (CCC), exposing the weaknesses of Intel ME.
- **May 2017**: The "Silent Bob is Silent" vulnerability, affecting all major brands worldwide.
- **August 2023**: The "Downfall" vulnerability, allowing the reading of sensitive data.

## Deleting It Completely?

But is it really impossible to remove this parasitic chip from your computer? The answer is no! But it won’t be easy.

### Possible Solutions

There are several more or less complex methods to disable or remove Intel ME:

1. **Me_cleaner Project**: Use the open-source project [me_cleaner](https://github.com/corna/me_cleaner) by Nicola Corna to modify the ME firmware and remove non-essential partitions.
2. **Enabling the HAP Bit**: Via firmware programming tools or certain BIOS configurations.
3. **Alternative Firmware**: Coreboot/Libreboot, open-source alternatives to proprietary BIOS, replacing the manufacturer's firmware with a lightweight software that disables or removes Intel ME.
4. **Physical Removal of ME Modules**: Physically disabling the ME by modifying or removing specific hardware components.

## Conclusion

You probably feel like you're being watched now. But there’s no need to fall into paranoia. Igor Skochinsky continues his battle against the chip with many new studies and conferences.

Key takeaways:

- No proof that Intel ME is an intentional backdoor.
- Intel ME is not entirely deactivatable via BIOS.
- Intel ME can operate independently of network hardware.
- The ME does not actively monitor user activities.
- Intel ME is not a malicious tool designed for spying.
- The ME is not useless for end users, handling critical tasks like boot management, hardware diagnostics, and microcode updates.

Despite all the controversy, this chip still holds many mysteries and awaits you to uncover all its secrets.

The full story is available in video format on [Trackflaw's YouTube channel](https://www.youtube.com/watch?v=8wC5BfsSQFw):

{{< youtube 8wC5BfsSQFw >}}
