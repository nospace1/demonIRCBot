import abilityhandler

#return a list
def getAllAbilities(bot):
    abilitylist = []
    for ability, value in abilityhandler.Abilities().abilityPermissions.items():
        print(ability)
        print(value)
        if value & bot.abilityBits:
            abilitylist.append(ability)
    return abilitylist

def identify(dictRef):
    dictRef['bot'].talk(dictRef['where'], 'Name: {n}' \
            .format(n=dictRef['bot'].name))
    dictRef['bot'].talk(dictRef['where'], 'Owner(s): {o}' \
            .format(o=dictRef['bot'].owners))
    dictRef['bot'].talk(dictRef['where'], 'ThreadID: {t}' \
            .format(t=dictRef['bot'].threadID))
    dictRef['bot'].talk(dictRef['where'], 'Channels: {c}' \
            .format(c=dictRef['bot'].channels))
#    for ability in getAllAbilities(dictRef['bot']):
    dictRef['bot'].talk(dictRef['where'], 'Abilities: {a}' \
            .format(a=str(getAllAbilities(dictRef['bot']))))

