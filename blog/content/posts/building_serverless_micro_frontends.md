---
title: Building serverless micro-frontends
image: images/posts/building-serverless-micro-frontends/index.jpg
date: 2019-12-05T06:08:49+01:00
tags: aws-reinvent-2019
type: "post"
draft: true
---

The idea behind micro-frontends is to think about a web app as a composition of features owned by independent teams. Each team has a specific area of business or mission it cares about and specializes in. A team is cross-functional and develops features end-to-end, from the database to the user interface.

Even though micro-frontends are a relatively new way of building frontend applications, many companies tried to embrace the principles behind them and have created multiple implementations for solving their frontend and organization challenges.

Micro-frontends appears to be technology-agnostic, and several different approaches are being taken:

- Iframes; where each frame has its own subdomain.
  Spotify uses micro-frontends in their desktop application leveraging iframes for stitching together different part of the same view. The communication between iframes is made via an event bus that decouples nicely the different part of the application allowing them to communicate without knowing who is going to listen for a message or event.
- Components.
  Online reservation service OpenTable goes this route, with the OpenComponents stack. Here, a registry houses all the components needed to build the application. “Each team can pick up the registry the components that they want,” he said.
- Server-side composition; where all the elements for a web application are assembled on the server.
  Fashion e-commerce site Zalando uses this approach, with the help of Project Mosaic, a framework of services, libraries, and a specification for how components should work together. One component, Tailor creates a tiny runtime layer for each page rendered, assembling each of the HTML fragments needed.

This session was about how you can use Lambda@Edge for your micro-frontends, so you can get the benefits of both server-side composition and the speed of the edge. Lambda@Edge provides you with the possibility to extend the behaviours of a request or response directly on the edge.
This paradigm, in conjunction with the serverless one, can provide a great flexibility in structuring our applications and it can prevent that too many requests hit our application servers executing operations directly on the edge like headers manipulation, access control, redirection rules and so on. In order to work with Lambda@Edge in AWS, you just need to set up a Cloudfront distribution in front of your infrastructure.

Lamba@Edge has several limitations that we need to be aware of before taking it in considerations. First of all, the Lambda@Edge has to be created in North Virginia only. You can associate only an exact version released with Cloudfront and not the $latest version. There are also some soft limits to take in consideration like maximum memory associated to our Lambda@Edge, concurrent executions, ...

When using DynamoDB in your Lambda@Edge, it is wise to use [DynamoDB Global Tables](https://aws.amazon.com/blogs/database/how-to-use-amazon-dynamodb-global-tables-to-power-multiregion-architectures/). By using Global Tables, your Lambda@Edge can request data from the same edge, which speeds it up significantly.

## DAZN
One of the speakers was the VP of Architecture at DAZN, a live and on-demand sports streaming service. He shared some of his experiences with micro-frontends.

DAZN follows Domain Driven Design practices for slicing their subdomains and make them really independent. Up to now, DDD was applied to the backend layer but not very often to the frontend as well, extending these concepts to the frontend allow us to easily identify our micro-frontends.

They're using 1 micro-frontend per page so they don’t have share dependencies between micro-frontends. For example, a request to `/account` is routed to a CloudFront (to get the caching benefits), which passes the request to a Lambda@Edge (when it's not cached or for personalization purposes). This means that each micro-frontend has its own CloudFront.

Micro-frontends are loaded and orchestrated by the "bootstrap", a simple JavaScript application embedded in the main HTML page that loads different micro-frontends based on deep-link requests, user status or any request coming from the loaded micro-frontend.

*I actually wanted to learn how people used multiple micro-frontends on the same page, so this was a bit of a bummer. The talk in itself was good though!*
