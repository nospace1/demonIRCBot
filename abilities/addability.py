
#probably need to rmove this ability it's not useful I don't think
#will replace with ability "teach"
import abilityhandler

def addAbility(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'No ability specified')
    else:
        ability = data[2]
        dictRef['bot'].abilityBits = \
        dictRef['bot'].abilityBits | abilityhandler.Abilities().getAbilValByName(ability)
        print('{n} learned ability {a}'.format(n=dictRef['bot'].name, a=ability))


