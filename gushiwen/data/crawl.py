# -*- coding: utf-8 -*-

"""
获取古诗文网列表数据
eg: https://www.gushiwen.cn/
"""

from pprint import pprint

import requests
from parsel import Selector


def get_list_data(url, params=None):
    """
    :return: list
    """
    response = requests.get(url, params=params)

    sel = Selector(text=response.text)
    rows = sel.css(".main3 .left .sons")

    lst = []
    for row in rows:

        title = row.css("b::text").extract_first()
        author = row.css(".source a::text").extract()
        content = row.css(".contson").xpath("string(.)").extract_first()

        if not title:
            continue

        # 标题，作者，作者时代，内容
        item = {
            "title": title.strip(),
            "author": author[0].strip(),
            "dynasty": author[1].strip("〔〕").strip(),
            "content": content.replace('\n', ''),
        }

        lst.append(item)

    return lst


def get_list_data_for_page(page=1):
    """
    :param page: 目前可以获取页码： 1-10
    :return:
    """
    url = 'https://www.gushiwen.cn/default.aspx'
    params = {
        'page': page
    }
    return get_list_data(url, params)


if __name__ == '__main__':
    for row in get_list_data_for_page(1):
        pprint(row)
