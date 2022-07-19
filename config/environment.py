# * Start out by bringing in the file locating pkgs
import os
import sys

# * Env only needs to bring in user made files
# os.system('cls||clear')

cwd = os.getcwd()
sys.path.append(cwd + "/config")
sys.path.append(cwd + "/lib")

# import services
# from services import *
from services.api import *
# from services.cli import *
# from models.asteroid import *
