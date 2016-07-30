


#pretty much teh same as suicide but this bot doesn't
#kill itself at the end
def rampage(dictRef):
    bot = dictRef['bot']
    bot.talk(dictRef['where'], "DIE")

    for lesser in bot.lessers:
        if(lesser.allowedToLive == False):
            bot.lessers.remove(lesser)

    if len(bot.lessers) > 0:
        for lesser in bot.lessers:
            lesser.kill()


