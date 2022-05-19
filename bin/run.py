import os
import sys
# import requests
# from decouple import config
# import pp

cwd = os.getcwd()
sys.path.append(cwd + "/config")

from environment import *

os.system('cls||clear')
print("STARTING CLI...")

NASA_BASE_URL = 'https://api.nasa.gov/'
apod_api = API(NASA_BASE_URL, ["planetary", "apod"], config("NASA_API_KEY"))
# apod_api.full_base_url()
# apod_api.get_request()

donki_api = API(NASA_BASE_URL, ["DONKI", "CME"], config("NASA_API_KEY"))

donki_query_params = {
    "startDate": "2022-05-10",
    "endDate": "2022-05-18"
}

donki_api.get_request(donki_query_params)






breakpoint()