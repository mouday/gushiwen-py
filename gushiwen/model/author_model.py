# -*- coding: utf-8 -*-

from peewee import *

from .user_model import UserModel
from .dynasty_model import DynastyModel
from .base_model import BaseModel


class AuthorModel(BaseModel):
    name = CharField(max_length=50)
    dynasty = ForeignKeyField(DynastyModel, backref='authors')
    user = ForeignKeyField(UserModel, unique=True, null=True, backref='author')

    class Meta:
        table_name = 'author'
