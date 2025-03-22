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
    res = f'> **{worldStateZariman['state'].capitalize()}**, {worldStateZariman['shortString']}'
    return res

def getFissures(fissures: list[dict], args: list[str] | None):
    procArgs = utils.collectionToLower(args)
    if procArgs:
        if procArgs[0] != 'help':
            fissures = [f for f in fissures if f['tier'].casefold() in procArgs]
        else:
            tierSet = set([f['tier'].casefold() for f in fissures])
            return f'Accepted arguments: {tierSet} (WIP for others)'
    
    fissures.sort(key= lambda elm: elm['tier'])
    res = ''
    for i in range(len(fissures)):
        fissure = fissures[i]
        diff = utils.getTimeDelta(fissure['expiry'])
        s = f'> {fissure['tier']}; **{fissure['missionType']}** on {fissure['node']}, expires in {diff['hours']}h {diff['minutes']}m\n'
        if (procArgs != None) and (str(fissure['tier']).casefold() not in procArgs):
            continue
        res += s
    return res

def getSortie(worldState, verbose=False):
    k = 0
    worldStateSortie = worldState['sortie']
    diff = utils.getTimeDelta(worldStateSortie['expiry'])
    res = f'Sortie expires in {diff['days']} days, {diff['hours']}h {diff['minutes']}m'
    for mission in worldStateSortie['variants']:
        k+=1
        if verbose:
            res += f'\n> {k}. **{mission['missionType']}** on {mission['node']} with {mission['modifier']}: {mission['modifierDescription']}'
        else:
            res += f'\n> {k}. **{mission['missionType']}** with {mission['modifier']}'
    return res

def getArchonHunt(worldState):
    k = 0
    worldStateArchonHunt = worldState['archonHunt']
    res = f'Archon Hunt expires in {worldStateArchonHunt['eta']}, Boss: **{worldStateArchonHunt['boss']}**'
    for mission in worldStateArchonHunt['missions']:
        k+=1
        res += f'\n> {k}. **{mission['type']}** on {mission['node']}'
    return res

def getVoidTrader(worldState):
    k = 0
    worldStateVoidTrader = worldState['voidTrader']
    res = f'Void Trader on **{worldStateVoidTrader['location']}**, leaves in {worldStateVoidTrader['endString']}'
    for item in worldStateVoidTrader['inventory']:
        k+=1
        res += f'\n> {k}. **{item['item']}** for {item['ducats']} ducats and {item['credits']} credits'
    return res

