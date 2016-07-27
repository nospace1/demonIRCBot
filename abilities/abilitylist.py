

class Abilities:
    abilityList = {
        'echo':             0b00000000000000000000000000000001,
        'timedEvent':       0b00000000000000000000000000000010,
        'createWorker':     0b00000000000000000000000000000100, #workers are for specific tasks then die
        'createDemonite':   0b00000000000000000000000000001000, #lowered permissions and unique controller
        'smite':            0b00000000000000000000000000010000, #demon kills a bot
        'kick':             0b00000000000000000000000000100000,
        'asciiSwarm':       0b00000000000000000000000001000000, #demon creates ascii art using workers
        'join':             0b00000000000000000000000010000000,
        'part':             0b00000000000000000000000100000000, #leaves a channel
        'broadcast':        0b00000000000000000000001000000000, #like echo but does it to all buffers that it is in
        'inspectDemonite':  0b00000000000000000000010000000000, #gets information about demonite (owner, buffers, alias, etc)
        'addAbility':       0b00000000000000000000100000000000, #abilities can only be added by another bot.
        'killAll':          0b00000000000000000001000000000000, #kills all bots including demon
        'suicide':          0b00000000000000000010000000000000, #bot kills itself
        'rampage':          0b00000000000000000100000000000000, #demon kills all bots but itself
        'abilityList':      0b00000000000000001000000000000000, # tells what abilities bot has


        }

    def abilityExists(self, name):
        return name in self.abilityList

    def getAbilValByName(self, name):
        return self.abilityList[name]

    #does a reverse search, taken from stackoverflow answer
    def getAbilNameByVal(self, value):
        rev_dict = dict((v,k) for k,v in self.abilityList.iteritems())
        return rev_dict[value]





