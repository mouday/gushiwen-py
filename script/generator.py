# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, PackageLoader

BASE_DIR = 'gushiwen'


def render(template_name, **kwargs):
    env = Environment(loader=PackageLoader(__name__))
    template = env.get_template(template_name)
    return template.render(kwargs)


def get_full_name(file_type, file_name):
    return os.path.join(os.getcwd(), f"{BASE_DIR}/{file_type}/{file_name}_{file_type}.py")


def camel_case(name: str):
    return ''.join([char.title() for char in name.split('_')])


def gen(file_type, file_name, **kwargs):
    full_name = get_full_name(file_type, file_name)
    if os.path.exists(full_name):
        print('file exists', full_name)
        return

    template_name = file_type + '.tpl'

    data = {
        'table_name': file_name,
        'class_name': camel_case(file_name)
    }

    content = render(template_name, **data)

    with open(full_name, 'w') as f:
        f.write(content)
