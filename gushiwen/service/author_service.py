# -*- coding: utf-8 -*-

import unittest

from gushiwen.model import AuthorModel
from gushiwen.model.extension import to_dict


class AuthorService:
    """author"""

    @classmethod
    @to_dict
    def get_author_by_name(cls, name):
        return AuthorModel.select().where(AuthorModel.name == name).first()

    @classmethod
    @to_dict
    def get_authors(cls):
        return AuthorModel.select()

    @classmethod
    def get_total(cls)->int:
        return AuthorModel.select().count()

    @classmethod
    @to_dict
    def get_author(cls, uid):
        return AuthorModel.get_or_none(AuthorModel.id == uid)

    @classmethod
    @to_dict
    def create_author(cls, name, dynasty=None):
        return AuthorModel.create(name=name, dynasty=dynasty)

    @classmethod
    @to_dict
    def get_or_create(cls, name, dynasty=None):
        row, _ = AuthorModel.get_or_create(name=name, dynasty=dynasty)
        return row


class TestAuthorService(unittest.TestCase):
    """"""

    def test_get_author_by_name(self):
        row = AuthorService.get_author_by_name('李白')
        print(row)

        row = AuthorService.get_author_by_name('李贺')
        print(row)

    def test_get_authors(self):
        row = AuthorService.get_authors()
        print(row)

    def test_get_total(self):
        row = AuthorService.get_total()
        print(row)

    def test_get_author(self):
        row = AuthorService.get_author(1)
        print(row)