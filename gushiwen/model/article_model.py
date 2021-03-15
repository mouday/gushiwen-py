# -*- coding: utf-8 -*-
from peewee import *

from .author_model import AuthorModel
from .base_model import BaseModel


class ArticleModel(BaseModel):
    title = CharField(max_length=200)
    content = TextField()
    author = ForeignKeyField(AuthorModel, backref='articles')

    class Meta:
        table_name = 'article'
