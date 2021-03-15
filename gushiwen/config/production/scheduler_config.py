# -*- coding: utf-8 -*-

JOBS = [
    {
        'id': 'import_data_to_db',
        'func': 'gushiwen.data.import_db:import_data_to_db',
        'trigger': 'interval',
        'seconds': 60 * 10
    }
]
