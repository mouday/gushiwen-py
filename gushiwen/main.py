# -*- coding: utf-8 -*-
from flask import Flask

from gushiwen import config
from gushiwen.data.import_db import async_import_data_to_db
from gushiwen.extension.scheduler import register_scheduler
from gushiwen.filters import register_filters
from gushiwen.model import register_database, db, tables
from gushiwen.view import register_blueprint

app = Flask(__name__)
app.config.from_object(config)

# 注册数据库
register_database(app)

# 注册路由
register_blueprint(app)

# 注册过滤器
register_filters(app)

# 注册定时任务
register_scheduler(app)


@app.before_first_request
def handle_before_first_request():
    db.create_tables(tables)
    async_import_data_to_db()


@app.before_request
def handle_before_request():
    # Deta部署的时候需要自动建表
    db.create_tables(tables)
