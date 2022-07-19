# * Apparently need to import all used pkgs at the top of each file
import pp
import requests
from decouple import config


class API:
    NASA_BASE_URL = 'https://api.nasa.gov/'
    APOD_ROUTES = ("planetary", "apod")
    DONKI_ROUTES = ("DONKI", "CME")


    def __init__(self, api_select):
        # * Start off by assigning the initial args as instance variables
        print("API init")
        # self.base_url = NASA_BASE
        # self.routes = routes
        self.api_key = config("NASA_API_KEY")
        if (api_select == "apod"):
            self.routes = self.APOD_ROUTES
        elif (api_select == 'donki'):
            self.routes = self.DONKI_ROUTES            
        
    def full_base_url(self, query_params={}):
        # * To create the full url to send to NASA
        base = self.NASA_BASE_URL + "/".join(self.routes) + "?api_key=" + self.api_key 
        # * If there are query params, add them to the end of the url
        # * ex: ....&api_key=ahdjk&start_date=11-11-2011&end_date=....
        if bool(query_params):
            str_params = ""
            for query in query_params:
                str_params += "&" + query + "=" + query_params[query]
            return base + str_params
        return base

    def get_request(self, query_params={}):
        # * send get req
        resp = requests.get(self.full_base_url(query_params))
        # pp(self.full_base_url(query_params))
        # * parse to json
        better_resp = resp.json()
        # pp(better_resp)
        return better_resp

    # @classmethod
    # def send_full_apod_request():
