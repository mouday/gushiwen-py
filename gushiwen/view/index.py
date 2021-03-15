# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, request

from gushiwen.data.import_db import import_data_to_db, async_import_data_to_db
from gushiwen.service import ArticleService, DynastyService, AuthorService

index_app = Blueprint(name="app", import_name=__name__)


@index_app.route('/')
def index():
    data = {
        'list': ArticleService.get_articles(),
        'total': ArticleService.get_article_total()
    }

    return render_template('index.html', **data)


@index_app.route('/detail/<int:uid>')
def detail(uid):
    data = {
        'detail': ArticleService.get_article_with_author(uid),
    }

    return render_template('detail.html', **data)


@index_app.route('/dynasty')
def dynasty():
    dynasty_id = request.args.get('dynasty_id', '')

    dynasty_rows = DynastyService.get_all_dynasties()

    dynasty_rows.insert(0, {'name': '全部', 'id': ''})

    data = {
        'dynasty_rows': dynasty_rows,
        'dynasty_id': dynasty_id,
        'list': ArticleService.get_articles(dynasty_id=dynasty_id),
        'total': ArticleService.get_article_total_by_dynasty(dynasty_id)
    }

    return render_template('dynasty.html', **data)


@index_app.route('/authors')
def authors():
    data = {
        'author_rows': AuthorService.get_authors(),
        'total': AuthorService.get_total()
    }

    return render_template('authors.html', **data)


@index_app.route('/author/<int:author_id>')
def author(author_id):
    author = AuthorService.get_author(author_id)

    data = {
        'author': author,
        'list': ArticleService.get_articles(author_id=author_id),
        'total': ArticleService.get_article_total_by_author(author_id)
    }

    return render_template('author.html', **data)


@index_app.route('/update-data')
def update_data():
    async_import_data_to_db()
    return {'result': '后台更新已启动'}
