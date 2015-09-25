# coding: utf-8

import requests

r = requests.get('http://connpass.com/api/v1/event/?keyword=python')
print r.status_code, r.headers['content-type']

for event in r.json()['events'][:3]:
	print event ['title'], event['started_at']
