import pp
import requests

class API:
    def __init__(self, base_url, routes, api_key=""):
        print("API init")
        self.base_url = base_url
        # routes as an array to create url routes
        self.routes = routes
        self.api_key = api_key
        
    def full_base_url(self, query_params):
        base = self.base_url + "/".join(self.routes) + "?api_key=" + self.api_key 
        if bool(query_params):
            str_params = ""
            for query in query_params:
                str_params += "&" + query + "=" + query_params[query]
            return base + str_params
        return base

    def get_request(self, query_params={}):
        resp = requests.get(self.full_base_url(query_params))
        # pp(self.full_base_url(query_params))
        better_resp = resp.json()
        pp(better_resp)
        return better_resp
