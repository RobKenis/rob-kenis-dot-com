---
title: "Policy as Code"
date: 2022-10-03T18:53:07+02:00
description: "This is meta description"
type: "post"
image: "images/masonary-post/post-2.jpg"
draft: true
categories:
  - "Food"
tags:
  - "Photos"
  - "Food"
---

### The problem

Developers need something, so they come to the core/ops team. Best case, you put this
in the service catalog. Anyhow, lots of communication.

One way to solve this is guardrails:

- preventive: SCP, unauthorized when you do something wrong
- detective: aws config, security hub. You have a dashboard and poke the teams.

--> The problem, you only get notified when you're almost done and it's wrong. Long feedback loop, lots of friction.

### The solution

How do we let teams deploy things without the ops team interfering? something like devops for security

cfn-guard: validates rules on json or yaml: https://github.com/aws-cloudformation/cloudformation-guard
Run this thing pre-commit or in a build pipeline. If you don't want to fail the build, use guard risks.

- [ ] Investigate on how to run this on cloudformation hooks
- When a config is changed in AWS Config, run guard
- AWS Cloud Control API: https://aws.amazon.com/cloudcontrolapi/. This returns some resources config as cfn

#### How to get started

- It's not perfect yet. Installation is trash.
- https://github.com/aws-cloudformation/aws-guard-rules-registry

### Challenges

- Where do I store my rules?
- Integrating with CloudFormation!
- https://cloudcustodian.io/ what's this?