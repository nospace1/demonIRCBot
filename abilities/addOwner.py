

#todo: add look up based on nick

def addOwner(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'No owner specified')
    else:
        data = data[2]
        dictRef['bot'].owners.append(data)# = dictRef['bot'].owners + (data,)
        print(dictRef['bot'].owners)


