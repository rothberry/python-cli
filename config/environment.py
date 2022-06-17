import os
import sys
import requests
from decouple import config
import pp

cwd = os.getcwd()
sys.path.append(cwd + "/config")
sys.path.append(cwd + "/lib")

# import services
# from services import *
from services.api import *
# from services.cli import *
# from models.asteroid import *