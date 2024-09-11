import random

JSON_TEMPLATE = '''{
    "name": "",
    "email": "",
    "tel": "",
    "urls": [],
    "image": "",
    "summary": "",
    "skills": [{"key": "", "value": ""}],
    "experience": [{
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
    }],
    "education": [{
        "entity": "",
        "location": "",
        "discipline": "",
        "degree": ""
    }]
}'''


content_types = {
    'pdf': 'application/pdf',
    'txt': 'text/plain; charset=utf-8',
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

def max_column_length(array, col):
    return max([len(row[col]) for row in array])

