from awacs.aws import PolicyDocument, Statement, Allow, Action
from troposphere import Template, AWS_STACK_NAME, Ref
from troposphere.iam import User, Policy

template = Template(Description="Everything to make deployments by GitHub Actions possible")

template.add_resource(User(
    'GitHub',
    UserName=Ref(AWS_STACK_NAME),
    Policies=[
        Policy(
            PolicyName='AllowCloudFormation',
            PolicyDocument=PolicyDocument(
                Statement=[Statement(
                    Effect=Allow,
                    Action=[Action(prefix='cloudformation', action='*')],
                    Resource=['*'],
                )]
            )
        ),
        Policy(
            PolicyName='AllowACM',
            PolicyDocument=PolicyDocument(
                Statement=[Statement(
                    Effect=Allow,
                    Action=[
                        Action(prefix='acm', action='*'),
                        Action(prefix='route53', action='*'),
                    ],
                    Resource=['*'],
                )]
            )
        ),
        Policy(
            PolicyName='AllowS3',
            PolicyDocument=PolicyDocument(
                Statement=[Statement(
                    Effect=Allow,
                    Action=[Action(prefix='s3', action='*')],
                    Resource=['*'],
                )]
            )
        ),
        Policy(
            PolicyName='AllowCloudFront',
            PolicyDocument=PolicyDocument(
                Statement=[Statement(
                    Effect=Allow,
                    Action=[Action(prefix='cloudfront', action='*')],
                    Resource=['*'],
                )]
            )
        )
    ]
))

f = open("output/github.json", "w")
f.write(template.to_json())
