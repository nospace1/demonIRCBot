

def leave(dictRef):
    data = dictRef['data'].split(' ', 2)
    bot = dictRef['bot']
    if(len(data) > 2):
        specChan = data[2]
        bot.leave(specChan)
        bot.channels.remove(specChan)
    else:
        bot.leave(dictRef['where'])
        bot.channels.remove(dictRef['where'])

