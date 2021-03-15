# -*- coding: utf-8 -*-
from datetime import datetime

from peewee import *

from .extension import DictModel
from .database import db


class BModel(DictModel):
    class Meta:
        database = db


class BaseModel(BModel):
    create_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)
