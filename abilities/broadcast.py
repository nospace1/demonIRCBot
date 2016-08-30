

def broadcast(dictRef):
    data = dictRef['data'].split(' ')
    ability = data[1]
    print('attempting to broadcast ability: ' + ability)
    print('with data: ' + str(dictRef))
    #swarm performs the ability
    dictRef['bot'].performAbility(ability, dictRef)
    for less in dictRef['bot'].lessers:
        dictRef['bot'] = less
        less.performAbility(ability, dictRef)


