

#pretty much teh same as suicide but this bot doesn't
#kill itself at the end
def rampage(dictRef):
    bot = dictRef['bot']
    bot.talk(dictRef['where'], "DIE")

    while(len(bot.lessers) > 0):
        less = bot.lessers.pop()
        less.kill()

