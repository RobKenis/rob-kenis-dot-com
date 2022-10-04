---
title: "Step Functions Advanced Design Patterns"
date: 2022-10-03T12:25:36+02:00
type: "post"
image: "images/masonary-post/post-2.jpg"
draft: true
tags: aws-community-days-2022
---

## Overview

https://www.awsgeek.com/AWS-History/

AWS Simple Workflow was released in 2012, one month after DynamoDB.
It was built on workers on EC2, because serverless didn not exist.
In 2014, Lambda was released.

In 2016, Step Functions was released at Re:Invent. Because Step 
Functions, there was no way to orchestrate Lambda. When you wanted
to build things in parallel or sequential steps, good luck.

In 2017, CloudFormation support was added. Within the year, impressive
stuff :). 

In 2018, integration with ECS (and Fargate), DynamoDB/SNS/SQS 
was introduced.

In 2019, local development and debugging was introduced.
https://hub.docker.com/r/amazon/aws-stepfunctions-local, one of the
foundations of LocalStack.
Integration with CloudWatch Events (EventBridge) was introduced.
A little bit later, callback patterns were introduced. Pass the callback
token to SQS, handle something async, pass the token back and
continue the workflow. This is 1000x better than waiting in the step
function itself.
In the summer, Nested Workflows were introduced, this made reusing
steps easier.
In October, Sagemaker integration was introduced, this marks the start
of MLOps. You can put all the steps of your machine learning pipeline
in Step Functions.
Re:Invent 2019 introduced https://aws.amazon.com/emr/ integration, to
reduce costs instead of running your EMR cluster 24/7. Also, express
workflows are added. They're a lot faster and cheaper, it's comparable
to inline Lambda. https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html

(!) In 2019, Lambda Destinations were added, this removed some of the
need for Step Functions. If you just need sequential Lambdas, just use
destinations.

In 2020, CodeBuild support was added. This looks dope, but I wasn't 
paying attention. Also AWS SAM integration was added. X-Ray support!
https://aws.amazon.com/blogs/opensource/migrating-x-ray-tracing-to-aws-distro-for-opentelemetry/

At Re:Invent 2020, EKS integration was added, this looks weird tho :shrug:

In 2021, FOCKING YAML SUPPORT BROTHAS, NO MORE JSON. Also, EventBridge 
support, but I don't know the difference with CloudWatch Events.
In the summer, Workflow Studio came out, basically drag and drop for
Step Functions.

In 2022, we now have local mocking support. No idea what it does yet,
but seems nice for testing. There's an Amazon Workshop: https://aws.amazon.com/about-aws/whats-new/2022/06/aws-step-functions-interactive-workshop-building-deploying-application-workflows/
There's also intrinsic functions now, seems nice when you have some simple
logic and you don't want to call a Lambda. No idea about testing.
https://aws.amazon.com/about-aws/whats-new/2022/09/aws-controllers-kubernetes-ack-rds-lambda-step-functions-prometheus-kms/
when you want to close the gap between AWS and K8S.

Functionless is a CDK extension. It will infer the underlying
type, so you don't need to know about State Language, Velocity templates,
Event Bridge Patterns. https://functionless.org/