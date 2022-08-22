---
title: 'AWS pre:Invent 2019'
image: images/posts/aws-preinvent-2019/index.jpg
date: 2019-12-01T11:45:00+01:00
tags: aws-reinvent-2019
type: "post"
---

The wait is over, re:Invent is around the corner. Just like me, most AWS teams cannot contain their excitement and have started releasing new features. This week leading up to re:Invent, also known as *AWS pre:Invent*, is all about the new features that didn't make the keynote. This doesn't mean they're not worth mentioning, so let's run over our top 5 of most heartwarming new features.

## Top 5 new features
1. [AWS Lambda destinations](#AWS-Lambda-destinations)
2. [Java 11](#Java-11)
3. [Cloudwatch ServiceLens](#Cloudwatch-ServiceLens)
4. [Amazon CDK now available for Java and C#](#Amazon-CDK-now-available-for-Java-and-C#)
5. [Cloudwatch Synthetics](#Cloudwatch-Synthetics)

### AWS Lambda destinations
So you've been writing reusable code for a while now. Or so you thought. To send your response to a consumer (e.g. SQS), you still had to write code to deliver the message specifically to that consumer. To mitigate this problem, AWS introduced [Lambda destinations](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-destinations-for-asynchronous-invocations/), a solution to send a lambda result to a consumer without writing application code. These consumers include: Lambda, SNS, SQS standard queue and EventBridge. Besides decoupling a part of your infrastructure, Lambda Destinations are supported in [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html() right from the start. *(At the time of writing, DestinationConfig was not yet added to the CloudFormation documentation).*

[Read more](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-destinations/) about Lambda destinations.

### Java 11
With the release of Java 13 last september, it hit me that the bigger part of my production code is written in Java 8. This isn't a bad thing, since Java 8 still has a couple years of support, but it got me thinking about why it was still so far behind. One of the major reasons was the lack of Java 11 support for [Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/). For lambda, this was not a problem, as my production lambdas are written in either Nodejs or Python. Well, AWS fixed both "problems" at once with the [release of Java 11 support for Beanstalk](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-elastic-beanstalk-launches-public-beta-corretto-al2-platforms/) and [Java 11 support for Lambda](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-java-11/). So go ahead and start writing those fancy Java 11 applications!

### Cloudwatch ServiceLens
AWS provides a couple ways to monitor your application, wether it's for logging purposes or application monitoring through [AWS X-Ray](https://aws.amazon.com/xray/). [Cloudwatch ServiceLens](https://aws.amazon.com/about-aws/whats-new/2019/11/announcing-amazon-cloudwatch-servicelens/) ties these functionalities together to give you a complete overview of your application. Gain insights in your infrastructure health using metrics and logs, and utilize transaction monitoring to get an overview of multiple resources for a deeper dive into your application health.

### Amazon CDK now availble for Java and C#
AWS CloudFormation, one of the most glorious things Amazon has to offer, can be a burden sometimes. Writing your configuration in YAML or JSON can become a giant file that will become hard to read after a while. Some frameworks, like [Troposphere](https://github.com/cloudtools/troposphere) and [Serverless Framework](https://serverless.com/), are doing a great job at relieving the pain and make resource configuration fun again. So last re:Invent, AWS came up with their own framework, the [Cloud Development Kit](https://aws.amazon.com/cdk/). A tool for Python or Typescript to help with resource configuration and make the world a better place, who could ask for more? So the Java and C# developers united and asked for more; And AWS delivered, introducing Java and C# support for the CDK.

[Read more](https://aws.amazon.com/blogs/aws/aws-cloud-development-kit-cdk-java-and-net-are-now-generally-available/) about CDK for Java and C#.

### Cloudwatch Synthetics
Discover issues before your users do, wouldn't that be amazing? AWS promises to bring you one step closer to Utopia with [Cloudwatch Synthetics](https://aws.amazon.com/about-aws/whats-new/2019/11/introducing-amazon-cloudwatch-synthetics-preview/). Cloudwatch Synthetics runs tests on your application endpoints every minute, alerting you when endpoints don't behave as expected. These tests, also called tasks, can consist of a couple flows, from latency testing to complex flows in your application. Endpoints can range from your REST endpoints to website content, to cover most of your workload before your customers get the chance to break it.

---
### Honorable mentions
- [SAM CLI simplified deployments](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-sam-cli-simplifies-deploying-serverless-applications-with-single-command-deploy/)
- [Elatic Beantstalk support for Spot Instances](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-elastic-beanstalk-adds-support-for-amazon-ec2-spot-instances/)
- [Lambda parallelization for event sources](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-parallelization-factor-for-kinesis-and-dynamodb-event-sources/)
- [Cost categories](https://aws.amazon.com/about-aws/whats-new/2019/11/introducing-aws-cost-categories/)
- [Lambda failure-handling for event sources](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-lambda-supports-failure-handling-features-for-kinesis-and-dynamodb-event-sources/)
- [CodeBuild test reporting](https://aws.amazon.com/about-aws/whats-new/2019/11/aws-codebuild-adds-support-for-test-reporting/)
