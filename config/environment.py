# * Start out by bringing in the file locating pkgs
import os
import sys

# * Env only needs to bring in user made files
# os.system('cls||clear')

cwd = os.getcwd()
sys.path.append(cwd + "/lib/models")

from api import *
from cli import *
from asteroid import *