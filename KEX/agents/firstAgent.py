import inspect
from pprint import pprint   # For pretty-printing 
from pathlib import Path

from CybORG import CybORG
from CybORG.Agents import *          # type: ignore
from CybORG.Shared.Actions import *  # type: ignore

cyborgRoot = Path(inspect.getfile(CybORG)).parent
path = cyborgRoot/ "Shared" / "Scenarios" / "Scenario2.yaml"   # We will only use Scenario2 (10 levels)

env = CybORG(str(path), "sim")

results = env.reset(agent="Red")
obs = results.observation
#pprint(obs)

#actionSpace = results.action_space
#print(list(actionSpace.keys()))

