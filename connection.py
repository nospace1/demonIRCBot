import socket
import logging

class Connection():

    def __init__(self, **kwargs):
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 6667)
        self.nick = kwargs.get('nick', 'undefined')
        self.chan = kwargs.get('channel', '#pit')
        self.ident = kwargs.get('ident', self.nick)
        self.realname = kwargs.get('realname', self.nick)
        self.sock = socket.socket()

    def connect(self):
        print("Connecting to server: " + self.host)
        self.sock.connect((self.host, self.port))
        data = self.sock.recv(4096).decode()

    def sendraw(self, string):
        #send a raw message to the server!
        print("\033[91m[>] {s}\033[0m".format(s=string))
        self.sock.send(string.encode())

    def register(self):
        #registers after connection?
        print("Sending Nick information")
        self.sendraw("NICK {n}\r\n".format(n=self.nick))
        print("Registering with identity {i} and name {n}" \
                .format(i=self.ident, n=self.realname))
        self.sendraw("USER {i} 0 * :{n}\r\n" \
                .format(i=self.ident, n=self.realname))

    def join(self, chan):
        self.sendraw("JOIN {ch}\r\n".format(ch=chan))

    def part(self, chan):
        self.sendraw("PART {ch}\r\n".format(ch=chan))

    def recieve(self):
        data = self.sock.recv(4096).decode()
        return data

    def privmsg(self, chan, message):
        msg = "PRIVMSG {ch} :{m}\r\n".format(ch=chan, m=message)
        self.sendraw(msg)

    def action(self, chan, action):
        act = "PRIVMSG {ch} :\x01ACTION {a}\r\n".format(ch=chan, a=action)
        self.sendraw(act)

    def pong(self, message):
#        print("I'm ponging: {m}".format(m=message))
        self.sendraw("PONG {m}\r\n".format(m=message))

    def lookup(self, user):
        self.sendraw("WHOIS {u}\r\n".format(u=user))


