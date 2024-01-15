---
title: "Reworking my homelab with Talos"
date: 2024-01-15T20:00:00+02:00
description: "How I reworked my homelab from k3s to Talos"
type: "post"
image: "images/posts/k3s-to-talos/index.jpg"
---

## My homelab through the years

I've been self-hosting and tinkering around for a couple of years now. A couple years ago, I deployed my first Pi-Hole
on a Raspberry Pi. I was amazed by the possibilities of self-hosting and got dragged into the rabbit hole sooner than
I like to admit.

Through the years, I've been looking for ways to make my setup at home more reliable and easier to maintain. My first
step was to containerize everything. So instead of manually installing Pi-Hole, I manually started a Docker container.

I had some idea of where I wanted to go, but with my background in software development, I was not familiar with
infrastructure as code. There were too many tools to choose from, so I went with something I knew: Ansible.

As I got more familiar with containers, I started to look into ways to minimize management, I needed my infrastructure
to update itself. I started to look into Kubernetes, and I found a lightweight Kubernetes distribution called k3s. It
was easy to set up, and it was lightweight enough to run on my Raspberry Pi's. This change didn't particularly make my
setup more reliable, but it did make it easier to manage. I could now deploy and update application
using [Argo CD](https://argoproj.github.io/cd/) so I no longer needed to interact with the server itself, everything
was stored in Git.

This setup worked well for a couple of years. But was it good enough? This is the question I'm always asking myself
regarding my homelab. Without a handful of meetings and the burden of story points, it's actually quite fun to improve
on my setup. The one thing I wanted to improve was the overhead of the OS. I was really only working with kubernetes,
so why did I need a full-blown OS?

## Enter Talos

I've been attending some Kubernetes conferences and meetups, and I've been hearing a lot about
Talos. [Talos](https://www.talos.dev/) is a modern operating system for Kubernetes. It easy enough to set up, but most
important for me, it manages everything through code.

While looking into ways to improve on my setup, I also got my hands on an Intel NUC. I was getting tired of SD cards
and loud, small fans, so this was the ideal timing to improve on my hardware situation as well. I decided to go with
[Proxmox](https://www.proxmox.com/en/) as my hypervisor. I've had my eyes on virtual machines for a while now, but
ARM was not really supported. With Proxmox, I was hoping to finally saying goodbye to the tedious process of flashing
SD cards and thumb drives.

## Booting my first Talos node

After loading the Talos ISO into Proxmox and booting a virtual machine, the hardest part was done. Kudos to the Talos
team for understandable [documentation](https://www.talos.dev/v1.6/talos-guides/install/virtualized-platforms/proxmox/).

The node starts in no time, but is not ready to be used. So I generated my first machine config and assigned the first
VM as a control plane node. I am not really planning on extending the cluster with smaller nodes, but if I wanted to,
I can start more nodes and apply worker node configs to them.

```shell
# This bootstraps the control plane node
talosctl gen config talos-proxmox-cluster https://$CONTROL_PLANE_IP:6443 --output-dir _out
talosctl apply-config --insecure --nodes $CONTROL_PLANE_IP --file _out/controlplane.yaml

# This sets credentials
export TALOSCONFIG="_out/talosconfig"
talosctl config endpoint $CONTROL_PLANE_IP
talosctl config node $CONTROL_PLANE_IP

# This bootstraps etcd
talosctl bootstrap
```

I liked k3s with their setup scripts and joins tokens, but this feels even simpler.

## Migrating my applications

Good thing I've been using Argo CD to manage my applications. Migration was as simple as installing ArgoCD using Helm,
and applying a manifests that syncs the cluster with my Git repo.

_Small remark on data migration: I've used hostPath the last years and I've moved over to TrueNAS, so storage is outside
Kubernetes and I intend to keep it that way._

I use following manifest to guarantee that ArgoCD is always in sync with Git using
the [App of Apps](https://argo-cd.readthedocs.io/en/stable/operator-manual/cluster-bootstrapping/) approach.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  namespace: argocd
  name: sync
spec:
  destination:
    namespace: argocd
    server: 'https://kubernetes.default.svc'
  source:
    path: kubernetes/argocd/clusters/talos
    repoURL: 'git@my-argocd-repo'
    targetRevision: main
  project: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
```

## What did I learn?

- Talos is easy to set up and manage
- When exploring a new OS, replacing a VM is way easier than starting over with a USB drive. The Proxmox overhead is not
  noticeable, so this can was worth it.
- I finally got [Metallb](https://metallb.universe.tf/) working properly, so if I ever want to scale out my nodes, I
  can.

## Read more

- Chick-fil-A's [case with Talos](https://robkenis.github.io/edgecase-2023/wednesday/2-chick-fil-a/)
- [Introduction to Cilium](https://robkenis.github.io/edgecase-2023/thursday/6-cilium/). I've been running this on both
  clusters and it's amazing.