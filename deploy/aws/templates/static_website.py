from troposphere import Template

template = Template(Description="Static Website")

f = open("output/static_website.json", "w")
f.write(template.to_json())
