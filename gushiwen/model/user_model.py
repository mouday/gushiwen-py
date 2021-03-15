# -*- coding: utf-8 -*-

from peewee import *

from .base_model import BaseModel


class UserModel(BaseModel):
    name = CharField(max_length=50, unique=True)
    password = CharField(max_length=100)

    class Meta:
        table_name = 'user'
