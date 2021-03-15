# -*- coding: utf-8 -*-
import json

from jinja2.filters import do_mark_safe

from gushiwen.common.main import CustomJSONEncoder
from gushiwen.service import DynastyService
from flask import g


def dynasty_filter(dynasty_id):
    """
    使用了 g对象
    :param dynasty_id:
    :return:
    """
    if 'mapping' not in g:
        g.mapping = DynastyService.get_all_dynasties_map()
    return g.mapping.get(dynasty_id)


def content_filter(content):
    break_tags = ['。']
    for tag in break_tags:
        content = content.replace(tag, f'{tag}<br/>')

    return do_mark_safe(content)


def dump_filter(obj):
    return json.dumps(obj, ensure_ascii=False, cls=CustomJSONEncoder)
