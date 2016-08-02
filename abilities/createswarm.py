
def noExistingSwarm(origin):
    #CHECK EVERYWHERAJLEJ
    for less in origin.lessers:
        if less.isSwarm == True:
            return False
    for great in origin.greaters:
        if great.isSwarm == True:
            return False
    return True

def findSwarmBot(bot):
    for less in bot.lessers:
        if less.name == 'swarm':
            return less

def createswarm(dictRef):
    #led by a bot named swarm.
    #if another swarm is created it is appended a number aka swarm2
    #the syntax is as follows:
    #demon createswarm [number of bots in swarm] [bots names which are appended numbers 1-swarmsize]
    #all bots under the swarm are lessers
    #any command passed on to the swarm is sent to each bot instead
    if(noExistingSwarm(dictRef['bot'])):
        #dictRef has 'demon createswarm 10 name'
        origin = dictRef['bot']
        data = dictRef['data'].split(' ', 4)
        if(len(data) < 3):
            size = 10
        else:
            if(data[2].isdigit()):
                size = int(data[2])
                if size < 31:
                    if(len(data) < 4):
                        swarmlingNames = 'imp'
                    else:
                        swarmlingNames = data[3]
                    if(len(swarmlingNames) < 7):

                        #first createimp called swarm
                        swarmRef = dictRef
                        swarmRef['data'] = '{n} createimp {s}'.format(n=dictRef['bot'].name, s='swarm')
                        origin.performAbility('createimp', swarmRef)
                        #then createimp x times with swarm
                        swarmlingRef = swarmRef
                        swarmlingRef['bot'] = findSwarmBot(origin)
                        for x in xrange(size):
                            swarmlingRef['data'] = '{n} createimp {s}'.format(n='swarm', s=swarmlingNames+str(x+1))
                            swarmlingRef['bot'].performAbility('createimp', swarmlingRef)

                        #then set variable
                        swarmlingRef['bot'].isSwarm = True
                    else:
                        dictRef['bot'].talk(dictRef['where'], "Too large of swarmling name, needs to be 6 or less ")
                else:
                    dictRef['bot'].talk(dictRef['where'], "Must be of size 30 or less")
            else:
                dictRef['bot'].talk(dictRef['where'], "{d} is not a number".format(d=data[2]))
    else:
        dictRef['bot'].talk(dictRef['where'], "There already exists a swarm")











