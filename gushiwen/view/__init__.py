# -*- coding: utf-8 -*-
from .index import index_app

ROUTERS = {
    '/': index_app
}


def register_blueprint(app):
    # 注册路由
    for router_url, router_app in ROUTERS.items():
        app.register_blueprint(blueprint=router_app, url_prefix=router_url)
