---
title: "Pretty URLs with CloudFront Functions"
date: 2021-11-18T19:00:00+01:00
description: "Enable Hugo pretty URLs with AWS CloudFront Functions"
type: "post"
image: "images/posts/hugo_pretty_urls_on_aws.jpg"
---

There's nothing as pleasing as sending a clean URL to a friend or a colleague. No complicated path, no
extensions, just a plain and simple URL. As I explained in [this post]({{< ref "/posts/hosting_your_blog_on_aws" >}} "Hosting your blog on AWS"), I hosted my statically linked website
on AWS S3. This is great for cost savings and low maintenance, but it comes with a trade-off.

When hosting websites on S3, you can configure your *index page* and your *error page*. When you configure 
`index.html` as your index page, `https://robkenis.com/` will lead to `https://robkenis.com/index.html`. 
Wonderful, your single-page application works without further configuration. But what about `https://robkenis.com/posts/hosting_your_blog_on_aws/` …there is no option to configure an index page
for that path straight from S3.

The work-around I used in the initial setup, was enabling *ugly URLs* in Hugo. This would export the post as
`/posts/hosting_your_blog_on_aws.html` and create the links to the post accordingly. Although my site worked,
I was unhappy with the need for extensions in my URLs.

### AWS Lambda to the rescue

There is another way to manipulate the URLs, a way in which the user won't even notice. Why don't we 
intercept the request before it reaches S3 and append `/index.html` to all URLs that need it? This would 
mean clean URLs for the user that point to actual files in S3. 

Obviously I wasn't the first one to come up with this solution. Years ago, AWS introduced 
[Lambda @ Edge](https://aws.amazon.com/lambda/edge), a solution that enables you to execute serverless
functions directly from your CloudFront Distribution. So no servers to maintain, you only need to write a 
Lambda function and configure CloudFront to call it when a request is received.

Great solution, but can be improved on!

### Introducing CloudFront Functions

And here we are, a couple of months after Lambda @ Edge was possible, the process to execute functions at the
edge was made simpler. Back in May 2021, AWS introduced [CloudFront Functions](https://aws.amazon.com/blogs/aws/introducing-cloudfront-functions-run-your-code-at-the-edge-with-low-latency-at-any-scale/), a
solution that provides the option to write small, fast functions that execute when a user arrives at your CDN.

#### Creating a function

For those who have written a Lambda before, the next part will seem familiar. Your function has a handler
method, which takes an event as input. The same applies to CloudFront Functions. I'll explain further with
the code I used to make pretty URLs possible for my own website.

```js
function handler(event) {
    var request = event.request;
    var uri = request.uri;
    if (uri.endsWith('/')) {
        request.uri += 'index.html';
    }
    else if (!uri.includes('.')) {
        request.uri += '/index.html';
    }
    return request;
}
```

When an event of type [CloudFrontRequest](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/types/aws-lambda/common/cloudfront.d.ts#L44) is received,
the URI is takes from the input. When the URI ends with a `/` or has no extension, `/index.html` is added
to the URI, so it points to the correct file in S3.

Now we have our logic inside a Lambda function. All that is left, is attaching it to our CloudFront. In the 
same fashion as the previous post, I'll share the CloudFormation snippet below. The following CloudFormation
resource will create a CloudFront Function. For now the only runtime available is `cloudfront-js-1.0`. To me,
this looks like very old JavaScript, so no *const* and *let* yet. To view your function, head over
to the CloudFront console and find 'CloudFront Functions' in the menu on the left side.

```yaml
Resources:
  PrettyURLs:
    Properties:
      AutoPublish: true
      FunctionCode: |
        function handler(event) {
            var request = event.request;
            var uri = request.uri;
            if (uri.endsWith('/')) {
                request.uri += 'index.html';
            }
            else if (!uri.includes('.')) {
                request.uri += '/index.html';
            }
            return request;
        }
      FunctionConfig:
        Comment: Enable pretty URLs for Hugo
        Runtime: cloudfront-js-1.0
      Name: !Join
        - '-'
        - - !Ref 'AWS::StackName'
          - rewrite-pretty-urls
    Type: AWS::CloudFront::Function
```

This will only create the CloudFront Function, but without configuring it, it will never be called. To attach
it to a Distribution, we must configure it like any Lambda @ Edge function. We must pick an `EventType`, and
this is where CloudFront Functions are limited. Out of the 4 options, we can only pick `viewer-request`
and `viewer-response`, so no modifying the request between the Distribution and the Origin during the 
`origin-request` and `origin-response` events. Next to the EventType, we must pass the reference to our
CloudFront Function using the ARN.

```yaml
Resources:
  CloudFront:
    Properties:
      DistributionConfig:
        ...
        DefaultCacheBehaviour:
          ...
          FunctionAssociations:
          - EventType: viewer-request
            FunctionARN: !GetAtt 'PrettyURLs.FunctionARN'
```

After attaching the Function to the Distribution, you're all set. When a user requests a page at
`https://robkenis.com/posts/whatever-post-comes-next/`, `index.html` will be added so the user is served
the correct page straight from S3, without managing any servers or adding noticeable costs.
