import bots
import abilityhandler

def createImp(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        #botName = dictRef['who'].split('!')[0]+'Imp'
        dictRef['bot'].talk(dictRef['where'], "I need a name!")
    else:
        botName = data[2]
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
        imp.owners.append(dictRef['who'])
        for owner in dictRef['bot'].owners:
            imp.owners.append(owner)
        imp.start()

