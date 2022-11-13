from awacs.aws import PolicyDocument, Statement, Action, Allow, Deny
from troposphere import Template, Ref
from troposphere.iam import User, ManagedPolicy
from troposphere.serverless import Globals, ApiGlobals, Cors, Function, ApiEvent
from troposphere.ssm import Parameter

template = Template(Description="Provides an API to request console and cli credentials")
template.set_transform('AWS::Serverless-2016-10-31')

template.set_globals(globals=Globals(
    Api=ApiGlobals(
        Cors=Cors(
            AllowMethods="'GET,OPTIONS'",
            AllowHeaders="'content-type'",
            AllowOrigin="'*'",
            AllowCredentials="'*'",
        )
    )
))

guest_admin_policy = template.add_resource(ManagedPolicy(
    'GuestAdminPolicy',
    ManagedPolicyName='guest-serverless-full-admin',
    PolicyDocument=PolicyDocument(
        Version='2012-10-17',
        Statement=[Statement(
            Effect=Allow,
            Action=[
                Action('cloudformation:*'),
                Action('s3:*'),
                Action('lambda:*'),
                Action('cloudfront:*'),
                Action('iam:*'),
                Action('apigateway:*'),
                Action('dynamodb:*'),
                Action('cloudwatch:*'),
                Action('logs:*'),
            ],
            Resource=['*'],
        ), Statement(
            Effect=Deny,
            Action=[
                Action('iam:CreateUser'),
            ],
            Resource=['*'],
        )]
    )
))

template.add_resource(User(
    'GuestUser',
    UserName='guest',
    ManagedPolicyArns=[Ref(guest_admin_policy)]
))

access_key = template.add_resource(Parameter(
    'GuestAccessKey',
    Name='/workshop/guest/accesskey',
    Type='String',
    Value='haha',
    Description='IAM access key for the guest user',
))

secret_key = template.add_resource(Parameter(
    'GuestSecretKey',
    Name='/workshop/guest/secretkey',
    Type='String',
    Value='haha',
    Description='IAM secret for the guest user',
))

password = template.add_resource(Parameter(
    'GuestConsolePassword',
    Name='/workshop/guest/password',
    Type='String',
    Value='haha',
    Description='Password for the guest user to login to the console',
))

with open('./code/get_credentials.js', mode='r') as code:
    template.add_resource(Function(
        'GetCredentialsFunction',
        FunctionName='guest-user-get-credentials',
        Handler='index.handler',
        Runtime='nodejs14.x',
        InlineCode=code.read(),
        Policies=[
            'AWSLambdaExecute',
            PolicyDocument(
                Version='2012-10-17',
                Statement=[Statement(
                    Effect=Allow,
                    Action=[
                        Action('ssm:GetParameter'),
                    ],
                    # TODO: Restrict this, but GetAtt and Ref don't work because they return the name.
                    Resource=['*'],
                )]
            )
        ],
        Events={
            'GetCredentials': ApiEvent(
                'GetCredentials',
                Path='/',
                Method='GET',
            )
        }
    ))

f = open("output/guest_access.json", "w")
f.write(template.to_json())
