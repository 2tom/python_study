# coding: utf-8

import json

data = {'spam': 'SPAM', 'ham': True, 'eggs': None}

print data

print json.dumps(data)
