---
title: "Terraforming my home network"
date: 2026-08-03T20:00:00+02:00
description: "How I used Terragrunt, OpenTofu and Mikrotik to build out my home network"
type: "post"
image: "images/posts/terraforming-my-home-network/index.jpg"
---

I wanted to make my network simpler, so I fell into a rabbithole of routers and switches.

## How did we get here?

Before we get started, I want to clear up that I'm nowhere near a network engineer. I was perfectly happy with my Unifi devices, the Ubiquiti ecosystem
has a user friendly management controller and all the dashboards I could ever need.
It all started when a friend had an extra [RB1100AHx4](https://mikrotik.com/product/rb1100ahx4) laying around. With 13 Gigabit ethernet ports, I had more
connectivity than I could use in the forseeable future and it came with rackmounts for which I didn't even have a rack.

I could have stopped there, but I also got my hands on a [CSS326-24G-2S+RM](https://mikrotik.com/product/CSS326-24G-2SplusRM) switch and
a [wireless access point](https://mikrotik.com/product/RBcAP2nD). Both of these devices weren't my brightest idea, but that will become more clear
further down the post.

## Why is this about Terraform?

I was about to spend some money on buying networking hardware, so I might as well learn something from it. After years of using Unifi, the simplicity is the
thing that stuck with me, all is managed with the click of a button. And exactly those clicks of a button is what I cannot preach as an IT professional who is
allergic to ClickOps. I've spend years mastering infrastructure as code, reproducability and deployment pipelines, just for my home network to be managed by a mouse.
Not on my watch, when we're doing this again, we're doing it properly through Terraform and Git commits.

## Learning MikroTik

Configuring MikroTik devices is pretty straight forward, it all starts with the [Getting started guide](https://help.mikrotik.com/docs/spaces/ROS/pages/328151/First+Time+Configuration). _While
writing this post, I learned the new docs have moved, so I probably spent some time troubleshooting outdated documentation._ After booting my router, I put the documentation and the MikroTik
Reddit together and figured out I'll need WinBox to configure these devices.

### My first mistake

The download page of WinBox states: `Advanced desktop utility to manage RouterOS limitless configuration options.`. At that point in time, I didn't know yet what *RouterOS*
meant and that other variants existed. It was only when I booted my switch that I discovered that MikroTik supports multiple operating systems, in the case of the switch,
that's _SwitchOS_. This means that my switch is not manageable through WinBox, this also means that my infrastructure as code journey already had a bump before it even started.

### Back to WinBox

After crying myself to sleep over my beautiful but complex switch, I got back to figuring out how my router actually works. On a first time setup, MikroTik configures pretty sensible
defaults on the router. Ethernet interfaces are connected to the bridge, one of those interfaces receives internet when connected to an ISP modem and devices on other ports
receive an IP address and can start sending traffic. For such a complex looking device, first time setup was a breeze.

### Here comes automation

MikroTik does not offer a first party Terraform provider, which is a bit of a shame since this means no official support. Keeping the provider and the RouterOS API in sync
is community driven, so we'll see how far we go until things break. The good thing about community driven projects, is that there's an actual community. It didn't take long
until I stumbled upon this [blog post](https://mirceanton.com/posts/mikrotik-terraform-getting-started/) written by an absolute legend. The post talks me through configuring the
[provider](https://registry.terraform.io/providers/terraform-routeros/routeros/latest) and modifying the basic settings. Having a blog post to walk you through it is one thing,
but finding out the author open sourced their own configuration, restores your faith in the open source community.

Because of following the configuration I found on GitHub, I also followed the path of [Terragrunt](https://terragrunt.com/). I had never used this tool in production, but for
this use case, I'm pleasantly surprised. Reusing modules across different devices, or instantiating a module multiple times against the same device, still kept my repository
structure manageable.

```shell
.
|── bootstrap.cloudformation.yaml # Used for Terraform state
|── docs
|   └── rb1100ahx4.md
|── infrastructure
|   ├── globals.hcl
|   ├── router-rb1100ahx4
|   │   └── provider.hcl
|   └── switch-rb952ui-5ac2nd
|       └── provider.hcl
|── modules
|   ├── base
|   ├── network
|   └── firewall
```

Each module hold a single configuration item, each directory under configuration instantiates the module.

## Aaaaah so that's how VLANs work

I'll be honest, on premise networking was never my strong side. I have a cloud background, specifically AWS. Setting up networks consists about brainstorming about IP ranges,
creating a VPC with 3 subnets and if you're thorough, creating some NACLs. All of this has always abstracted away the actual workings of an IP network. Until today, because today
we find out why a device on a network is assigned a certain IP address and why that matters.

On my Unifi setup, I didn't really spend time to create different VLANs, I gathered all the hardware over the years, but the main advantage for me was being able to configure which
DNS server was configured by default when a device connected to my network. I could set my pihole as the DNS server, and that was all that mattered.

This time, I wanted to do better, at least the bare minimum: network devices go into a VLAN, servers go into a VLAN, trusted devices go into a VLAN, and guests keep their pesky
phones disconnected from the other devices in my network. With all this in mind, I got to the drawing board to gather some IP ranges for all devices to sit in. _For now, servers and trusted
devices are still in the same VLAN, I'll solve that issue when I have spare time again._ But now that I had the IP ranges in mind, 
I followed the [docs](https://manual.mikrotik.com/docs/bridging-and-switching/vlan#simple-vlan-routing) on how to configure those on my router. But that story
is only have true, I stole most of the implementation from <https://github.com/mirceanton/terraform-modules-routeros> which configures the VLANs and the bridge.

Configuring the VLANs, I had no idea what I was doing or what configuration meant. I come from AWS, I only know what ingress, egress and security groups mean. Moving over to
VLANs, this was a bit uneasy for me. But what I'm taking away from this is: "Untagged ports put a VLAN ID on a packet, tagged ports can route packages tagged with a VLAN ID".
So this means "When I ethernet port 3 as untagged for vlan 1000 and I connect my desktop to ethernet port 3, it will receive an IP address from the DHCP server in VLAN 1000".

During all this, I didn't touch a single firewall rule. I was used to my devices seeing eachother, so I'll solve that problem later. What mattered now, was that specific devices
received IP addresses from different VLANs. Networking devices got a certain IP prefix and trusted devices received another prefix. To me, that was a victory on its own.

## Wireless

Man, this made me feel all kinds of emotions. If my mistake with the SwitchOS was bad, I'll tell you the difference between `wifi-qcow` and `wifi-qcow-ac`.
I'm enjoying writing again, but I want to keep these posts short and sweet, so I'll tell you about my wifi journey in another post.

## References

- [Cover image](https://unsplash.com/photos/a-close-up-of-a-server-in-a-server-room-vSprjjDbu60) by [Tyler](https://unsplash.com/@tylergm) on Unsplash
- The absolute machine that is [mirceanton](https://github.com/mirceanton/)
- <https://forum.mikrotik.com/t/using-routeros-to-vlan-your-network/126489>
