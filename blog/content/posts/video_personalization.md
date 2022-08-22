---
title: Video Personalization
image: images/posts/video-personalization/index.jpg
date: 2019-12-04T09:43:45+01:00
tags: aws-reinvent-2019
type: "post"
draft: true
---

In today's world, you can't browse anything without getting recommendations. Find a nice pair of shoes: recommendations. Watch a nice movie: recommendations. A recommendation engine is an informatiom filtering system that limits the amount and sort of content to the users likings. It's about tailoring a service for specific individuals rather than giving everyone the same, large amount of content.

## Types of recommendation / personalization
- Homepage video recommendations (featured)
- Genre/category (top x movies)
- Item-to-item similarities (if you like this, you'll like that)
- Personal re-ranking (search, genre)
- Layout customization (order of carousel)

## How to train the model
Gather incoming data from input sources like Kafka or Kinesis. Gather the explicit feedback like thumbs up or down, amount of stars. The downside to this is that very few people actually rate the content they watch. Or they rate on the extremes if they for example rate a movie one star because Niels Destadsbader is starring in it. It's also hard to calibrate, one person's 5 stars can ben another person's 4 stars.
### Implicit feedback
Implicit feedback is derived from actions taken by the user like clicking or watching content, subscribing to content. It's a lot of data which is good. The downside is that there's no direct negative feedback, you don't know if the user liked the content. Leaving the content early might be interpreted as negative feedback, on the other hand, it might not be negative.

## AWS Services for content recommendation
- [AWS Personalize](https://aws.amazon.com/personalize/)
- [Amazon SageMaker](https://aws.amazon.com/sagemaker/)
- EMR, EC2, but these seem like a lot of work compared to Personalize

## Common approacheas for engines
### Content-based filtering
Generate recommendation based on *known* user preferences. This is great for media because the genres and categories are well defined. The upside is a fast *cold start* for new items, you don't need to know a lot about the new content. It's very clear where the recommendation came from. The downside is that the user will get nothing exciting, the user will get what they already like. The users do get a cold start, they have to explictly tell you what they like.

### Collaborative filtering
Based on item-item or user-user relations. Recommendations are based on other experiences, but based on the amount of content and users, this can be a very hard process to calculate recommendations. For example, if Rob and Kenneth like 5 same movies, Rob can get a recommendation about one of Kenneth's preferred movies. This does come will a cold start, users have to interact with eachother before you can recommend things. Plus it is harder to find out why some recommendation is given compared to content-based filtering.

> There is no *right* way to do a recommendation engine.

### Matrix factorization
This started with a matrix computation I did not understand 😞. SageMaker does have algorithms to do this. All you do with factorization machines, is fill out the matrix, but with a high amount of users, this becomes expensive. The Jupyter notebook looked impressive, I didn't understand it sadly.

## Deep learning recommendation engines
{% asset_img engines.jpg "Deep learning recommendation engines" %}

The advantage is that complex interactions can be modeled, which makes it way more flexible. The downside is that is requires more data and is more complex to implement. Oh, and it's computationally expensive, wonderful. You lose a bit of insights in the recommendations, it's harder to tell why something was recommended.

## Modeling for personalization
Recommend the same shoes for 2 days after you've visited Zalando for 5 minutes. Sequence of events matter, if I search for a new laptop in the afternoon, the recommendation should change. This can be achieved with neural networks and sequential modeling.

## Amazon Prime Video
### Define the customer problem
How would you optimize the layout of a video store to maximize customer engagement? Some customers know exactly what they want, some know somewhat what the want like a genre, and some have no idea what they want. For the first, just give them what they want, for the second, give them something in a certain genre. For the last group, just let them browse. Having an online movie store is easier than a physical one. Moving shelves is no issue, the store can be different for each customer and you can better predict what the customer wants. In an actual store, you only show your membership card at checkout. On the otherhand, your online vendor already knows you before you even know yourself.
### Measure success
We want the customer to come back, a great way to achieve that is A/B testing.
### Getting started
Keep it simple, deliver value quickly so it stays easy to improve and debug. The algorithms to achieve this are content-based filtering and collaborative filtering.
#### Results
| What worked                    | What didn't work                      |
| ------------------------------ |:-------------------------------------:|
| Easy to debug                  | Recommendation felt *static*          |
| Recommendations were OK        | Groups of people got the same content |
| Customer engagement increased  | Low quality of long-tail metadata     |

### Collaborative filtering
| What worked                           | What didn't work                             |
| ------------------------------------- |:--------------------------------------------:|
| Recommendations were more appropriate | Same titles were recommended again and again |
|                                       | Did not respond changes in taste             |

### Next steps
Assumptions don't scale, what is true in the US doesn't have to be true in Germany. Deep neural networks can improve the constant updating of assumptions.
#### Results
| What worked                                                                                               | What didn't work                 |
| --------------------------------------------------------------------------------------------------------- |:--------------------------------:|
| Recommendation were better because preferences got updated quicker and more broad content was recommended | Some titles felt *out of place*  |

Pro tip: Build extra guardrails and business logic to make sure you don't lose customer trust by recommending very wromg content like a horror show to a kids account.
