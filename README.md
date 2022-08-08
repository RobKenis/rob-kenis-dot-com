# Hello

> My very own homepage on the internet

![Validate](https://github.com/RobKenis/rob-kenis-dot-com/actions/workflows/validate.yaml/badge.svg)
![Deploy](https://github.com/RobKenis/rob-kenis-dot-com/actions/workflows/deploy.yaml/badge.svg)
![Deploy](https://github.com/RobKenis/rob-kenis-dot-com/actions/workflows/learn.yaml/badge.svg)

## Blog

The blog section is created using [hugo](https://gohugo.io).
```shell
# Create a new post
$ hugo new posts/my-new-post.md
```

```shell
# Start the server with drafts enabled
$ HUGO_UGLYURLS=true hugo server -D
```
It is important to enable ugly URLs when running locally. This is also the way that the site is deployed, so links
are adapted to append the extension. When running locally without ugly URLS, the menu will break.
- [ ] TODO: Make pretty URLs work in S3/CloudFront.

```shell
# Build static pages
$ hugo -D
```
