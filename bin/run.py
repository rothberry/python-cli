from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd + "/config")

from environment import *

os.system('cls||clear')
print("STARTING CLI...")


# donki_api = API(NASA_BASE_URL, DONKI_ROUTES, config("NASA_API_KEY"))

# donki_query_params = {
#     "startDate": "2022-05-10",
#     "endDate": "2022-05-18"
# }

# donki_api.get_request(donki_query_params)

cli = CLI()
cli.start()






# breakpoint()