---
title: Real World ML lifecycle with Amazon SageMaker
image: images/posts/real-world-ml-lifecycle-with-sagemaker/index.jpg
date: 2019-12-04T11:15:31+01:00
tags: aws-reinvent-2019
type: "post"
draft: true
---

In Amazon warehouses, it's all about robotics. More than 200.000 robots are part of the workflow to get the massive variety of products to the customer. The constantly improve the movement and timings of these robots, a couple of very smart people have used machine learning to define their behaviour.

## ML Lifecycle
### Feature selection
It all starts with the selection of features, the input parameters that you define your model upon. In case of Amazon, the features consist of product size and weight, placement of the product in the rack and many more. Once you've selected the features, it's time to start gathering samples. Collect as much data as you can about the input you've defined and the outcome they produce.

People were asking very difficult questions that were not related to the problem, which was a big problem in itself.

### Sample collection
I was very excited to work with Kinesis firehose, because I'm not rich enough to use it in my personal account. I learned that when creating an S3 bucket, there's a **create** button on the bottom left corner, this is what re:Invent is all about folks! At the moment, you have to use a Lambda to 'subscribe' Kineses to SNS, but my new buddy at AWS is going to upvote it on roadmaps to add Kinesis to the list of direct SNS subscriptions.

### Model training
After you've gone wild and collected all the information you can get, you're ready to start training your model. *This is the part where the people without ML knowledge, like me, got completely lost.*

Some people don't read comments and then fail horribly, like me.
{% asset_img hyperparameters.png "Always read the documentation" %}

### Live inference
Once you've trained your model using Jupyter Notebooks in SageMaker, just deploy it from the SageMaker console. This may take a while, but after waiting for a couple of minutes, you can start using the model to predict outcome of new data, this is also known as inference.

### Automated retraining
You can do automated training based on a CloudWatch alarm that triggers a lambda that triggers retraining.

## Conclusion
At the end of the session, a leaderboard was created to rank all the best models. I'm very proud that I made the top 50, Kenneth was only a couple places before me. This is due to the fact that he had some idea of what he was doing and he is better at reading documention.

{% asset_img leaderboard.jpg "Leaderboard of best models with SageMaker" %}

*Instructions for this workshop are here: https://github.com/mike-calder/AIM368-Instructions*
