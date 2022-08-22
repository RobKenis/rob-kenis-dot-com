---
title: Customizing content delivery at the Edge
image: images/posts/customizing-content-at-the-edge/index.jpg
date: 2019-12-04T15:09:07+01:00
tags: aws-reinvent-2019
type: "post"
draft: true
---

<!-- Intercept request on viewer request and response and origin request and response.
Can be used to add headers, A/B testing and URL rewriting for example. Originless flows like redirecting. -->
When you want to serve your website on a global scale, you will eventually get complaints from clients because their response times are slow. This makes sense, since some clients will be further away from the region where your website is hosted. You can't bring your clients closer to your server, but you can move your computations closer to your clients. Leverage Lambda@Edge to run compute when clients hit your CloudFront edge.


## Security
In modern web, many security features are implemented and enforced by the web browsers. The client-side security features are usually enabled and configured by HTTP response headers sent by a web server. However, a web server may not include all of the desired security headers in responses sent to your clients.

We will add several response headers to enable web browsers security features. For example, the Strict-Transport-Security response header protects your viewers from certain categories of the man-in-the-middle attacks, and the Content-Security-Policy header helps prevent cross-site scripting (XSS), clickjacking, and other code injection attacks resulting from execution of malicious content in the trusted web page context. We will also configure the CloudFront distribution to always require HTTPS for communication between your viewers and CloudFront. All HTTP requests received by CloudFront will be redirected a corresponding HTTPS URL. Redirecting all requests to HTTP is a setting on CloudFront behaviours, no further action is required. To add extra security headers, intercept the request on the Origin-Response. Using Origing-Response has the advantage of being cacheable, compared to Viewer-Response. During the Lambda executiom, add the headers you want to the Response object.

You can use https://observatory.mozilla.org/ to validate if your site's security is configured correctly.
<!-- Lambda has a *Deploy to Lambda at edge* action, which is pretty handy. Lambda@Edge has support for Nodejs up until 10.x -->

## Content Generation
With Lambda@Edge, you go beyond modifying HTTP requests and response that CloudFront receives from and sends to your viewers or your origin. Using your Lambda@Edge functions, you can generate content on the fly closest to your viewers without even going to an origin by returning a response from a Lambda@Edge function triggered by viewer-request or origin-request events. By triggering lambda on origin-request, we can leave out the use of API Gateway and trigger a Lambda straight from CloudFront.

## Simple API
In order to make a simple website a little bit more interactive, let's accept some feedback from the viewers and reflect it in the dynamically generated pages. The downside of using Lambda@Edge instead of API Gateway is the manual checking for request method. You can add GET, PUT or POST to the behaviour; CloudFront doesn't care which method it receives. The upside is that the computation is executed as close as possible to the client, making sure response times are faster than you can imagine.

## Pretty URLs
Pretty URLs are easy to read and remember. They also help with search engine ranking and allow your viewers to use the descriptive links in social media.
There are two common ways to serve content with pretty URLs:
- Redirect from semantic URLs to the URLs accepted by the origin
- Rewrite semantic URLs to URLs accepted by the origin. This can be done either by the origin itself or by an intermediate proxy.

The URI rewrite approach has two advantages over the redirect:
- Faster content delivery as there is now need for an extra round-trip between the server and the client to handle the redirect
- The semantic URLs stay in the address bar of the web browser

```javascript
'use strict';

exports.handler = async (event) => {
    let request = event.Records[0].cf.request;

    const redirects = {
        '/r/music':    '/card/bcbd2481',
        '/r/tree':     '/card/da8398f4',
    };

    if (redirects[request.uri]) {
        // generate 302 redirect response
        return {
            status: '302',
            statusDescription: 'Found',
            headers: {
                'location': [{ value: redirects[request.uri] }]
            }
        };
    }
    return request;
};
```

## Customization
You can serve customized content from an S3 bucket by changing the path prefix depending on the CloudFront device type headers like:
- CloudFront-Is-Mobile-Viewer
- CloudFront-Is-Desktop-Viewer

```javascript
'use strict';

exports.handler = async (event) => {
    const request = event.Records[0].cf.request;

    if (request.headers['cloudfront-is-desktop-viewer'] &&
        request.headers['cloudfront-is-desktop-viewer'][0].value !== 'true') {

        // it's not a desktop (it's  mobile, tablet or tv), use the mobile css
        request.uri = request.uri.replace(new RegExp('^/css/'),'/css/mobile/');
    }
    return request;
};
```

<!-- ## Extra Challenges
Here is a few extra challanges for you if you feel up to it.

Why aliens that landed in, say, Japan are learning English? It would make sense for them to learn Japanese instead, perhaps using some authentic pictures and characters. With Lambda@Edge you can inspect CloudFront-Viewer-Country header and select a different S3 bucket (for example, in the ap-northeast-1 region) for CloudFront to fetch the images from using Content-Based Origin Selection feature. For more information, please refer to some public documentation:

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirecting-examples
https://aws.amazon.com/blogs/networking-and-content-delivery/dynamically-route-viewer-requests-to-any-origin-using-lambdaedge/

Consider using Amazon DynamoDB Global tables. In the previous labs, we implemented Lambda@Edge functions in a way that they access a DynamoDB table in a single region, thus, introducing extra latency. This can be improved if DynamoDB table is replicated to multiple regions closer to where your viewers are. For more information, please refer to some public documentation:

https://aws.amazon.com/dynamodb/global-tables/
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html

Sometimes, you may want to introduce a new change in your website to only a fraction of your viewers. You can do it with Lambda@Edge, for example, by rolling a dice and setting a cookie on the client side so that clients get consistent behavior, i.e. either variant A, or variant B, but not a mix of them.

https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-general-examples

Interested in exploring more use cases that Lambda@Edge supports? Check this out.

https://aws.amazon.com/blogs/networking-and-content-delivery/resizing-images-with-amazon-cloudfront-lambdaedge-aws-cdn-blog/
https://aws.amazon.com/blogs/networking-and-content-delivery/authorizationedge-how-to-use-lambdaedge-and-json-web-tokens-to-enhance-web-application-security/
https://aws.amazon.com/blogs/networking-and-content-delivery/category/networking-content-delivery/lambdaedge/ -->

## Extra options with Lambda@EDge
- [URL redirects](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirecting-examples)
- [Dynamic routing](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirecting-examples)
- [DynamoDB Global tables](https://aws.amazon.com/dynamodb/global-tables/), [developer docs](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [Dynamic image resizing](https://aws.amazon.com/blogs/networking-and-content-delivery/resizing-images-with-amazon-cloudfront-lambdaedge-aws-cdn-blog/)
