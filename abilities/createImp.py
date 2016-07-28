import bots
from .abilityhandler import *

def createImp(dictRef):
    data = dictRef['data'].split(' ', 2)
    botName = data[2]
    #if dict['bot'].imps != None:
   # if botName not in dictRef['bot'].imps:
    if(dictRef['who'] == 'nospace!edarr@yakko.cs.wmich.edu'):
        dictRef['who'] = ''
    dictRef['bot'].imps = dictRef['bot'].imps + (botName,)
#        imp = bots.Bot(name=botName, thrId=botName, \
#                ablBits= \
#                (Abilities().getAbilValByName('echo') & \
#                Abilities().getAbilValByName('suicide')), \
#                owners='demon!demon@yakko.cs.wmich.edu' + dictRef['who'],)
    imp = bots.Bot(name=botName, thrId=botName, \
            ablBits=1,
            owner=('demon!demon@yakko.cs.wmich.edu', dictRef['who']),
            channels=dictRef['where'])
    imp.start()

