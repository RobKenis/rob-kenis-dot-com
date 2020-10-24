from troposphere import Template, ImportValue, Parameter, constants, Join, Ref, Tags, AWS_STACK_NAME
from troposphere.certificatemanager import Certificate, DomainValidationOption

template = Template(Description="Static Website")

dns_stack = template.add_parameter(Parameter(
    'DnsStack',
    Type=constants.STRING,
    Default='rob-kenis-dot-com-dns',
    Description='Name of the CloudFormation stack that holds the HostedZone',
))

template.add_resource(Certificate(
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

f = open("output/static_website.json", "w")
f.write(template.to_json())
