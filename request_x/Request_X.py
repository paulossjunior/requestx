class Request_X (object):

    def __init__(self):
        self.headers_json = {'Content-type': 'application/json', 'Accept': 'application/json'}
        self.headers_uri_list = {'Content-type': 'text/uri-list', 'Accept': 'application/json'}

    def __post(self,data, url):
        response = requests.post(url,json=data,headers=self.headers_json)
        return response.json()

    def __get(self,url):
        response = requests.get(url,headers=self.headers_json)
        return response.json()
        
    def __put_uri_list (self,data, url):
        return response = requests.put(url, data=data,headers=self.headers_uri_list)
        return response.json()
    