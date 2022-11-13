# Introduction

In this workshop, we will build a to-do application without needing any server to run. We will
use [AWS Lambda](https://aws.amazon.com/lambda/),
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

## Installing NodeJS

AWS Lambda supports multiple languages by default, including Java, Python, Golang and many more. To keep the build
process
as simple as possible, we will use [Node.js](https://nodejs.org/en/) during this workshop. It does not require
compilation, and it is support by AWS Lambda by default.

To install Node.js, use can use one of the supported [package managers](https://nodejs.org/en/download/package-manager/)
or [download the installer](https://nodejs.org/en/#home-downloadhead).

```shell
# Install on Mac using Brew
brew install node

# Install on Ubuntu using Snap
sudo snap refresh node --channel=15

# Install on Windows using Chocolatey
cinst nodejs.install
```

## Accessing the AWS Console

Click [here](https://localhost ':id=console-link') to go to the AWS console. Log in with these credentials
[<span id=console-credentials></span>]

If you want to use the AWS CLI during the workshop, set the credentials in your shell.

!> These AWS Credentials are requested when you load the page. If the credentials don't show up, refresh this page.

##### CLI Credentials (Linux & Mac)

```shell aws-cli-code-bash
export AWS_ACCESS_KEY_ID="ACCESS_KEY_PLACEHOLDER"
export AWS_SECRET_ACCESS_KEY="SECRET_KEY_PLACEHOLDER"
```

##### CLI Credentials (Windows)

```powershell aws-cli-code-powershell
$Env:AWS_ACCESS_KEY_ID="ACCESS_KEY_PLACEHOLDER"
$Env:AWS_SECRET_ACCESS_KEY="SECRET_KEY_PLACEHOLDER"
```