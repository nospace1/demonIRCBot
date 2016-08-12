from .echo import *
from .join import *
from .suicide import *
from .addOwner import *
from .telephone import *
from .createImp import *
from .identify import *
from .teach import *
from .github import *
from .rampage import *
from .leave import *
from .yell import *
from .createswarm import *
from .broadcast import *
from .becomeswarm import *
from .timedevent import *
from .repeat import *
#from .help import *

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
        'timedevent':       0b00000000000000000000000000000010,
        'repeat':           0b00000000000000000000000000000100, #workers are for specific tasks then die
        'createimp':        0b00000000000000000000000000001000, #lowered permissions and unique controller
#        'smite':            0b00000000000000000000000000010000, #demon kills a bot, aka sends it a pm to suicide
#        'kick':             0b00000000000000000000000000100000,
#        'asciiSwarm':       0b00000000000000000000000001000000, #demon creates ascii art using workers
        'join':             0b00000000000000000000000010000000,
        'leave':            0b00000000000000000000000100000000, #leaves a channel
        'yell':             0b00000000000000000000001000000000, #like echo but does it to all buffers that it is in
        'becomeswarm':      0b00000000000000000000010000000000, #gets information about demonite (owner, buffers, alias, etc)
        'teach':            0b00000000000000000000100000000000, #abilities can only be added by an ownerbot, and the owner must already know that ability
#        'createsuperswarm':          0b00000000000000000001000000000000, #uses processes to exceed the thread limit
        'suicide':          0b00000000000000000010000000000000, #bot kills itself
        'rampage':          0b00000000000000000100000000000000, #greater kills all its lessers
        'broadcast':        0b00000000000000001000000000000000, # tells what abilities bot has
        'addowner':         0b00000000000000010000000000000000, # tells what abilities bot has
#        'removeOwner':      0b00000000000000100000000000000000, # tells what abilities bot has
        'telephone':        0b00000000000001000000000000000000,
        'identify':         0b00000000000010000000000000000000, #displays information about the bot
        'github':           0b00000000000100000000000000000000, #prints a link to the github :D
        'createswarm':      0b00000000001000000000000000000000, #creates a swarm!!
        'help':             0b00000000010000000000000000000000, #creates a swarm!!
#        'spam':             0b00000000010000000000000000000000, #pulls random spam line from file
#        'macro':             0b00000000010000000000000000000000, #macros are a defined ability created from a collection of other abilities
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
        'rampage': rampage,
        'leave': leave,
        'yell': yell,
        'broadcast': broadcast,
        'becomeswarm': becomeswarm,
        'createswarm': createswarm,
        'timedevent': timedevent,
        'repeat': repeat,
        'help': help,
#        'spam': spam,
        }

    def abilityExists(self, name):
        return name in self.abilityPermissions

    def getAbilValByName(self, name):
        return self.abilityPermissions[name]

    #does a reverse search, taken from stackoverflow answer
    def getAbilNameByVal(self, value):
        rev_dict = dict((v,k) for k,v in self.abilityList.iteritems())
        return rev_dict[value]



