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
    expiry = worldStateDuviri['expiry']
    state = worldStateDuviri['state']
    normalChoices = ', '.join(worldStateDuviri['choices'][0]['choices'])
    hardChoices = ', '.join(worldStateDuviri['choices'][1]['choices'])
    diff = utils.getTimeDelta(expiry)

    res = f'Duviri Cycle: {state}, expires in {diff['hours']}h {diff['minutes']}m'
    if state in kullervoState:
        res += '\nKullervo spawned'
    res += f'\nWarframes: {normalChoices}\nIncarnons: {hardChoices}'
    
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
        s = f'> {fissure['tier']}; **{fissure['missionType']}** on {fissure['node']}; Faction: {fissure['enemy']}\n'
        if (procArgs != None) and (str(fissure['tier']).casefold() not in procArgs):
            continue

        if i <= half:
            res1+= s
        else:
            res2+= s
    
    return res1, res2

# worldState = getWorldState()
# print(worldState.keys())
# print('------')
# print(getFissures(worldState['fissures']))

