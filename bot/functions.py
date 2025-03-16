import requests
import json
import utils

def getWorldState(platform = 'pc', language = 'en'):
    res = requests.get(f'https://api.warframestat.us/{platform}?language={language}', 
                   headers={'Content type':'application/json'})
    return json.loads(res.text)

def getDuviriCycle(worldState):
    worldStateDuviri = worldState['duviriCycle']
    #get all the strings needed from dictionary with world state
    kullervoState = ['anger', 'sorrow', 'fear']
    normalChoices = ', '.join(worldStateDuviri['choices'][0]['choices'])
    hardChoices = ', '.join(worldStateDuviri['choices'][1]['choices'])
    diff = utils.getTimeDelta(worldStateDuviri['expiry'])

    res = f'> **{worldStateDuviri['state'].upper()}**, expires in {diff['hours']}h {diff['minutes']}m\n'
    if worldStateDuviri['state'] in kullervoState:
        res += '> **Kullervo spawned**\n'
    res += f'> Warframes: {normalChoices}\n> Incarnons: {hardChoices}'
    
    return res

def getCetusCycle(worldState):
    worldStateCetus = worldState['cetusCycle']
    res = f'> **{worldStateCetus['state'].capitalize()}**, {worldStateCetus['shortString']}'
    return res

def getEarthCycle(worldState):
    worldStateEarth = worldState['earthCycle']
    nextState = 'day' if worldStateEarth['state'] == 'night' else 'night'
    res = f'> **{worldStateEarth['state'].capitalize()}**, {nextState} in {worldStateEarth['timeLeft']}'
    return res

def getCambionCycle(worldState):
    worldStateCambion = worldState['cambionCycle']
    nextState = 'vome' if worldStateCambion['state'] == 'fass' else 'fass'
    res = f'> **{worldStateCambion['state'].capitalize()}**, {nextState} in {worldStateCambion['timeLeft']}'
    return res

def getVallisCycle(worldState):
    worldStateVallis = worldState['vallisCycle']
    res = f'> **{worldStateVallis['state'].capitalize()}**, {worldStateVallis['shortString']}'
    return res

def getZarimanCycle(worldState):
    worldStateZariman = worldState['zarimanCycle']
    res = f'> **{worldStateZariman['state'].capitalize()}, {worldStateZariman['shortString']}'
    return res


def getFissures(fissures, *args):
    procArgs = utils.collectionToLower(args[0])
    if procArgs:
        fissures = [f for f in fissures if f['tier'].casefold() in procArgs]
    fissures.sort(key= lambda elm: elm['tier'])
    res1 = ''
    res2 = ''
    half = len(fissures)//2
    for i in range(len(fissures)):
        fissure = fissures[i]
        diff = utils.getTimeDelta(fissure['expiry'])
        s = f'> {fissure['tier']}; **{fissure['missionType']}** on {fissure['node']}, expires in {diff['hours']}h {diff['minutes']}m\n'
        if (procArgs != None) and (str(fissure['tier']).casefold() not in procArgs):
            continue

        if i <= half:
            res1+= s
        else:
            res2+= s
    
    return res1, res2

def getSortie(worldState, verbose=False):
    k = 0
    worldStateSortie = worldState['sortie']
    diff = utils.getTimeDelta(worldStateSortie['expiry'])
    res = f'Sortie expires in {diff['days']} days, {diff['hours']}h {diff['minutes']}'
    for mission in worldStateSortie['variants']:
        k+=1
        if verbose:
            res += f'\n> {k}. **{mission['missionType']}** on {mission['node']} with {mission['modifier']}: {mission['modifierDescription']}'
        else:
            res += f'\n> {k}. **{mission['missionType']}** with {mission['modifier']}'
    return res

# worldState = getWorldState()
# print(worldState.keys())
# print('------')
# print(getFissures(worldState['fissures']))

