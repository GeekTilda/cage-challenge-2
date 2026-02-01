import inspect
from pprint import pprint   # For pretty-printing 
from pathlib import Path

from CybORG import CybORG
from CybORG.Agents import *          # type: ignore
from CybORG.Shared.Actions import *  # type: ignore

cyborgRoot = Path(inspect.getfile(CybORG)).parent
path = cyborgRoot/ "Shared" / "Scenarios" / "Scenario2.yaml"   # We will only use Scenario2 (10 levels)

env = CybORG(str(path), "sim", agents={"Red": B_lineAgent}) 

# Reset environment, get inital observation (Blue)
results = env.reset(agent="Blue")
obs = results.observation
actionSpace = results.action_space
agent = BlueReactRemoveAgent() # BlueMonitorAgent()

# Run for 20 steps
for step in range(20):
    action = agent.get_action(obs, action_space=actionSpace)
    results = env.step(agent="Blue", action=action)
    obs = results.observation
    reward = results.reward
    print("Step " + str(step) + ": " + str(reward))
