

def telephone(dictRef):
    data = dictRef['data'].split(' ', 3)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'Who do I call?')
    if(len(data) < 4):
        dictRef['bot'].talk(dictRef['where'], 'What is the message?')
    else:
        print(data)
        target = data[2] #who it is directed to
        message = data[3]
        whoFrom = (dictRef['who'].split('!'))[0] #gets only the nick
        message = "{f} says: {m}".format(f=whoFrom, m=message)
        dictRef['bot'].talk(target, message)

