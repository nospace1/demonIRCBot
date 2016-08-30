
#demon repeat 5 timedevent 2 echo hi
def repeat(dictRef):
    bot = dictRef['bot']
    data = dictRef['data'].split(' ', 3)
    times = data[2]
    ability = data[3].split(' ')[0]
    newDictRef = dict(dictRef)
    newDictRef['data'] = data[0] + ' ' + data[3]
    for i in xrange(int(times)):
        print("attempting ability: " + ability)
        print("with data: " + newDictRef['data'])
        bot.performAbility(ability, newDictRef)


