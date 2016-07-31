

def yell(dictRef):
    bot = dictRef['bot']
    data = dictRef['data'].split(' ', 2)
    message = data[2]

    for ch in bot.channels:
        bot.talk(ch, message.upper())
