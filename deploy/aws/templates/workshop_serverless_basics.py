from troposphere import Template, Ref, AWS_STACK_NAME
from troposphere.iam import Role
from awacs.aws import PolicyDocument, Statement, Allow, Principal, Action

template = Template(Description="Lab resources and requirements for AWS Serverless Basics")

template.add_resource(Role(
    'LambdaExecution',
    RoleName='workshop-lambda-execution',
    Description=Ref(AWS_STACK_NAME),
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    ],
    AssumeRolePolicyDocument=PolicyDocument(
        Statement=[Statement(
            Effect=Allow,
            Action=[Action('sts:AssumeRole')],
            Principal=Principal(principal='Service', resources='lambda.amazonaws.com'),
        )]
    )
))

f = open("output/workshop_serverless_basics.json", "w")
f.write(template.to_json())
