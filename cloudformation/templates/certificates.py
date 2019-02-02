from troposphere import Template, Output, Ref, Export, Join, AWS_STACK_NAME
from troposphere.certificatemanager import Certificate, DomainValidationOption

VALIDATION_DOMAIN = 'robkenis.com'

DOMAINS = {
    'RobKenisDotCom': {
        'domain': 'robkenis.com',
        'altNames': [],
    }
}

template = Template(Description='Certificates for CloudFront')
for key, config in DOMAINS.items():
    certificate = template.add_resource(Certificate(
        "Certificate",
        DomainName=config['domain'],
        SubjectAlternativeNames=config['altNames'],
        DomainValidationOptions=[DomainValidationOption(
            DomainName=config['domain'],
            ValidationDomain=VALIDATION_DOMAIN,
        )],
        ValidationMethod='DNS',
    ))

    template.add_output(Output(
        key + 'Output',
        Description='Arn of the Certificate',
        Value=Ref(certificate),
        Export=Export(
            name=Join('-', [Ref(AWS_STACK_NAME), key, 'Arn']),
        ),
    ))

f = open("output/certificates.json", "w")
f.write(template.to_json())
