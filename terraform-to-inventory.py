from jinja2 import Template
import json

template = Template(
    open('ansible_inventory.j2').read(),
    trim_blocks=True,
    lstrip_blocks=True
)

terraform_data = json.load(
    open('public_ips.json')
)

jinja_render = template.render(providers=terraform_data)

print(jinja_render)

with open('ansible_inventory.yml', 'w') as the_file:
    the_file.write(jinja_render)
