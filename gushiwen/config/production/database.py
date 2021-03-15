# -*- coding: utf-8 -*-

DB_CONFIG = {
    'scheme': 'sqlite',
    'database': '/tmp/data.db',  # Deta支持写入临时文件
    'pragmas': {
        'journal_mode': 'wal',
        'cache_size': -1 * 64000,  # 64MB
        'foreign_keys': 1,
        'ignore_check_constraints': 0,
        'synchronous': 0
    }
}
