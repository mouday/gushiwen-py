# -*- coding: utf-8 -*-
import datetime
from json import JSONEncoder

from gushiwen.model.extension import DictModel


class CustomJSONEncoder(JSONEncoder):
    """增加时间datetime 和Model 的格式化"""
    def default(self, obj):
        print(type(obj))

        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        elif isinstance(obj, DictModel):
            return obj.to_dict()

        else:
            return super().default(self, obj)
