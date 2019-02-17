import awacs
from awacs import aws, sts
from awacs.aws import Principal, Action
from troposphere import Template, GetAtt, Ref, Parameter, constants, AWS_STACK_NAME, Join
from troposphere.codebuild import Project, Artifacts, Source, Environment
from troposphere.codepipeline import Pipeline, Stages, Actions, ActionTypeId, ArtifactStore, OutputArtifacts, \
    InputArtifacts
from troposphere.iam import Role, Policy

template = Template(Description="Code pipeline for static website to S3.")

github_user = template.add_parameter(Parameter(
    "GithubUser",
    Type=constants.STRING
))

github_token = template.add_parameter(Parameter(
    "GithubToken",
    Type=constants.STRING
))

github_repo = template.add_parameter(Parameter(
    "GithubRepo",
    Type=constants.STRING
))

website_bucket = template.add_parameter(Parameter(
    "WebsiteBucket",
    Type=constants.STRING
))

pipeline_role = template.add_resource(Role(
    "CodePipelineRole",
    RoleName=Join("-", [Ref(AWS_STACK_NAME), "pipeline-role"]),
    AssumeRolePolicyDocument=awacs.aws.Policy(
        Statement=[
            awacs.aws.Statement(
                Effect=awacs.aws.Allow,
                Action=[awacs.sts.AssumeRole],
                Principal=Principal("Service", "codepipeline.amazonaws.com")
            ),
        ]
    ),
    Policies=[
        Policy(
            PolicyName='AllowS3',
            PolicyDocument=awacs.aws.Policy(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[Action("s3", "*")],
                        Resource=[
                            Join('', ["arn:aws:s3:::", Ref(website_bucket), "/*"]),
                            Join("", ["arn:aws:s3:::", Ref(website_bucket)]),
                        ],
                    )
                ]
            ),
        ),
        Policy(
            PolicyName='AllowCodeCommit',
            PolicyDocument=awacs.aws.Policy(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[Action("codecommit", "*")],
                        Resource=['*']
                    ),
                ]
            )
        ),
        Policy(
            PolicyName='AllowCodeBuild',
            PolicyDocument=awacs.aws.Policy(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[Action("codebuild", "*")],
                        Resource=['*']
                    ),
                ]
            )
        ),
    ]
))

codebuild_role = template.add_resource(Role(
    "CodeBuildRole",
    RoleName=Join("-", [Ref(AWS_STACK_NAME), "build-role"]),
    AssumeRolePolicyDocument=awacs.aws.Policy(
        Statement=[
            awacs.aws.Statement(
                Effect=awacs.aws.Allow,
                Action=[awacs.sts.AssumeRole],
                Principal=Principal("Service", 'codebuild.amazonaws.com'),
            ),
        ]
    ),
    Policies=[
        Policy(
            PolicyName='AllowCodeBuild',
            PolicyDocument=awacs.aws.Policy(
                Statement=[
                    awacs.aws.Statement(
                        Effect=awacs.aws.Allow,
                        Action=[
                            Action("codebuild", "**"),
                            Action("logs", "**"),
                            Action("s3", "**"),
                        ],
                        Resource=['*']
                    )
                ]
            ),
        )
    ]
))

codebuild_project = template.add_resource(Project(
    "CodebuildProject",
    Name=Join("-", [Ref(AWS_STACK_NAME), "build-project"]),
    ServiceRole=GetAtt(codebuild_role, 'Arn'),
    Source=Source(
        Type='CODEPIPELINE',
    ),
    Artifacts=Artifacts(
        Type='CODEPIPELINE'
    ),
    Environment=Environment(
        Type='LINUX_CONTAINER',
        Image='aws/codebuild/nodejs:10.14.1',
        ComputeType='BUILD_GENERAL1_SMALL'
    )
))

template.add_resource(Pipeline(
    "CodePipeline",
    Name=Ref(AWS_STACK_NAME),
    RoleArn=GetAtt(pipeline_role, 'Arn'),
    ArtifactStore=ArtifactStore(
        Type='S3',
        Location=Ref(website_bucket)
    ),
    Stages=[
        Stages(
            Name="Checkout",
            Actions=[
                Actions(
                    Name="CheckoutGithub",
                    ActionTypeId=ActionTypeId(
                        Category='Source',
                        Owner='ThirdParty',
                        Provider='GitHub',
                        Version='1'
                    ),
                    Configuration={
                        "Owner": Ref(github_user),
                        "Repo": Ref(github_repo),
                        "Branch": "master",
                        "OAuthToken": Ref(github_token)
                    },
                    OutputArtifacts=[
                        OutputArtifacts(
                            Name="SourceOutput"
                        )
                    ]
                )
            ]
        ),
        Stages(
            Name="Build",
            Actions=[
                Actions(
                    Name="Build",
                    ActionTypeId=ActionTypeId(
                        Category='Build',
                        Owner='AWS',
                        Provider='CodeBuild',
                        Version='1'
                    ),
                    InputArtifacts=[
                        InputArtifacts(
                            Name='SourceOutput'
                        )
                    ],
                    OutputArtifacts=[
                        OutputArtifacts(
                            Name="BuildResult"
                        )
                    ],
                    Configuration={
                        "ProjectName": Ref(codebuild_project),
                    }
                )
            ]
        ),
    ]
))

f = open("output/code_pipeline.json", "w")
f.write(template.to_json())
