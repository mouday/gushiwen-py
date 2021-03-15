# -*- coding: utf-8 -*-
from peewee import *

from .base_model import BaseModel


class DynastyModel(BaseModel):
    name = CharField(max_length=50, unique=True)

    class Meta:
        table_name = 'dynasty'