---
title: "Hosting your blog on AWS"
date: 2021-11-16T18:00:00+01:00
description: "Get your static blog up and running with Hugo and AWS"
type: "post"
image: "images/posts/hosting_your_blog_on_aws.jpg"
---

Hosting my own space on the internet for the price of a pint of Stella. That was the requirement I set for myself,
bonus points if the solution was easy with zero maintenance.

After writing my first blog post back in 2019, I started thinking about creating a personal blog. Sounds great, a place
on the internet to write down my thoughts on various topics, so maybe one day someone else could find it useful.
As I didn't really think about user interaction, my requirements were limited: 
*Cheap, zero maintenance, everything in git*

As a software developer, the next step is easy. You pick an existing framework, write your first post and deploy your
site to the first hosting solution that comes to mind. Just kidding…you try writing everything from scratch. So I set
up an empty project with NextJS, added the required Markdown extensions to store my posts in git. And then the first 
problems started popping up, the Markdown was showing in a weird way, my CSS skills are far below par, and I noticed 
I was going on and adventure I never intended to be in. Time to rethink some steps and grab something off the shelf.

### Introducing Hugo

When I bootstrapped my first blog, I picked [Hexo](https://hexo.io/), it's an open source project, powered by NodeJS.
I had a quick look at it, and it ticked all my boxes: Markdown, statically generated pages and a ton of ready-to-use
themes. The statically generated pages will be important later on, so hang in there. Hexo worked great, 10/10 would 
recommend. The [blog](https://reinvent.robkenis.com/) is still up today with zero maintenance.

Now, 2 years later, I'm ready to start over with a blank project. I compared the classic options: Hugo, Jekyll and Hexo.
They all looked great, but it was the *Go* language that caught my eye. The 
[documentation](https://gohugo.io/getting-started/quick-start/) has a neat quick start guide which I followed. 

#### Setting up a new project

Setting up a new project is a rather simple process. First, install the CLI, then use the CLI to generate a blank
project.

```shell
$ brew install hugo
$ hugo new site quickstart
```

When the new project is created, a directory *quickstart* is created which contains a blank project. To keep this post
concise, I'll focus on building and deploying the site and cover customization in another part. Before starting the
server, we need to select a theme and create our first post. Add a theme by cloning an existing theme in the *themes*
directory. For my own blog, I picked [parsa-hugo](https://github.com/themefisher/parsa-hugo).

```shell
$ cd quickstart
$ git init
$ git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```

After cloning the theme, configure it in *config.toml*, the content should look somewhat like this.

```shell
baseURL = 'https://robkenis.com/'
languageCode = 'en-us'
title = 'Rob Kenis | Blog'
theme = "ananke"
```

Great! We have an empty, working project. Now it's time for a first post. With Hugo, you have the option to define
templates for posts in *archetypes*. An archetype for a post is already defined, use it with the following command.

```shell
$ hugo new posts/my-first-post.md
```

After generating the first post and writing some stuff down in the newly created Markdown file, it's finally time
to start Hugo. Using the `-D` option will start the server with *drafts* enabled.

```shell
$ hugo server -D
```

#### Building the project

To deploy the blog in the most simple way, we need a simple *HTML, CSS and JS* files. We need those files, so we can
deploy the site on solutions like *AWS S3*, *Azure Blog Storage* or even *GitHub Pages*. To build the site, simply use

```shell
$ hugo
```

This will bundle all your Markdown files, themes, config and more and write the output to a directory called *public*.
If you have a look inside that directory, you'll see that it's a collection of files that you'll recognize from any
other website. Great! We've eliminated the need for web servers, now let's move on the deployment.

### Configuring AWS

For the setup on S3, we'll need 2 resources: [AWS S3](https://aws.amazon.com/s3/) and 
[AWS CloudFront](https://aws.amazon.com/cloudfront/). The first is an object store with the option to host static 
websites, the second is a CDN.

You might have seen some tutorials on how to set up S3 buckets using the AWS Console. This works fine, but I'm a firm
believer of managing your resources with code. I've chosen the native solution of AWS, called 
[AWS CloudFormation](https://aws.amazon.com/cloudformation/). This makes it easier to reproduce the setup if I ever need
to tear it down of move it to another account or region. Below is the full CloudFormation template, I've used a
framework called [Troposphere](https://github.com/cloudtools/troposphere), a Python library that creates CloudFormation.

The following snippet will create 2 important resources: an S3 bucket and a CloudFront distribution. The S3 bucket
is used to hold the static files, the CloudFront introduces caching. The *OriginAccessIdentity* makes sure clients
cannot access the files in S3 directly, but have to go through CloudFront. This optimizes cachhing and makes sure 
individuals cannot bombard your S3 bucket that will increase your AWS bill. To deploy the CloudFormation template, head over
to the CloudFormation console and create a new stack.

#### Setting up S3 and CloudFront

```yaml
Description: Static Website
Resources:
  Type: AWS::CloudFront::Distribution
  CloudFront:
    Properties:
      DistributionConfig:
      Comment: !Ref 'AWS::StackName'
      DefaultCacheBehavior:
      ForwardedValues:
      QueryString: false
      TargetOriginId: default
      ViewerProtocolPolicy: redirect-to-https
      Enabled: true
      HttpVersion: http2
      IPV6Enabled: true
      DefaultRootObject: 'index.html'
      Origins:
        - DomainName: !Join
              - ''
              - - !Ref 'WebsiteOrigin'
              - .s3.
              - !Ref 'AWS::Region'
              - .amazonaws.com
      Id: default
      S3OriginConfig:
      OriginAccessIdentity: !Join
              - ''
              - - origin-access-identity/cloudfront/
              - !Ref 'WebsiteOriginAccessIdentity'
      PriceClass: PriceClass_100
  WebsiteOrigin:
    Type: AWS::S3::Bucket
    Properties:
      AccessControl: Private
  WebsiteOriginAccessIdentity:
    Type: AWS::CloudFront::CloudFrontOriginAccessIdentity
    Properties:
      CloudFrontOriginAccessIdentityConfig:
        Comment: !Ref 'AWS::StackName'
  WebsiteOriginPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref 'WebsiteOrigin'
      PolicyDocument:
        Statement:
          - Action:
              - s3:GetObject
            Effect: Allow
            Principal:
              CanonicalUser: !GetAtt 'WebsiteOriginAccessIdentity.S3CanonicalUserId'
            Resource:
              - !Join
                - ''
                - - 'arn:aws:s3:::'
                  - !Ref 'WebsiteOrigin'
                  - /*
```

#### Uploading the website

To upload the website in the *public* directory to S3, the easy way is to go with the 
[AWS CLI](https://github.com/aws/aws-cli). After installing and configuring the CLI, use following command to upload
the website to S3. To get the name of your S3 bucket, head over to the S3 console. You'll see that a new bucket was
created by CloudFormation.

```shell
$ aws s3 sync ./public/ s3://BUCKET_NAME/
```

To view your website, head over to the *CloudFront* console and click on the URL for your distribution. It will load
the homepage of your blog. Now click on one of your posts, and realise that your website is completely broken. An error
from S3 will pop up because it cannot find some files. This is expected behaviour, Hugo expects your posts to be under
`/posts/my-first-post/`, but S3 cannot magically link that path to `/posts/my-first-post/index.html`. We'll have to 
find a workaround for this issue now, but I'll cover pretty URLs in another post.

#### Enabling ugly URLs

Hugo has the option to generate the site with ugly urls. Generate the site with the command mentioned above, but with
the `HUGO_UGLYURLS=true` environment variable set. This will still output the site in *public*, but Hugo will expect
the post to be on `/posts/my-first-post.html`, which is a path that S3 can find, so your post will work just fine now.
After generating the site locally, execute the command again to upload the files to S3 and wait a minute for the
CloudFront cache to expire.

### Wrapping up

Hugo in combination with AWS S3 and CloudFront is a quick and easy way to get started with a personal website. There
are still some TODOs which I'll cover in another post:
- Pretty URLs
- A custom domain
