import os
import sys

cwd = os.getcwd()
sys.path.append(cwd + "/config")
sys.path.append(cwd + "/lib/models")

from api import *