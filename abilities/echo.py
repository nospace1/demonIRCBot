#!usr/bin/env python
#echo.py
#import sys
#sys.path.append('..')

#from bots import *
#from connection import *

#dict_ref = who, where, data, conn, bot
def echo(dictRef):
    dictRef['bot'].talk(dictRef['where'], dictRef['data'])

