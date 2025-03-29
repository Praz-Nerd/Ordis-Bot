from functions import *
from api import API

worldState = getWorldState()
print(worldState.keys())
print('------')
print(worldState['invasions'])
print('------')
print(getVoidTrader(worldState), len(getVoidTrader(worldState)))