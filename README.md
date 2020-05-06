> This repository is part of Relay Monkey project.

## About
Jinja template to convert Relay Monkey Terraform output to Ansible inventory.

## Usage
In the directory of `terraform-to-inventory.py`, `public_ips.json` is expected. This is JSON Terraform output from Relay Monkey project. Feel free to expand the program to accept arguments.
```shell
python terraform-to-inventory.py
```
