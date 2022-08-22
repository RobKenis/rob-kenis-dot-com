---
title: Keynote with Werner Vogels
image: images/posts/keynote-with-werner-vogels/index.jpg
date: 2019-12-05T08:18:36+01:00
tags: aws-reinvent-2019
type: "post"
---

Expectations are high, the 2018 Keynote with Werner Vogels brought us a lot. Custom Lambda runtimes, Lambda layers and a million new databases. Deepracer was introduced, Amazon Forecast got announced, it was an overall amazing experience. So we got up early, got our breakfast burrito and buckled up for the ride.

> There's no compression algorithm for experience - Werner Vogels' T-Shirt team, 2019
> Sometimes innovation is about focussing on the things that will never change for your customers - Jeff Bezos

## Virtualization
The bread and butter of the compute parts from day one. Classical virtualization has been around for a long time. x86 has come to life by major research at Stanford and revolutionized the virtualization landscape. We really pushed boundaries of virtualization over time, but we're still stuggling with a couple of issues. All guest OS's are fighting for the host resources, especially for network. Guests would see network jitter because they're fighting for the same network. AWS Nitro reinvented the virtualization to solve these problems, and reduce virtualization overhead. Amazon took the lessons they learned in software and applied them to hardware.
Microservices are the small building blocks that you can quickly improve on, it's time to bring these to hardware.

![Amazon builders library](/images/posts/keynote-with-werner-vogels/banner.jpg)

### AWS Nitro System
Step 1: Move the network component to a separate card, the first thing they did in 2016. It took another 2 years to learn what happens when you offload components to a second card.
Step 2: Move EBS processing to a separate card.
Step 3: Offload all I/O to separate cards.
Step 4: Move the management components to Nitro controller.

#### Nitro volume attach
An EBS volume attachement talks to the Nitro controller, which then talks to the OS level controller. The pre-nitro hypervisor introduces way more jitter. The Nitro hypervisor increased IOPS tremendously, the network bandwitch increased fron 14Gb/s to 19Gb/s.
C5 instances have performance close to bare metal, this is because the hypervisor layer is so thin that it introduces zero to no latency for the Guest OS. Network optimized instances improved network throughput 4x because of the Nitro System.

