import requests as rq

impact_crendtials = ('superadmin', 'superadmin')
base_url = 'http://100.69.164.181:8380/rest'


response = rq.get( base_url+ '/device', auth=impact_crendtials, )

print(response.status_code)
print(response.json())

response_json = response.json()

print(response_json['aaData'][0]['id'])


