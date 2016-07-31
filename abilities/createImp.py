import bots
import abilityhandler

#all the greaters of this imp need to have
#this imp as a lesser
#this works becaues for each greater
#there is a lesser relationship
def updateLessersInGreaters(imp):
    for great in imp.greaters:
        if imp not in great.lessers:
            great.lessers.append(imp)

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
                abilityhandler.Abilities().getAbilValByName('rampage') | \
                abilityhandler.Abilities().getAbilValByName('createimp') | \
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
            #update the lessers of the greaters to include new imp
            updateLessersInGreaters(imp)
            #imp.channels.append(dictRef['where'])
            imp.start()
        else:
            dictRef['bot'].talk(dictRef['where'], "Name too long")


