

def github(dictRef):
    who = dictRef['who']
    who = who.split('!')[0]
    where = dictRef['where']
    bot = dictRef['bot']
    bot.talk(where, '{w}: https://github.com/nospace1/demonIRCBot' \
            .format(w=who))

