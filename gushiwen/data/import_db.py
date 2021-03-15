# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor

from gushiwen.data.crawl import get_list_data_for_page
from gushiwen.service import AuthorService, ArticleService
from gushiwen.service.dynasty_service import DynastyService

executor = ThreadPoolExecutor()


def import_data_to_db():
    """"""
    print('import_data_to_db')

    for page in range(1, 11):
        for row in get_list_data_for_page(page):
            dynasty = DynastyService.get_or_create(row['dynasty'])

            author = AuthorService.get_or_create(name=row['author'], dynasty=dynasty['id'])

            article = ArticleService.get_or_create(author_or_author_id=author['id'], title=row['title'],
                                                   content=row['content'])


def async_import_data_to_db():
    """异步执行数据抓取任务"""
    executor.submit(import_data_to_db)


if __name__ == '__main__':
    import_data_to_db()
