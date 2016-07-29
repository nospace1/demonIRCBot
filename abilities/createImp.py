import bots
import abilityhandler

def createImp(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], "I need a name!")
    else:
        botName = data[2]
        if(len(botName) < 15):
            imp = bots.Bot(name=botName, \
                thrId=botName, \
                ablBits= \
                (abilityhandler.Abilities().getAbilValByName('echo') | \
                abilityhandler.Abilities().getAbilValByName('suicide') | \
                abilityhandler.Abilities().getAbilValByName('identify') | \
                abilityhandler.Abilities().getAbilValByName('github') | \
                abilityhandler.Abilities().getAbilValByName('join')), \
                channels=dictRef['where'])
            dictRef['bot'].lessers.append(imp) #adds actual bot to list of original bots
            imp.IRCOwners.append(dictRef['who']) #
            imp.greaters.append(dictRef['bot']) #adds creator bot to list of greaters
            # Removes duplicates irc owners
            for ircowner in dictRef['bot'].IRCOwners:
                imp.IRCOwners = list(set(dictRef['bot'].IRCOwners) | set(imp.IRCOwners))
            # adds all bot owners into a list aka greaters
            for great in dictRef['bot'].greaters:
                imp.greaters = list(set(dictRef['bot'].greaters) | set(imp.greaters))
            imp.start()
        else:
            dictRef['bot'].talk(dictRef['where'], "Name too long")
