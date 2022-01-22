import requests
from json import dumps
from .config import config


class Api:

    def test(self):
        try:
            requests.get(config['API_ADDRESS'])
        except requests.exceptions.ConnectionError:
            return False
        return True

    def request(self, method, route="/", params=None, data=None):
        if params and data:
            data['key'] = {'key': config['API_KEY']}
            return requests.request(method, config['API_ADDRESS']+route, params=params, data=dumps(data))
        if data:
            data['key'] = {'key': config['API_KEY']}
            return requests.request(method, config['API_ADDRESS']+route, data=dumps(data))
        data = {'key': config['API_KEY']}
        if params:
            return requests.request(method, config['API_ADDRESS']+route, params=params, data=dumps(data))
        return requests.request(method, config['API_ADDRESS']+route, data=dumps(data))


api = Api()
