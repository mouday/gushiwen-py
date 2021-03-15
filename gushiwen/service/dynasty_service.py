# -*- coding: utf-8 -*-

import unittest
from typing import Dict, Optional, List

from gushiwen.model import DynastyModel
from gushiwen.model.extension import to_dict
from mo_cache import MemoryCache

cache = MemoryCache()


class DynastyService:
    """dynasty"""

    @classmethod
    def get_all_dynasties_map(cls) -> Dict:
        """
        :return: {id: name}
        """
        rows = DynastyModel.select()
        return dict([(row.id, row.name) for row in rows])

    @classmethod
    @to_dict
    def get_all_dynasties(cls) -> List:
        return DynastyModel.select(DynastyModel.id, DynastyModel.name)

    @classmethod
    @cache(expire=60 * 2)
    def get_all_dynasties_map_from_cache(cls) -> Dict:
        return cls.get_all_dynasties_map()

    @classmethod
    def get_dynasty_id_by_name_from_cache(cls, name) -> Optional[int]:
        mapping = cls.get_all_dynasties_map_from_cache()
        reversed_mapping = {v: k for k, v in mapping.items()}
        return reversed_mapping.get(name)

    @classmethod
    @to_dict
    def get_dynasty_by_name(cls, name) -> Dict:
        return DynastyModel.select().where(DynastyModel.name == name).first()

    @classmethod
    def get_dynasty_id_by_name(cls, name) -> Optional[int]:
        row = cls.get_dynasty_by_name(name)
        if row:
            return row['id']

    @classmethod
    @to_dict
    def create_dynasty(cls, name):
        return DynastyModel.create(name=name)

    @classmethod
    @to_dict
    def get_or_create(cls, name):
        row, _ = DynastyModel.get_or_create(name=name)
        return row


class TestDynastyService(unittest.TestCase):
    """"""

    def test_get_dynasty_by_name(self):
        row = DynastyService.get_dynasty_by_name('唐代')
        print(row)

    def test_get_dynasty_by_name_or_create(self):
        row = DynastyService.get_or_create('唐代')
        print(row)

    def test_get_all_dynasties(self):
        rows = DynastyService.get_all_dynasties()
        print(rows)

    def test_get_dynasty_id_by_name(self):
        row = DynastyService.get_dynasty_id_by_name('唐代')
        print(row)

    def test_get_all_dynasties_map(self):
        rows = DynastyService.get_all_dynasties_map()
        print(rows)

    def test_get_all_dynasties_map_from_cache(self):
        rows = DynastyService.get_all_dynasties_map_from_cache()
        print(rows)

        rows = DynastyService.get_all_dynasties_map_from_cache()
        print(rows)
