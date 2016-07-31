

# needs to kill all children to be able to die
def suicide(dictRef):
    bot = dictRef['bot']
    bot.talk(dictRef['where'], "I will be back...")

    while(len(bot.lessers) > 0):
        less = bot.lessers.pop()
        less.kill()

    bot.kill()
