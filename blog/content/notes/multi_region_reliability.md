---
title: "Build, understand and operate fault-tolerant multi-region applications through Resilience Testing and Automation"
date: 2022-10-03T13:33:12+02:00
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

Customers have 3 main reasons to go with multi-region applications.
First, disaster recovery. If you design properly in one region, for
example with multiple AZ, you're good (most of the time). Second,
data residency requirements. In some regulated industries, you need
to keep customer data in a certain region. Third, low-latency for
global audience. 2 way handshake SSL can take 200ms when going from 
Thailand to US. CloudFront and AWS Global Accelerator are good solutions,
but might not be enough.

Things against multi region:
- expensive
- operational complexity: what about rollbacks and testing?
- consistency: replication on dynamodb global tables is not strongly consistent

### The architecture

First region has a CloudFront with S3 for static assets and API Gateway
for a Lambda with DynamoDB. Even if you don't set caching on CF, you
get into the right network faster, so good.

Second region is the exact same and has data replication on DynamoDB.

The user comes in and has a DNS record pointing to one of the regions.
Routing policy is set to failover.

### The demo

https://k6.io/

An easy way to create chaos in Lambda, is to reduce the concurrency
to 0.
Through R53 health checks, when one of the regions becomes unhealthy,
R53 will change the failover record to the other region.
When you think naming stuff is hard, let's talk about threshold for
alarms :).
DNS TTL is important, because when one of the regions goes down, you'll have 
downtime until the TTL expires.

https://aws.amazon.com/global-accelerator/ ?

