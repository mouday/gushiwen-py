# -*- coding: utf-8 -*-

from gushiwen.config import DB_CONFIG
from .extension import connect

db = connect(**DB_CONFIG)
