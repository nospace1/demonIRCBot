from time import sleep
#0     1      2 3 4
#demon repeat 5 2 echo hi
def timerrepeat(dictRef):
    bot = dictRef['bot']
    data = dictRef['data'].split(' ', 4)
    times = data[2]
    duration = data[3]
    data = data[4]
    ability = data.split(' ')[0]
    newDictRef = dict(dictRef)
    newDictRef['data'] = data[0] + ' ' + data
    for i in xrange(int(times)):
        bot.performAbility(ability, newDictRef)
        sleep(float(duration))


