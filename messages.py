#!usr/bin/env python
import re
#handle message distribution

class MessageHandler():
    #regex it to get nick, username, server, message type,
    #   channel, and message
    #ex: nospace!edarr@yakko.cs.wmich.edu PRIVMSG #asdf :testing
    def parse(self, data):
        #"borrowed" from stringy <3
        #   who probably "borrowed" it from someone else
        IRC_RE = re.compile(r'^(:(?P<prefix>\S+) )?(?P<command>\S+)' \
                          '( (?!:)(?P<params>.+?))?( :(?P<trail>.+))?$')
        match = IRC_RE.match(data)
        if match:
            ref = {'user':match.group('prefix'),
                    'mtype':match.group('command'),
                    'channel':match.group('params'),
                    'data':match.group('trail')}
            return ref
        else:
            #no match!
            ref = {'user':None,'mtype':None,'channel':None,'data':None}
            return ref

    #The data should be sent in as a dictionary and be used with the appropriate application
#    def distribute(self, data):
        # Based on the given data we must figure out if it's important data or not
        # We should first determine if the message is for specified bot
        #       Continue with message handling if it is
        #   otherwise
        #       Ignore it
        #
        # We should then decide whether the person who directed the message
        #   allowed to control the bot, referencing the owners list, and perhaps
        #   make a blacklist/ignorelist in the future
        #
        # Next we determine whether the bot has the ability


