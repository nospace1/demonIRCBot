
from time import sleep


#take in how long in seconds to wait then function and args
#demon timedevent 20 echo hi
def timedevent(dictRef):
    print("in timedevent with data: " + dictRef['data'])
    bot = dictRef['bot']
    data = dictRef['data'].split(' ', 3)
    #doing this makes it a copy rather than a reference
    #to the same object, therefore we can modify values
    newDictRef = dict(dictRef)
    duration = data[2]
    ability = data[3].split(' ')[0]
    abilityData = data[0] + ' ' + data[3]
    sleep(float(duration))
    newDictRef['data'] = abilityData
    bot.performAbility(ability, newDictRef)



