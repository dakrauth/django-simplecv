import os
import json
import random
from datetime import datetime
from django.conf import settings

JSON_TEMPLATE = '''{
    "name": "",
    "email": "",
    "url": "",
    "tel": "",
    "image": "",
    "summary": "",
    "skills": [{"key": "", "value": ""}],
    "experience": [
        {
            "org": "",
            "location": "",
            "positions": [
                {
                    "period": {"from": "", "to": ""},
                    "title": "",
                    "description": "",
                    "achievements": []
                }
            ]
        }
    ],
    "education": [
        {
            "entity": "",
            "location": "",
            "discipline": "",
            "degree": ""
        }
    ]
}'''


content_types = {
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'docx': (
        'application/'
        'vnd.openxmlformats-officedocument.wordprocessingml.document'
    ),
    'html': None
}


def int_entity(c):
    return '&#{};'.format(ord(c))


def hex_entity(c):
    return '&#x{:x};'.format(ord(c))


def mangle(s):
    funcs = [str, int_entity, hex_entity]
    s = ''.join([random.choice(funcs)(c) for c in s])
    return s.replace('@', hex_entity('@'))


def load_cv(filename=None, mangle_email=False):
    filename = filename or settings.SIMPLECV_FILENAME
    st = os.stat(filename)
    with open(filename) as fp:
        cv = json.load(fp)
    cv['last_mod'] = datetime.fromtimestamp(st.st_mtime).strftime('%A, %b %d, %Y %I:%M%p')
    if mangle_email:
        cv['email'] = mangle(cv['email'])
    
    return cv


def max_column_length(array, col):
    return max([len(row[col]) for row in array])

