

# needs to kill all children to be able to die
def suicide(dictRef):
    bot = dictRef['bot']
    bot.talk(dictRef['where'], "I will be back...")

    if len(bot.lessers) > 0:
        for lesser in bot.lessers:
            lesser.kill()
    # NEED TO REMOVE FROM ITS MASTERS LIST!!!
    bot.kill()
