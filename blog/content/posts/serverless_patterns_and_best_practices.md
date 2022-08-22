---
title: Serverless patterns and best practices
image: "images/posts/serverless-patterns-and-best-practices/index.jpg"
date: 2019-12-03T11:49:50+01:00
tags: aws-reinvent-2019
type: "post"
---

## Operational responsibility model
Not everything will be serverless, most of the time, it will be mix and match. 'Create a serverless application' from the console became easy as 🥧.
Read more about getting started with serverless [here](https://aws.amazon.com/quickstart/architecture/serverless-cicd-for-enterprise/), [here](https://www.jeremydaly.com/serverless-microservice-patterns-for-aws/) and [here](https://github.com/alexcasalboni/aws-Lambda-power-tuning).

## Performance test
Decide wether you need a regional or and edge-optimized endpoint in API Gateway. By removing the CDN in regional gateway, you skip an unnecessary hop and your gateway gets much faster *duh*. Tweak your memory limits in Lambda. Using Java in Lambda doesn't mean you need to use all the RAM in the world plus a little extra.

## Patterns
### Comfortable "REST"
Enable access logs, structure logs and instrument your code. Use Cloudwatch async metrics Embedded Metrics Format **NEW**. Annotate your code to enable tracing. Regulate inbound access rate, enable throttling by default. Manage Secrets with SSM, and authorize your consumers.
Cost effectiveness:
- Regional endpoints for API Gateway, especially if you don't need the CDN
- Use on-demand scaling for DynamoDB. If huge capacity is known beforehand, obviously enable provisioned throughput
- Optimize CPU and memory for Lambda. Beyond 1.7GB memory, Lambda gets 2 CPUs

### The "Cherry-pick"
Use AppSync. Enable caching **NEW**. In GraphQL, caching is hard because the client picks what they want. With new AppSync caching, data can be cached at the resolver level or at the data level. Use Lambda for complex logic but not for just connecting point A to point B. Use state machines for long transactionsm Pipeline resolvers for simpler transactions. Authorize at data level and use the database build for the purpose.

### Call me, "Maybe"
The famous webhook, call something when something happens. Limit Lambda concurrency to avoid depleting the connection pool to relational databases. Lambda scales way quicker than RDS. Use kinesis as a buffer. Use Lambda destinations for failed requests **NEW**. *If I have X retries, send the message to a destination.* Obfuscate sensitive data on the stream. Kinesis can batch records for up to 5 minutes, very nice for low-volume traffic. You can integrate API Gateway with pretty much any service, you don't need a Lambda.

### The big "Fan"
Use fanout to leverage multiple consumers for pretty fast processing. Verify signature of SNS messages to make sure the message effectively came from SNS. Default SNS broadcasts messages to all consumers. Use messages filtering by consuming only messages with a certain message attribute. Compress and aggregate messages when possible. Consider *KINESIS* if possible for larger payloads.

### They say "I'm a streamer"
Enable source stream record backup for kinesis firehose without invoking a Lambda. Favor dedicated Data Firehose per context. Obfuscate sensitive data. Use parquet transformation at stream level. Transform payload at stream level from [JSON](https://www.json.org/json-en.html) to [parquet](https://en.wikipedia.org/wiki/Parakeet) for example to be used with Athena. Use message filtering to prevent unwanted events.

[Learn more](https://aws.amazon.com/blogs/networking-and-content-delivery/global-data-ingestion-with-amazon-cloudfront-and-Lambdaedge/) about global data ingestion to Kinesis.

### The "Strangler"
Use an API to abstract implementation details, which makes it easier to move parts behind the API. Centralize logs, metrics and tracing. Enforce authorization on the top level of on-premise mainframes, most of the times this will be Active Directory. [Learn more](https://www.ad.nl/) about AD. Gradually shift functionalities to new compute and database platforms. Don't straight up move everything to Lambda, but gradually do this to avoid disruption.

##### Usefull resources
- https://github.com/aws-samples/aws-serverless-airline-booking
- https://github.com/awslabs/realworld-serverless-application
- https://github.com/awslabs/aws-Lambda-powertools
