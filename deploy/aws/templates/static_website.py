from awacs import s3
from awacs.aws import PolicyDocument, Policy, Statement, Allow, Principal
from troposphere import Template, ImportValue, Parameter, constants, Join, Ref, Tags, AWS_STACK_NAME, GetAtt, \
    AWS_REGION, Output
from troposphere.certificatemanager import Certificate, DomainValidationOption
from troposphere.cloudfront import Distribution, DistributionConfig, DefaultCacheBehavior, Origin, ViewerCertificate, \
    CloudFrontOriginAccessIdentity, CloudFrontOriginAccessIdentityConfig, S3OriginConfig, ForwardedValues
from troposphere.route53 import RecordSetGroup, RecordSet, AliasTarget
from troposphere.s3 import Bucket, BucketPolicy

template = Template(Description="Static Website")

dns_stack = template.add_parameter(Parameter(
    'DnsStack',
    Type=constants.STRING,
    Default='rob-kenis-dot-com-dns',
    Description='Name of the CloudFormation stack that holds the HostedZone',
))

cloudfront_certificate = template.add_resource(Certificate(
    "CloudFrontCertificate",
    DomainName='robkenis.com',
    SubjectAlternativeNames=['www.robkenis.com'],
    ValidationMethod='DNS',
    DomainValidationOptions=[
        DomainValidationOption(
            DomainName='robkenis.com',
            HostedZoneId=ImportValue(Join('-', [Ref(dns_stack), 'HostedZoneId'])),
        ),
        DomainValidationOption(
            DomainName='www.robkenis.com',
            HostedZoneId=ImportValue(Join('-', [Ref(dns_stack), 'HostedZoneId'])),
        ),
    ],
    Tags=Tags({'Name': Ref(AWS_STACK_NAME)}),
))

s3_website_origin = template.add_resource(Bucket(
    'WebsiteOrigin',
    AccessControl='Private',
))

origin_access_identity = template.add_resource(CloudFrontOriginAccessIdentity(
    'WebsiteOriginAccessIdentity',
    CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig(
        Comment=Ref(AWS_STACK_NAME),
    ),
))

template.add_resource(BucketPolicy(
    'WebsiteOriginPolicy',
    Bucket=Ref(s3_website_origin),
    PolicyDocument=Policy(
        Statement=[Statement(
            Effect=Allow,
            Action=[s3.GetObject],
            Resource=[Join('', ['arn:aws:s3:::', Ref(s3_website_origin), '/*'])],
            Principal=Principal('CanonicalUser', GetAtt(origin_access_identity, 'S3CanonicalUserId')),
        )],
    ),
))

cloudfront = template.add_resource(Distribution(
    'CloudFront',
    DistributionConfig=DistributionConfig(
        Aliases=['robkenis.com', 'www.robkenis.com'],
        Comment=Ref(AWS_STACK_NAME),
        DefaultCacheBehavior=DefaultCacheBehavior(
            TargetOriginId='default',
            ViewerProtocolPolicy='redirect-to-https',
            ForwardedValues=ForwardedValues(
                QueryString=False,
            ),
        ),
        DefaultRootObject='index.html',
        Enabled=True,
        HttpVersion='http2',
        IPV6Enabled=True,
        Origins=[Origin(
            Id='default',
            DomainName=Join('', [Ref(s3_website_origin), '.s3.', Ref(AWS_REGION), '.amazonaws.com']),
            S3OriginConfig=S3OriginConfig(
                OriginAccessIdentity=Join('', [
                    'origin-access-identity/cloudfront/',
                    Ref(origin_access_identity),
                ]),
            ),
        )],
        PriceClass='PriceClass_100',
        ViewerCertificate=ViewerCertificate(
            AcmCertificateArn=Ref(cloudfront_certificate),
            SslSupportMethod='sni-only',
        ),
    ),
))

template.add_resource(RecordSetGroup(
    'DnsRecords',
    Comment=Ref(AWS_STACK_NAME),
    HostedZoneId=ImportValue(Join('-', [Ref(dns_stack), 'HostedZoneId'])),
    RecordSets=[
        RecordSet(
            Name='robkenis.com',
            Type='A',
            AliasTarget=AliasTarget(
                DNSName=GetAtt(cloudfront, 'DomainName'),
                HostedZoneId='Z2FDTNDATAQYW2',
            ),
        ),
        RecordSet(
            Name='robkenis.com',
            Type='AAAA',
            AliasTarget=AliasTarget(
                DNSName=GetAtt(cloudfront, 'DomainName'),
                HostedZoneId='Z2FDTNDATAQYW2',
            ),
        ),
        RecordSet(
            Name='www.robkenis.com',
            Type='A',
            AliasTarget=AliasTarget(
                DNSName=GetAtt(cloudfront, 'DomainName'),
                HostedZoneId='Z2FDTNDATAQYW2',
            ),
        ),
        RecordSet(
            Name='www.robkenis.com',
            Type='AAAA',
            AliasTarget=AliasTarget(
                DNSName=GetAtt(cloudfront, 'DomainName'),
                HostedZoneId='Z2FDTNDATAQYW2',
            ),
        ),
    ],
))

template.add_output(Output(
    'WebsiteOriginBucketName',
    Description='Name of the S3 bucket that holds the website',
    Value=Ref(s3_website_origin),
))

f = open("output/static_website.json", "w")
f.write(template.to_json())
