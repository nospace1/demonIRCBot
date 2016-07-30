from .echo import *
from .join import *
from .suicide import *
from .addOwner import *
from .telephone import *
from .createImp import *
from .identify import *
from .teach import *
from .github import *

__all__ = ['Ability', 'Abilities']
class Ability:

    def __init__(self, name, args):
        self.name = name
        self.args = args

    def execute(self):
        Abilities.abilityFuncRef[self.name](self.args)

class Abilities:
    abilityPermissions = {
        'echo':             0b00000000000000000000000000000001,
#        'timedEvent':       0b00000000000000000000000000000010,
#        'createWorker':     0b00000000000000000000000000000100, #workers are for specific tasks then die
        'createimp':        0b00000000000000000000000000001000, #lowered permissions and unique controller
#        'smite':            0b00000000000000000000000000010000, #demon kills a bot, aka sends it a pm to suicide
#        'kick':             0b00000000000000000000000000100000,
#        'asciiSwarm':       0b00000000000000000000000001000000, #demon creates ascii art using workers
        'join':             0b00000000000000000000000010000000,
#        'leave':            0b00000000000000000000000100000000, #leaves a channel
#        'yell':             0b00000000000000000000001000000000, #like echo but does it to all buffers that it is in
#        'inspectImp':       0b00000000000000000000010000000000, #gets information about demonite (owner, buffers, alias, etc)
        'teach':            0b00000000000000000000100000000000, #abilities can only be added by an ownerbot, and the owner must already know that ability
#        'killAll':          0b00000000000000000001000000000000, #kills all bots including demon, probably will not make this
        'suicide':          0b00000000000000000010000000000000, #bot kills itself
#        'rampage':          0b00000000000000000100000000000000, #demon kills all bots but itself
#        'abilityList':      0b00000000000000001000000000000000, # tells what abilities bot has
        'addowner':         0b00000000000000010000000000000000, # tells what abilities bot has
#        'removeOwner':      0b00000000000000100000000000000000, # tells what abilities bot has
        'telephone':        0b00000000000001000000000000000000,
        'identify':         0b00000000000010000000000000000000, #displays information about the bot
        'github':           0b00000000000100000000000000000000, #prints a link to the github :D
        }

    abilityFuncRef = {
        'echo': echo,
        'join': join,
        'suicide': suicide,
        'addowner': addOwner,
        'telephone': telephone,
        'createimp': createImp,
        'identify': identify,
        'github': github,
        'teach': teach,
        }

    def abilityExists(self, name):
        return name in self.abilityPermissions

    def getAbilValByName(self, name):
        return self.abilityPermissions[name]

    #does a reverse search, taken from stackoverflow answer
    def getAbilNameByVal(self, value):
        rev_dict = dict((v,k) for k,v in self.abilityList.iteritems())
        return rev_dict[value]



