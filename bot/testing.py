from functions import *
from api import API

worldState = getWorldState()
print(worldState.keys())
print('------')
print(worldState['voidTrader'])
print('------')
print(getVoidTrader(worldState), len(getVoidTrader(worldState)))