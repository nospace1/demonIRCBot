import abilityhandler


#demon help ability jibberish
def help(dictRef):
    """
    Returns information on specified ability
    """
    data = dictRef['data'].split(' ')
    if(len(data) > 2):
        ability = dictRef['data'].split(' ')[2]
        if(ability not in abilityhandler.Abilities.abilityFuncRef):
            dictRef['bot'].talk(dictRef['where'], 'Unrecognized ability')
        else:
            ab = abilityhandler.Abilities.abilityFuncRef[ability].__doc__
            if ab != None:
                dictRef['bot'].talk(dictRef['where'], ab.strip())
            else:
                dictRef['bot'].talk(dictRef['where'], "I'm lazy and haven't documented this yet")
    else:
        dictRef['bot'].talk(dictRef['where'], 'No ability specified')


