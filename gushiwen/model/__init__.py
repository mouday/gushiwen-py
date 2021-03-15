# -*- coding: utf-8 -*-
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
