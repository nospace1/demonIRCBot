
import bots
#import connection
#import abilities


def createswarm(dictRef):
    #led by a bot named swarm.
    #if another swarm is created it is appended a number aka swarm2
    #the syntax is as follows:
    #demon createswarm [number of bots in swarm] [bots names which are appended numbers 1-swarmsize]
    #all bots under the swarm are lessers
    #any command passed on to the swarm is sent to each bot instead

    #dictRef has demon createswarm 10 name
    swarm = bots.Swarm(dictRef)
    swarm.start()












