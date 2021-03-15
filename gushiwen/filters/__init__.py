# -*- coding: utf-8 -*-
"""
过滤器
"""
from .main import *

FILTERS = {
    'dynasty':   dynasty_filter,
    'dump':      dump_filter,
    'content':   content_filter
}


def register_filters(app):
    for filter_name, filter_func in FILTERS.items():
        app.jinja_env.filters[filter_name] = filter_func
