# Hello

> My very own homepage on the internet

![Validate](https://github.com/RobKenis/rob-kenis-dot-com/actions/workflows/validate.yml/badge.svg)
![Deploy](https://github.com/RobKenis/rob-kenis-dot-com/actions/workflows/deploy.yml/badge.svg)

## Developing

```shell
# Install dependencies
$ yarn install

# Serve with hot reload at localhost:3000
$ yarn dev
```

## Deploying

When new commits are pushed to `master`, the website is deployed using 
_GitHub Actions_. To build locally, run following commands

```shell
$ yarn build
```

## Storybook

```shell
# Run storybook on port 6006
$ yarn storybook
```

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
