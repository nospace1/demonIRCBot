#!/usr/bin/env python

from connection import *
from messages import *
import threading
from abilities.abilityhandler import *

#bots have names!
#bots have owners!
#bots have a server connection!
#bots have abilities!
#bots do NOT have rights!
#        ^^^
#First we must create our lovely little bot. It shall be wonderful!

class Bot(threading.Thread): #bots are actually threads, who knew?
    #bot properties
    def __init__(self, **kwargs):
        #I think this makes it a thread itself!
        threading.Thread.__init__(self)
        #Not sure what to do about the default name
        self.name = "undefined"
        #oh boy multiple owners! This is quite the list!
        self.owners = 'nospace!edarr@yakko.cs.wmich.edu', \
                kwargs.get('owner', None)

        self.channels = kwargs.get('channels', '#pit')

        #This should be a 32 bit data field in which it "describes"
        #what abilities should be available for the bot based on which
        #bits are at 1. 32 bits allows for up to 32 abilities to be dynamically
        #given out. OR by value to give ability, XOR to remove ability. The
        #abilites should be functions available to bots.
        self.abilityBits = kwargs.get('ablBits', 0)

        self.allowedToLive = True

        self.name = kwargs['name']
        self.threadID = kwargs['thrId']

    def run(self):
        #needs its own connection to the server!
        self.conn = Connection(nick=self.name)
        self.conn.connect()
        self.conn.register()
        for ch in self.channels:
            self.joinChan(ch)
        self.listen()

    def joinChan(self, chan):
        self.conn.join(chan)

    def talk(self, chan, msg):
        self.conn.privmsg(chan, msg)

    def gesture(self, chan, action):
        self.conn.action(chan, action)

    def kill(self):
        self.allowedToLive = False #:(

    def hasLeader(self, data):
        if(data.lower().startswith(self.name)):
            return True
        else:
            return False

    def getAbilityFromData(self, data):
        ability = data.split(' ')
        if(len(ability) < 2): #means the ability is missing
            return None
        return ability[1]

    def isValidAbility(self, abilityName):
        print("Reading ability: {d}".format(d=str(abilityName)))
        if(Abilities().abilityExists(abilityName)):
            return True
        else:
            return False

    def hasAbilityRights(self, abilityValue):
        if(abilityValue & self.abilityBits):
            return True
        else:
            return False

    def constructDict(self, who, where, data, bot):
        dataDict = {'who':who, 'where':where, 'data':data, 'conn':self.conn, 'bot':bot}
        return dataDict

    def interpret(self, who, where, data, mtype):
        print("\033[93m[{bn}>] Interpreting {s} of {mt} from {u} in channel {wh}\033[0m"\
                .format(bn=self.name, s=data, mt=mtype, u=who, wh=where))
        data = data.strip()
        if(data != None):
            if(self.hasLeader(data)):
                ability = self.getAbilityFromData(data)
                if(ability == None):
                    print("No ability presented")
                    self.talk(where, '{u}'.format(u=(who.split('!'))[0]))
                else:
                    #self.talk(where, "Let me see if I know what {a} means...".format(a=ability))
                    if(self.isValidAbility(ability)):
                        #self.talk(where, "I think I understand this! Let me see if I have this ability")
                        if(self.hasAbilityRights(Abilities().getAbilValByName(ability))):
                            #self.talk(where, "I can do this ability!")
                            if(who in self.owners):
                                #self.talk(where, "I'm at your service")
                                ab = Ability(ability, self.constructDict(who, where, data, self))
                                ab.execute()
                            else:
                                self.talk(where, "you don't own me!")
                        else:
                            self.talk(where, "It's an ability I cannot perform yet")
                    else:
#                        self.talk(where, "I don't recognize that ability")
                        self.gesture(where, "sneers")

    def listen(self):
        for ch in self.channels:
            self.talk(ch, "I'm alive!")
            self.talk(ch, \
                'My name is {n}, my thread ID is {th}, and my owner(s) is/are {own}' \
                .format(n=self.name, th=self.threadID, own=str(self.owners)))

        while self.allowedToLive: #holy shit this is a sad variable :((((
            try:
                data = self.conn.recieve();
                print("\033[92m[<]{n}: {d}\033[0m".format(n=self.name, d=data))
            except UnicodeDecodeError:
                print("Unicode is evil")

            for line in data.splitlines():
                print("Data line: {l}".format(l=line))
                if 'PING' == line.split()[0]:
                    print("Recieved a ping message, responding with pong")
                    self.conn.pong(line.split()[1])
                #I guess this works, but it removes allowance of mtype interpretation
                elif 'PRIVMSG' in line:
                    dataDict = MessageHandler().parse(line)
                    self.interpret(
                            dataDict['user'],
                            dataDict['channel'],
                            dataDict['data'],
                            dataDict['mtype'])


