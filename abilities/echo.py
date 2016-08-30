
#dict_ref = who, where, data, conn, bot
def echo(dictRef):
    data = dictRef['data'].split(' ', 2)
    if(len(data) < 3):
        dictRef['bot'].talk(dictRef['where'], 'Nothing to echo')
    else:
        data = data[2]
        dictRef['bot'].talk(dictRef['where'], data)

