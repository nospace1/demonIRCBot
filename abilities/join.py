

def join(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'Nothing to join')
    else:
        data = data[2]
        if(data.startswith('#')):
            dictRef['bot'].joinChan(data)
            dictRef['bot'].channels.append(data)
        else:
            dictRef['bot'].talk(dictRef['where'], 'Bad channel name')
