# -*- coding: utf-8 -*-
from playhouse.flask_utils import FlaskDB

from .article_model import ArticleModel
from .author_model import AuthorModel
from .dynasty_model import DynastyModel
from .user_model import UserModel
from .database import db

tables = [
    ArticleModel,
    AuthorModel,
    DynastyModel,
    UserModel
]


def register_database(app):
    """web 长链接的一种方式，适合访问频率低场景"""
    FlaskDB(app=app, database=db)
