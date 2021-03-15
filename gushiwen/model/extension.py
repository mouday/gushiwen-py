# -*- coding: utf-8 -*-
import datetime
import json
import logging
import time
from collections import Iterator, Iterable
from functools import wraps

from peewee import MySQLDatabase, SENTINEL, Model, ForeignKeyField

# 日志设置
from playhouse.shortcuts import model_to_dict
from playhouse.db_url import schemes, register_database

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
logger.propagate = False  # 不向上传播


# 计时器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        ret = func(*args, **kwargs)

        end_time = time.time()
        logger.debug("time: %.2f s" % (end_time - start_time))

        return ret

    return wrapper


class CustomMySQLDatabase(MySQLDatabase):
    """
    打印sql执行时间
    see: https://github.com/coleifer/peewee/issues/2370
    """

    @timer
    def execute_sql(self, sql, params=None, commit=SENTINEL):
        return super().execute_sql(sql, params, commit)


register_database(CustomMySQLDatabase, 'mysql')


def connect(**kwargs):
    scheme = kwargs.pop('scheme')
    return schemes[scheme](**kwargs)


def encode_complex(obj):
    if isinstance(obj, datetime.datetime):
        return obj.__repr__()

    elif isinstance(obj, DictModel):
        return obj.to_dict()


class DictModel(Model):

    def to_data(self, recurse=True, backrefs=False,
                only=None, exclude=None,
                seen=None, extra_attrs=None,
                fields_from_query=None, max_depth=None,
                manytomany=False):
        return model_to_dict(self,
                             recurse=recurse, backrefs=backrefs,
                             only=only, exclude=exclude,
                             seen=seen, extra_attrs=extra_attrs,
                             fields_from_query=fields_from_query,
                             max_depth=max_depth, manytomany=manytomany)

    def to_dict(self):
        return dict(self.__data__)

    def __str__(self):
        return json.dumps(self, ensure_ascii=False, default=encode_complex)


# 返回字典
def to_dict(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        logger.debug('decorator: to dict')

        result = func(*args, **kwargs)

        def _to_dict(item):
            if isinstance(item, DictModel):
                return item.to_dict()
            else:
                return item

        if isinstance(result, Iterable):
            return list(map(_to_dict, result))
        else:
            return _to_dict(result)

    return decorator


# 返回嵌套字典
def to_data(func=None, recurse=True, backrefs=False,
            only=None, exclude=None,
            seen=None, extra_attrs=None,
            fields_from_query=None, max_depth=1,
            manytomany=False):
    def inner(inner_func):
        @wraps(inner_func)
        def decorator(*func_args, **func_kwargs):
            logger.debug('decorator: to data')

            result = inner_func(*func_args, **func_kwargs)

            def _to_data(item):
                if isinstance(item, DictModel):
                    return item.to_data(
                        recurse=recurse, backrefs=backrefs,
                        only=only, exclude=exclude,
                        seen=seen, extra_attrs=extra_attrs,
                        fields_from_query=fields_from_query,
                        max_depth=max_depth, manytomany=manytomany)
                else:
                    return item

            if isinstance(result, Iterable):
                return list(map(_to_data, result))
            else:
                return _to_data(result)

        return decorator

    if func is None:
        return inner
    else:
        return inner(func)
