import awacs.s3 as s3
from awacs.aws import Policy, Statement, Allow, Principal
from troposphere import Template, AWS_STACK_NAME, Ref, Join, GetAtt, Parameter, constants, AWS_REGION
from troposphere.cloudfront import CloudFrontOriginAccessIdentity, CloudFrontOriginAccessIdentityConfig, Distribution, \
    DistributionConfig, DefaultCacheBehavior, Origin, S3OriginConfig, ForwardedValues, ViewerCertificate
from troposphere.route53 import RecordSetGroup, RecordSet, AliasTarget
from troposphere.s3 import Bucket, WebsiteConfiguration, BucketPolicy

template = Template(Description="Static website with CloudFront")

domain_name = template.add_parameter(Parameter(
    'DomainName',
    Type=constants.STRING,
))

certificate_arn = template.add_parameter(Parameter(
    'CertificateArn',
    Type=constants.STRING,
))

hosted_zone_id = template.add_parameter(Parameter(
    'HostedZoneId',
    Type=constants.STRING,
    Default='Z2GNC22ZPZPE8L',
))

oai = template.add_resource(CloudFrontOriginAccessIdentity(
    "OriginAccessIdentity",
    CloudFrontOriginAccessIdentityConfig=CloudFrontOriginAccessIdentityConfig(
        Comment="Used to control access between S3 bucket for static website and CloudFront.",
    ),
))

bucket = template.add_resource(Bucket(
    "S3Bucket",
    BucketName=Ref(AWS_STACK_NAME),
    AccessControl='PublicRead',
    WebsiteConfiguration=WebsiteConfiguration(
        IndexDocument='index.html',
        ErrorDocument='index.html',
    ),
))

bucket_policy = template.add_resource(BucketPolicy(
    "BucketPolicy",
    Bucket=Ref(bucket),
    PolicyDocument=Policy(
        Statement=[Statement(
            Effect=Allow,
            Action=[s3.GetObject],
            Resource=[Join('', ['arn:aws:s3:::', Ref(bucket), '/*'])],
            Principal=Principal('CanonicalUser', GetAtt(oai, 'S3CanonicalUserId')),
        )],
    ),
))

cloudfront = template.add_resource(Distribution(
    "CloudFrontDistribution",
    DistributionConfig=DistributionConfig(
        Aliases=[Ref(domain_name)],
        Comment=Ref(AWS_STACK_NAME),
        DefaultCacheBehavior=DefaultCacheBehavior(
            TargetOriginId='S3',
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
            DomainName=Join('', [Ref(bucket), '.s3.', Ref(AWS_REGION), '.amazonaws.com']),
            Id='S3',
            S3OriginConfig=S3OriginConfig(
                OriginAccessIdentity=Join('/', ['origin-access-identity', 'cloudfront', Ref(oai)]),
            ),
        )],
        PriceClass='PriceClass_100',
        ViewerCertificate=ViewerCertificate(
            AcmCertificateArn=Ref(certificate_arn),
            SslSupportMethod='sni-only',
            MinimumProtocolVersion='TLSv1.1_2016',
        ),
    ),
))

dns_record = template.add_resource(RecordSetGroup(
    "DnsRecordA",
    HostedZoneId=Ref(hosted_zone_id),
    RecordSets=[RecordSet(
        Name=Ref(domain_name),
        Type='A',
        AliasTarget=AliasTarget(
            HostedZoneId='Z2FDTNDATAQYW2',
            DNSName=GetAtt(cloudfront, 'DomainName'),
        ),
    )],
    Comment=Join('', ['A-Record for CloudFront in ', Ref(AWS_STACK_NAME)]),
))

f = open("output/static_website.json", "w")
f.write(template.to_json())
