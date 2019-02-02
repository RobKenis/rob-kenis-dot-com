from troposphere import Template, Parameter, constants, Ref
from troposphere.route53 import RecordSetGroup, RecordSet, AliasTarget

# TODO CloudFormation doesn't seem to be creating the records :/

RECORDS = {
    '_ee9257d7567f7e81f21834f9729a1645.robkenis.com.': '_9fb53cd3302b3f33277aa9089b51be69.hkvuiqjoua.acm-validations.aws.'
}

template = Template(Description='List of validation records for ACM')

hosted_zone_id = template.add_parameter(Parameter(
    'HostedZoneId',
    Type=constants.STRING,
    Default='Z2GNC22ZPZPE8L',
))

template.add_resource(RecordSetGroup(
    'ValidationRecords',
    HostedZoneId=Ref(hosted_zone_id),
    Comment='Validation records for ACM',
    RecordSets=list(map(lambda name: RecordSet(
        Name=name,
        Type='CNAME',
        AliasTarget=AliasTarget(
            HostedZoneId=Ref(hosted_zone_id),
            DNSName=RECORDS[name],
        ),
    ), RECORDS.keys()))
))

f = open("output/validation_records.json", "w")
f.write(template.to_json())