#### Kill Dom0
Do not trust the thing. You could do a memory dump which is a massive security risk. By removing [Dom0](https://wiki.xenproject.org/wiki/Dom0), you can remove SSH which closes a lot of security holes.

## Passive communications design
The Nitro controller talks to the hypervisor, not the other way around. The external control plane can talk to the Nitro controller, but not the other way around. When the communication happens the other way around, you can conclude your system is compromised. Inside the nitro controller, all components can talk to eachother. With nitro, everything is encrypted by default with no performance loss. By the way, don't even trust your guests, make sure they can not do anything with the hardware. Thay may not change volatile memory.

### Nitro: the base for innovation
Live updates from the micro part without anything taken down. Start running bare metal and create outposts. This is all enabled by Nitro which controls the environments.

### Protect sensitive data
[Nitro Enclanves](https://aws.amazon.com/ec2/nitro/nitro-enclaves/) **NEW** constantly checks if code is not compromised. Customers want control over sensitive data. Nitro changes the way we think about your compute environment.

## Firecracker
### Fargate
Fargate provides serverless compute for containers. Security is number one priority. In fargate, each copy of an application runs in its own machine under the hood, isolated from other machines in Fargate. This ensures isolation at multiple levels. Starting from this week, you can run Kubernetes workloads on Fargate. When a traffic spike comes in, Kubernetes takes a while to spin up more instances introducing latency. This is called underprovisioning. Fargate allocates the right amount of compute per pod, only inducing latency when pods are spinning up. Dont worry about underprovisioning and overprovisioning. Fargate reacts quicker to changes in traffic and allocates the right amount of conpute per pod. A traditional VM will reserve 4MB for graphics, containers don't usually have graphics, so this is a waste. Fargate is purpose-built for containers using microVMs. They are fast and lightweight and only have devices they actually need. A microVM requires only 5MB of overhead in total. Each application can use a separate microVM instead of a separate EC2 instance. Originally, the Fargate data plane ran on every VM. The new control plane is designed to run directly on bare metal, making the microVMs faster to startup.

[Read more](https://firecracker-microvm.github.io) about Firecracker containerd.

### Lambda
Lambda runs on firecracker. Surprisingly, the most rapid adoption of serverless is happening in the enterprise. It's cheaper and easier.

#### Vanguard
They're a gobal assets manager, around $5.7 trillion in assets. They have industry best client satisfaction results. They had some concerns about public cloud security, so they went on a private cloud adventure. They couldn't compete with AWS and building a private cloud was going to be expensive. So they moved to the public cloud and selected AWS. Their applications were 40 million-ish lines of code, so we're talking Maggie De Block huge here. They started moving smaller workloads to the cloud and adopted Route53, AWS WAF and CloudFront. They became heavy users of S3 and EMR, also other fancy ML stuff. More security services were introduced like Shield, Macy and SSM. They introduces DynamoDB and Aurora for storage and Kinesis datastreams. The next design decision was moving to ECS and Fargate, the reached stronger container isolation with integration with IAM. This accelerates the decomposition of the monolith. So here is the end state, about a 100% cloud native architectue. This enabled faster deployments, improved resiliency and lower costs.

## Evolvable architecture
"At AWS, we always think about evolvable architecture." The software you are building now might not be the software you're running a year from now. There's no better example than S3. S3 started out as 8 microservices, now there are 262 microservices. Including S3 access points, S3 access analyzer and more. Everything fails all the time, network controllers do weird things, bitflips are just straight up stupid. At AWS, people are always thinking about reducing impact on customers, this is called *blast radius reduction*.
### Cell based architectures
A cell based version of a multi-AZ application would be divided into multiple cells to reduce blast radius. This is zonal based architecture. EBS is a very good example, EBS is made up of multiple replicated shards that make up the block store. To control failure, the configuration master which is on a second network, rewires the set of shards when anything fails. If multiple things fail at the same time, this thing can get overloaded fast. In a world where you have partitions, you cannot have consistency and availability. To ensure both things in EBS, cell-based architectures were introduced. By splitting the architecture in zones and then splitting the zones, you reduce the blast radius. Instead of splitting EBS in a couple of zones, they splitted EBS in millions of small units to minimize the blast radius. This creates a colony of cells, inside a cell there's 7 nodes. A cell has a dedicated master. At AWS, this called project [Physalia](https://en.wikipedia.org/wiki/Portuguese_man_o%27_war), this also moves nodes as close as possible to the clients. Introducing Physalia reduced the error rate spectacularly.
#### Shuffle sharding
You have a number of nodes and randomly spread them over different shards. When a client fails, not all nodes in a shard are effected.
> The magic of math. - Werner Vogels, 2019

## Building distributed systems is hard
Amazon has been doing this the last 25 years on a scale that is unmatched. How does Amazon do this? Introducing the [Amazon Builders' Library ](https://aws.amazon.com/builders-library) **NEW**, you can now find out how Amazon had been inventing and building systems in the past and present.

![Amazon builders library](/images/posts/keynote-with-werner-vogels/library.jpg)

#### Saildrone
Ocean data is scarce, because everyone is scared to gather the data. The sea is scary 👻. *Rob took a break from typing for a second*

[Find out more](https://www.saildrone.com/) about Saildrone.

## Industry evolution
1.0: Steam machines
2.0: Electrity
3.0: Electronics started to arrive
4.0: Automation start taking place. Especially things like logistics. Are we really in industry 4.0? Factory equipment is way too old, they don't gather enough information to gain insights. The data needs to start flowing out of manufactoring sites into places where you can do analytics.

When Amazon started with selling books, logistics was easy. When they started selling TVs, books, pillows and coffee, things got alot harder. Computer vision is used to identify items and robots drive the correct products to people putting them into boxes. Machine learning is at the basis of all of this. This also powers major innovations like Alexa and Amazon Go stores. Lots of things in the physical world are powered by AWS, Woodside for example. They do very complicated things, that even startled Werner a little. Woodside started producing useful data instead of just using alarms that tell you when something stopped working. They are now using autonomous platforms that only use robots. These innovations can remove humans from very dangerous plants. Another example is Modjoul, they make smart wearables like safety belts to meaure if their workers are using the right techniques and improve worker health.

## Making our cities smarter
ShotSpotter are registring gun usage in environments to identify gun shots within 60 seconds and notify law enforcements. Since then, gun homocides have reduced drastically. Miovision put sensors on the streets to optimize transportation. The climate corporation built something like 'Climate field view' to help farmers optimize field usage. Farmers are sharing information anonymously about their crop fielding so prices for their sold crops are accurate.

## Modernizing transportation
Deutsche Bahn are accurately measuring delays on the German train tracks.

### Volkswagen
They produce 44.000 vehicles every day, that's a lot. They make over 200 million components and parts every day. Alright, alright, they're a big company, we get it. With AWS, they've lifted 200-ish factories into the cloud. This is what they call *The Volkswagen Industrial Cloud*, probably the biggest industrial cloud at the moment. The digital production platform controls the robots, the logistics, the assembly and more. Security controls, IoT and ML power this massive piece of beauty. Algorithms for predictive maintenance is only one feature of the thing. This lead to cost reduction, faster product release and something else, but my fingers are getting tired.

## Solving hard, human problems
Wether it's about education, health or anything else. A lot of young companies want to solve these problems. Aquabyte is a Norwegian company that focuses on producing protein. A common problem in Indonesia is that alot of farmers have no identity. This causes them to get ripped off when buying seeds. With AWS, farmers are given an identity, now banks are eager to give out loans because repay rate is almoest 100%. Have a look at the [Now Go build video series](https://aws.amazon.com/startups/NowGoBuild/).

> Wait, what? - Rob, end of keynote

> 2018 brought us serverless, 2019 left us speechless. - Kenneth, end of keynote

*I hope you had a nice read, because we were left empty-handed.*
