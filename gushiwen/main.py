# -*- coding: utf-8 -*-
from flask import Flask
from flask_apscheduler import APScheduler
from playhouse.flask_utils import FlaskDB

from gushiwen import config
from gushiwen.data.import_db import async_import_data_to_db
from gushiwen.filters import register_filters
from gushiwen.model.database import db
from gushiwen.view import register_blueprint

app = Flask(__name__)
app.config.from_object(config)

FlaskDB(app=app, database=db)

# 注册路由
register_blueprint(app)

# 注册过滤器
register_filters(app)

# 定时任务
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.before_first_request
def handle_before_first_request():
    async_import_data_to_db()
