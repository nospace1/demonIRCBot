import bots
import abilityhandler
#from .abilityhandler import *

def createImp(dictRef):
    data = dictRef['data'].split(' ', 2)
    botName = data[2]
    #if dict['bot'].imps != None:
   # if botName not in dictRef['bot'].imps:
    if(dictRef['who'] == 'nospace!edarr@yakko.cs.wmich.edu'):
        dictRef['who'] = ''
    dictRef['bot'].imps = dictRef['bot'].imps + (botName,)
    imp = bots.Bot(name=botName, \
        thrId=botName, \
        ablBits= \
        (abilityhandler.Abilities().getAbilValByName('echo') | \
        abilityhandler.Abilities().getAbilValByName('suicide') | \
        abilityhandler.Abilities().getAbilValByName('identify') | \
        abilityhandler.Abilities().getAbilValByName('join')), \
        owners='demon!demon@yakko.cs.wmich.edu' + dictRef['who'], \
        channels=dictRef['where'])
#    imp = bots.Bot(name=botName, thrId=botName, \
#            ablBits=1,
#            owner=('demon!demon@yakko.cs.wmich.edu', dictRef['who']),
#            channels=dictRef['where'])
    imp.start()
#    imp.join('#pit)

