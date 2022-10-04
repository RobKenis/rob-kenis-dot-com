---
title: "DevOps Guru for Serverless Applications"
date: 2022-10-03T14:31:58+02:00
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

https://aws.amazon.com/devops-guru/

DevOps Guru detects behavior that deviates from the normal operating
patterns.

- Detect operational issues
- Reduce noise from alarms

### How does it work?

CloudWatch, CloudTrail and X-Ray as data sources for the baseline. 

When an incident happens, it aggregates metrics and monitoring, e.g. Lambda errors
correlated with a throttled DynamoDB. Also events are correlated that can impact the
healthiness of the application, e.g. deployments and infrastructure changes.

### The demo

https://github.com/Vadym79/DevOpsGuruWorkshopDemo

I don't even know what's going on

### How to set it up?

https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html

When your resources are in a CloudFormation stack or are tagged, you can use them in 
a resource collection.

Look up alerting. When a medium alert is fired, it seems to take a very long time
for users to get notified. `ProvisionedConcurrencySpilloverInvocations` https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html

### Conclusions

- Errors have been correctly identified. It takes at least 7 minutes to create an incident.
- No incidents created for temporary events, e.g. API Gateway throttling.
- Recommendations could be more precise, not concrete enough when it concerns service/account limits.
- When handling 4xx errors, it takes a long time and API/Lambda is not correlated so manual work required.
- Lambda anomaly insights takes too long, 30 minutes to detect.
- Proactive insights keep analysing after incident occurred once.
- Missing link between log groups and X-Ray tracing.