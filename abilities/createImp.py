import bots
import abilityhandler
#from .abilityhandler import *

def createImp(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        botName = dictRef['who']+'Imp'
    else:
        botName = data[2]
        #if dict['bot'].imps != None:
       # if botName not in dictRef['bot'].imps:
        if(dictRef['who'] == 'nospace!edarr@yakko.cs.wmich.edu'):
            dictRef['who'] = ''
        imp = bots.Bot(name=botName, \
            thrId=botName, \
            ablBits= \
            (abilityhandler.Abilities().getAbilValByName('echo') | \
            abilityhandler.Abilities().getAbilValByName('suicide') | \
            abilityhandler.Abilities().getAbilValByName('identify') | \
            abilityhandler.Abilities().getAbilValByName('github') | \
            abilityhandler.Abilities().getAbilValByName('join')), \
            owners='demon!demon@yakko.cs.wmich.edu' + dictRef['who'], \
            channels=dictRef['where'])
        dictRef['bot'].lessers.append(imp) #adds actual bot to list of original bots
        imp.start()

