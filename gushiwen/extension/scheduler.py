# -*- coding: utf-8 -*-
from flask_apscheduler import APScheduler


def register_scheduler(app):
    # 定时任务
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
