

# needs to kill all children to be able to die
def suicide(dictRef):
    bot = dictRef['bot']
    bot.talk(dictRef['where'], "I will be back...")

    for lesser in bot.lessers:
        if(lesser.allowedToLive == False):
            bot.lessers.remove(lesser)

    if len(bot.lessers) > 0:
        for lesser in bot.lessers:
            lesser.kill()

    bot.kill()
