

#demon repeat 5 timedevent 2 echo hi
def repeat(dictRef):
    bot = dictRef['bot']
    data = dictRef['data'].split(' ', 3)
    times = data[2]
    ability = data[3].split(' ')[0]
    dictRef['data'] = data[0] + ' ' + data[3]
    for i in xrange(int(times)):
        print("attempting ability: " + ability)
        print("with data: " + dictRef['data'])
        bot.performAbility(ability, dictRef)

