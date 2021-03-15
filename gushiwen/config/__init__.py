# -*- coding: utf-8 -*-

from .production import *

from environs import Env

Env.read_env()

# 如果是测试环境，从测试配置中导入，覆盖默认配置
env = Env()

DEBUG = env.bool('MODE_DEBUG', True)

print('MODE_DEBUG', DEBUG)

if DEBUG:
    from .development import *
