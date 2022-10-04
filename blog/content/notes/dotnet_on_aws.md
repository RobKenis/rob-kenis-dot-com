---
title: "Dotnet_on_aws"
date: 2022-10-03T15:31:15+02:00
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


How did serverless come into the picture? Around 2016, the 'serverless'
term started as a buzzword. 'AWS Lambda' came a little before that. In 2014, Werner
Vogels was not talking about Serverless when Lambda was released. It was an
'event-driven computing service'.

At the same time, the 'Reactive Manifesto' was written. https://www.reactivemanifesto.org/
Responsive means that: when your application is going to fail, you can give a fast
response to the end user. This makes your application resilient, meaning that it can 
adapt to a broken state. Reactive applications are elastic, meaning that they can 
scale up and down, based on the load. This can be achieved by using async communication.

Robke had animations, very nice :).

Downsides of synchronous communication: when a service needs to do 3 sync things, it
needs to orchestrate those 3 things. When 1 of the dependents has a breaking change, the
orchestration service needs code changes to make ends meet. What happens when one of the
services cannot return an OK response? Who has responsibility to go back to the happy flow?

Event Driven Architecture:

- What is an event? A state change that has happened in the past, cannot be changed anymore.
- Focus on communication. When an event has happened, subscribe to the event updates when you need to act upon an event.

Signature Lambda Handler:

- Event. Specific for each integration
- Context. Runtime information

How to invoke:

- Sync: request-response, errors are handled by the client
- Async: event based, errors get 2 retries and go to the DLQ (or Lambda Destinations) when they keep failing
- Poll: SQS for example. When a message on SQS is failing, how is this handled?

Cold starts:

When a Lambda is started, these steps need to happen: 
- Download code (cold start)
- Start execution environment (cold start)
- Execute initialization code
- Execute handler code

Cold starts are slow, so people started writing 'lambda handlers' to ping your lambda
function on an interval to keep the environment running.
This works, but it's not perfect. Lambdas are multi-AZ, so you can ping your Lambda all
you want, but this doesn't guarantee that you ping the proper AZ all the times.
We can solve warm Lambdas properly by configuring Provisioned Concurrency. By setting this,
AWS will keep the right lambda warm in the right AZ.

! When you break something in a Lambda invocation, which breaks your constructor, your Lambda will fail all the time. **Look into this**

### Data storage for Serverless

Relational databases were invented in the 70s, storage was expensive to make sure you don't
have a big footprint. Normalization was created to reduce the amount of storage needed.
For transactional processing, we have better solutions.

With the rise of the cloud, we had harder requirements for applications. Higher performance,
better scaling, more reliability. CPU performance is flattening and storage is getting cheaper,
database designers are making use of this.

DynamoDB is the NoSQL variant on AWS. Single milli-digit second response time, it's built
for scalability. You have to configure read/write capacity units and AWS will make sure it scales.

Data is stored in partitions. An item is stored in a partition, the item next to it can be
stored on another partition. This enables horizontal scaling, but you can have maximum throughput 
on a single partition. Items are fetched by making use of the Partition Key. When passing the Sort
Key, you know where to look in the partition for your data.
Use high-cardinality attributes for the partition key, this makes sure the items are spread
across the partitions.

- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html
- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SecondaryIndexes.html

When you know the access patterns, you can optimize your secondary indexes so you don't have to scan all the time. **Scans are bad.**

Single table design in DynamoDB:

- Joins are expensive. You have to scan the left table, the right table and then combine. That's why AWS did not add joins.
- It's cheaper and easier to back up.
- The downside is that it's not flexible.

Partition Key overloading:

- Give a generic name to your PK and SK attributes. Prefix the value with the thing your going to store: `CUSTOMER-001` and `ORDER-69`
- One-to-many relations are hard to manage, because how would you even put this in a queryable field?
  - When the data is not changing often, just put it in multiple records
- https://www.dynamodbbook.com/

Amazon Cognito:

- Not related, but when you set swagger UI to use Bearer tokens, you can click the login button in the UI and it will open the Cognito login form.

API Gateway:

- With direct integrations, you can skip Lambda entirely to put data from point A (HTTP request) to point B (SQS).