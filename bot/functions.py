import requests
import json
import utils

def getWorldState(platform = 'pc', language = 'en'):
    res = requests.get(f'https://api.warframestat.us/{platform}?language={language}', 
                   headers={'Content type':'application/json'})
    return json.loads(res.text)

def getDuviriCycle(worldStateDuviri, verbose = False):
    #get all the strings needed from dictionary with world state
    kullervoState = ['anger', 'sorrow', 'fear']
    expiry = worldStateDuviri['expiry']
    state = worldStateDuviri['state']
    normalChoices = ', '.join(worldStateDuviri['choices'][0]['choices'])
    hardChoices = ', '.join(worldStateDuviri['choices'][1]['choices'])
    diff = utils.getTimeDelta(expiry)

    res = f'Duviri cycle: {state}, expires in {diff['hours']}h {diff['minutes']}m'
    if state in kullervoState:
        res += '\nKullervo spawned'
    if verbose:
        res += f'\nWarframes: {normalChoices}\nIncarnons: {hardChoices}'
    
    return res
    
