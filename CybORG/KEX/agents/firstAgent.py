import inspect
from pprint import pprint   # For pretty-printing 

from CybORG import CybORG
from CybORG.Agents import *
from CybORG.Shared.Actions import * 

path = str(inspect.getfile(CybORG))
path = path[:-10] + 'Shared/Scenarios/Scenario2.yaml'