import fire
from .generator import gen


def create_tables():
    from gushiwen.model import db, tables
    db.create_tables(tables)


def drop_tables():
    from gushiwen.model import db, tables
    db.drop_tables(tables)


if __name__ == '__main__':
    fire.Fire()
