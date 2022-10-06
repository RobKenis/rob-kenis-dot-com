---
title: "Re:Factor 2022 Compiled"
date: 2022-10-06T20:14:49+02:00
description: "The things I learned at Re:Factor 2022"
type: "post"
image: "images/posts/refactor-2022/index.jpg"
---

At an Axxes event, expectations are always through the roof. With Re:Factor, this wasn't any different.
These are the things I learned at Re:Factor 2022.

Apart from delivering quality talks, Re:Factor worked together with [Tree Nation](https://tree-nation.com/) to put focus
on the reforestation about the world, more specific around the equator.

I mostly followed the Open Source and Infrastructure track, which was filled with talks about Kubernetes and
CI/CD. Other than that, I picked up some new things about Java, which might help me with running Java more
efficient in containerized environments.

I you want to know more about Re:Factor, visit https://www.re-factor.be/.

1. [Tekton in Practice](#tekton-in-practice)
2. [Spring vs Quarkus](#spring-vs-quarkus)
3. [Service Mesh](#service-mesh)

### Tekton in Practice

[Tekton](https://tekton.dev/) is an open source solution for running CI/CD pipelines on [Kubernetes](https://kubernetes.io/).
It enables you to build reusable workflows that scale with your cluster.

#### Tekton Components

Tekton uses the Kubernetes resource model to define 3 key parts of their ecosystem.

##### Task

A task is the smallest unit of a Tekton workflow. It defines which steps need to be executed in a given container.
A task gets scheduled in a Pod, which each step representing a Container within that Pod. A Task is available within
a namespace, to make the Task cluster-wide, create a ClusterTask, this one is reusable from other namespaces. A common
use case is a `git checkout` task.

Following Task definition represents a Tekton task which will build a project using [Maven](https://maven.apache.org/).
Parameters, inputs and outputs are omitted, but information can be found [here](https://tekton.dev/docs/pipelines/tasks/).

```yaml
apiVersion: tekton.dev/v1beta1
kind: Task
metadata:
  name: maven-build
spec:
  steps:
    - name: build
      image: ubuntu
      args: ["mvn", "package"]
```

##### Pipeline

A Pipeline is a collection of Tasks, the orchestration of these tasks is defined by the Pipeline.

Following Pipeline definition will first execute the `maven-build` Task defined above, followed by the `docker-build`
Task (which is not mentioned, but you get the idea). More information about composing Pipelines can be found [here](https://tekton.dev/docs/pipelines/pipelines/).

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: my-first-pipeline
spec:
  tasks:
    - name: build-the-jar
      taskRef:
        name: maven-build
    - name: build-the-container
      taskRef:
        name: docker-build
      runAfter:
        - build-the-jar
```

##### PipelineRun

A PipelineRun is an instantiation of a Pipeline resource. A Pipeline is a generic object with parameters for example
the Git repository to pull changes from. The PipelineRun resource creates a Pipeline with parameters filled in.

#### Tekton on a Container Platform

Tekton works well with GitOps tooling like [ArgoCD](https://argo-cd.readthedocs.io/en/stable/). When a container image
is built using Tekton, the latest step can update an environment repository, which is monitored by ArgoCD. When using
this approach, all configuration is managed through Git, which gives optimal visibility on changes in the environment.

#### Conclusion

Tekton seems like scalable solution when already running on Kubernetes. Instead of re-inventing the wheel with every
workflow, you can reuse Tasks and Pipelines, even exposing them to other teams with the use of ClusterTask and
ClusterPipeline.

### Spring vs Quarkus

[Java](https://www.java.com/en/) architecture does not match well with Kubernetes architecture. Scaling Java is done 
by assigning it more memory, thus scaling it vertically. Scaling on Kubernetes happens horizontally by running multiple
instances of the same application. On the topic of scaling, Kubernetes is built with the idea that an application is
immutable and ephemeral, something which does not apply necessarily to Java. Java applications can change at runtime,
modules are dynamically loaded, context can change. All of this is a horrible situation when working with Kubernetes.

So let's solve the issue. Over the years, Java has worked hard to run better on container platforms. Some improvements 
are better communication between the Linux container and the JVM, which optimizes the usage of resources and the introduction
of [Project Loom](https://openjdk.org/projects/loom/) and [GraalVM](https://www.graalvm.org/) to move optimizations
to compile time.

In practice, this is a little more complicated, no one in their right mind should change from a mature [Spring](https://spring.io/)
application to [Quarkus](https://quarkus.io/) without thinking this through. Spring has the advantage of being a mature
framework with wide adoption and great documentation. Quarkus is the new kid on the block, rapid development, but a 
smaller community.

But here are the major Quarkus advantages. It is developed with Kubernetes is mind, meaning a smaller memory footprint
and faster startup times. It respects enterprise standards like [MicroProfile](https://microprofile.io/), Jakarta EE
and [VertX](https://vertx.io/). Apart from using more modern solutions, Quarkus moves most of the heavy lifting to
compile time. With dependencies being created at compile time, you don't have to wait for that during application
startup. In comparison to other frameworks, Spring makes you wait during application startup while it's searching
for all possible beans to create.

Now to conclude, if it seems too good to be true, it probably is. There's also some downsides to this new way of compiling
Java. First of all, you'll have to wait a lot longer during compilation. Yeah nah, I don't have another disadvantage,
Quarkus seems dope.

### Service Mesh

Services Meshes are great when connecting applications in a distributed environment. The most adopted implementation is
the sidecar-proxy pattern. An application called a sidecar proxy, like [Envoy](https://www.envoyproxy.io/), will run
alongside your container and handle incoming and outgoing traffic. Configuration of the sidecar is handled by the control
plane. The control plane can have different flavors like [Consul](https://www.consul.io/), [Open Service Mesh](https://openservicemesh.io/)
and [Istio](https://istio.io/).

A service mesh uses [Layer 7](https://en.wikipedia.org/wiki/OSI_model#Layer_7:_Application_layer) routing, which gives
fine-grained control over the requests, for example by differentiating between `GET` and `POST` requests. By routing
on L7, we can load balance requests instead of load balancing a connection. When you want to do A/B testing, canary
deployments or route based on request headers, this is essential. This form or routing, called traffic shifting, can be
used by [Argo Rollouts](https://argoproj.github.io/argo-rollouts/) to do some cool stuff while performing rolling deploys.

Running a sidecar proxy also has some added benefits regarding observability. All incoming requests are logged, so you 
can collect your access logging by default. Logs are printed to stdout, so you can pick them up with for example
[Fluentbit](https://fluentbit.io/) and process them using [Loki](https://grafana.com/oss/loki/).
Tracing between applications can also be handled by using a Service Mesh. Tracing headers are injected in the request when
passing through a proxy and the headers are not set yet. The application is responsible for passing the request header
to its own requests, but other than that, it's hands-off. Tracing information is compatible with [Open Telemetry](https://opentelemetry.io/),
which looks super nice from an open standard perspective.
And last but not least, your Service Mesh can generate metrics for you regarding request count, latency, success rate
and everything you'd want to know about the traffic between applications.

On the topic of security, a Service Mesh basically handles 2 things for you: authentication through mutual TLS and
authorization through the usages of policies. Policies are fine-grained enough to give certain applications access
to specific request methods and paths, giving you the opportunity to full remove authentication from your application.
Not saying you should do this, because it sounds horrible from a security point of view, but you definitely could.

Honorable mentions are [Linkerd](https://linkerd.io/), which is built for speed and security and [Cilium](https://cilium.io/),
which is built on kernel level and requires less resources and is stupid fast.

### Honorable Mentions

- When creating a Machine Learning model, make sure (and I can't stress this enough) to use a complete set of training
data. AI can become incredibly racist when giving a training set of white people (read: the majority op people working
in IT).
- [Influx](https://www.influxdata.com/) seems like a nice timeseries database. With up to 3 million writes per second,
it seems ready for enterprise workloads.
- Lightweight Kubernetes is a great solution to run a home. [k3s](https://k3s.io/) with [minio](https://min.io/) running
on top makes a great self-hosted solution for Amazon S3.

> The honorable mentions were great talks and brought new insights, but I didn't take notes, so yeah.