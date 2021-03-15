# -*- coding: utf-8 -*-

from gushiwen.main import app
from gushiwen.model import db, tables

# Deta部署的时候需要自动建表
db.create_tables(tables)

if __name__ == '__main__':
    app.run()
