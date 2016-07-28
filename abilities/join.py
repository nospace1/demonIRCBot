

def join(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'Nothing to join')
    else:
        data = data[2]
        dictRef['bot'].joinChan(data)
