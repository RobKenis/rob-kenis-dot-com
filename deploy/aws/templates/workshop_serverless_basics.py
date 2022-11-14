from troposphere import Template, Ref, AWS_STACK_NAME, GetAtt
from troposphere.iam import Role, Policy
from awacs.aws import PolicyDocument, Statement, Allow, Principal, Action
from troposphere.dynamodb import Table, AttributeDefinition, KeySchema

template = Template(Description="Lab resources and requirements for AWS Serverless Basics")

to_do_items = template.add_resource(Table(
    'ToDoItems',
    TableName='to-do-items',
    BillingMode='PAY_PER_REQUEST',
    AttributeDefinitions=[AttributeDefinition(AttributeName='id', AttributeType='S')],
    KeySchema=[KeySchema(AttributeName='id', KeyType='HASH')]
))

template.add_resource(Role(
    'LambdaExecution',
    RoleName='workshop-lambda-execution',
    Description=Ref(AWS_STACK_NAME),
    ManagedPolicyArns=[
        'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    ],
    Policies=[Policy(
        PolicyName='use-dynamodb',
        PolicyDocument=PolicyDocument(
            Statement=[Statement(
                Effect=Allow,
                Action=[
                    Action("dynamodb:BatchGet*"),
                    Action("dynamodb:DescribeStream"),
                    Action("dynamodb:DescribeTable"),
                    Action("dynamodb:Get*"),
                    Action("dynamodb:Query"),
                    Action("dynamodb:Scan"),
                    Action("dynamodb:BatchWrite*"),
                    Action("dynamodb:CreateTable"),
                    Action("dynamodb:Delete*"),
                    Action("dynamodb:Update*"),
                    Action("dynamodb:PutItem"),
                ],
                Resource=[GetAtt(to_do_items, 'Arn')],
            )]
        )
    )],
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
