import os
import sys
import requests
from decouple import config
import pp

cwd = os.getcwd()
sys.path.append(cwd + "/config")
sys.path.append(cwd + "/lib/models")
sys.path.append(cwd + "/lib/services")

from api import *