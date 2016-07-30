import abilityhandler

#return a list
def getAllAbilities(bot):
    abilitylist = []
    for ability, value in abilityhandler.Abilities().abilityPermissions.items():
        if value & bot.abilityBits:
            abilitylist.append(ability)
    return abilitylist

def getLesserNameList(lesserlist):
    lesserNames = []
    for less in lesserlist:
        lesserNames.append(less.name)
    return lesserNames

def getGreaterNameList(greaterlist):
    greaterNames = []
    for great in greaterlist:
        greaterNames.append(great.name)
    return greaterNames

def identify(dictRef):
    dictRef['bot'].talk(dictRef['where'], 'Name: {n}' \
            .format(n=dictRef['bot'].name))
    dictRef['bot'].talk(dictRef['where'], 'Owner(s): {o}' \
            .format(o=dictRef['bot'].IRCOwners))
    dictRef['bot'].talk(dictRef['where'], 'ThreadID: {t}' \
            .format(t=dictRef['bot'].threadID))
    dictRef['bot'].talk(dictRef['where'], 'Channels: {c}' \
            .format(c=dictRef['bot'].channels))
    dictRef['bot'].talk(dictRef['where'], 'Abilities: {a}' \
            .format(a=str(getAllAbilities(dictRef['bot']))))
    dictRef['bot'].talk(dictRef['where'], 'Lessers: {l}' \
                .format(l=str(getLesserNameList(dictRef['bot'].lessers))))
    dictRef['bot'].talk(dictRef['where'], 'Greaters: {g}' \
                .format(g=str(getGreaterNameList(dictRef['bot'].greaters))))


