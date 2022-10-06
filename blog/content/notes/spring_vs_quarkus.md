# Spring vs Quarkus

Java architecture does not match well with the k8s native architecture:

- Scaling Java is through more memory, k8s through more instances.
- Java has behaviour for mutable systems, e.g dynamic module loading. k8s is immutable
- Java runs long and slow, but on k8s performance and footprint matters

How to fix:

- Efforts on JVM:
    - Container-aware jvm efforts, linux container and jvm can communicate about memory usage. This makes the jvm more
      efficient
    - better performance, project loom for better concurrency
    - compiled java, remove the jvm

Spring

Pro:

- documentation and community
- lots of features and mature, exists since 2002
- spring cloud and spring reactive are initiatives to move spring to the cloud

Cons:

- Lots of dependencies
- large memory footprint, high startup times

Quarkus

Pro:

- Developed with kubernetes native in mind
- fast boot times, low memory footprint
- enterprise standards like microprofile, jakarta EE and vertx
- dependencies are created with native compilation in mind

Quarkus application lifecycle

Spring does not do much at compile time, most of the things are created at runtime,
like creation of beans. Quarkus does most of the decisions at build time. Application
can start at an instant, this is faster, but harder to change things at runtime.

Cons:

- Native compilation is hard and slow
- Not as mature as Spring. Active development but smaller community.

- https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/