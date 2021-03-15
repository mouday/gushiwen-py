# -*- coding: utf-8 -*-
from typing import List
from unittest import TestCase
from gushiwen.model import ArticleModel, AuthorModel
from gushiwen.model.extension import to_dict, to_data
from .dynasty_service import DynastyService


class ArticleService:
    """article"""

    @classmethod
    @to_dict
    def get_article_by_author_and_title(cls, author_or_author_id, title):
        return (ArticleModel
                .select()
                .where((ArticleModel.author == author_or_author_id)
                       & (ArticleModel.title == title)).first())

    @classmethod
    @to_dict
    def create_article(cls, author_or_author_id, title, content):
        return ArticleModel.create(author=author_or_author_id, title=title, content=content)

    @classmethod
    @to_dict
    def get_or_create(cls, author_or_author_id, title, content):
        row, _ = ArticleModel.get_or_create(author=author_or_author_id, title=title, content=content)
        return row

    @classmethod
    @to_data(max_depth=1)
    def get_articles(cls, page=1, size=5, dynasty_id=None, author_id=None) -> List:
        query = (ArticleModel
                 .select(ArticleModel, AuthorModel)
                 .join(AuthorModel))

        # dynasty_id = None
        # if dynasty_name:
        #     dynasty_id = DynastyService.get_dynasty_id_by_name_from_cache(dynasty_name)

        if dynasty_id:
            query = query.where(AuthorModel.dynasty == dynasty_id)

        elif author_id:
            query = query.where(AuthorModel.id == author_id)

        rows = (query
                .order_by(ArticleModel.create_time.desc())
                .paginate(page, size))

        return rows

    @classmethod
    def get_article_total(cls):
        return ArticleModel.select().count()

    @classmethod
    def get_article(cls, uid):
        return ArticleModel.get_or_none(uid)

    @classmethod
    @to_data(max_depth=1)
    def get_article_with_author(cls, uid):
        return cls.get_article(uid)

    @classmethod
    def get_article_total_by_author(cls, author_id=None)->int:
        query = ArticleModel.select()
        if author_id:
            query = query.where(ArticleModel.author == author_id)

        return query.count()

    @classmethod
    def get_article_total_by_dynasty(cls, dynasty_id=None) -> int:
        query = ArticleModel.select()
        if dynasty_id:
            query = query.join(AuthorModel).where(AuthorModel.dynasty_id == dynasty_id)

        return query.count()


class TestArticleService(TestCase):
    def test_get_article_by_author_and_title(self):
        author = 1
        title = '渡浙江问舟中人'

        row = ArticleService.get_article_by_author_and_title(author_or_author_id=author, title=title)
        print(row)

    def test_get_articles(self):
        rows = ArticleService.get_articles()
        print(rows)

        rows = ArticleService.get_articles(dynasty_id=1)
        print(rows)

        rows = ArticleService.get_articles(author_id=1)
        print(rows)

    def test_get_article_total(self):
        total = ArticleService.get_article_total()
        print(total)

    def test_get_article(self):
        row = ArticleService.get_article(1)
        print(row)

        print(row.author_id)

        row = ArticleService.get_article(100)
        print(row)

    def test_get_article_with_author(self):
        row = ArticleService.get_article_with_author(1)
        print(row)
        # print(row['author'])

        row = ArticleService.get_article(100)
        print(row)

    def test_get_article_total_by_author(self):
        row = ArticleService.get_article_total_by_author()
        print(row)

        row = ArticleService.get_article_total_by_author(1)
        print(row)

    def test_get_article_total_by_dynasty(self):
        row = ArticleService.get_article_total_by_dynasty()
        print(row)

        row = ArticleService.get_article_total_by_dynasty(1)
        print(row)