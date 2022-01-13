#!/usr/bin/python3
from db import Database
class Database(db.Model):
    TABLE = 'database'
    DB_SCHEMA = {
        'db_name': './perfd.db',
        'tables': [
            {
                'name': TABLE,
                'fields': {
                    'perf_name': 'text',
                    'name_obj_file': 'text',
                    'amount_of_samples': 'int'
                },
            }
        ]
    }
    VALIDATE_WRITE = True