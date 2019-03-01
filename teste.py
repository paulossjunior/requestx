from requestx.RequestX import RequestX
from pprint import pprint
r = RequestX()
pprint (r.get('http://localhost:9093/projectteams'))
