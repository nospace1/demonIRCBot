

def suicide(dictRef):
    dictRef['bot'].talk(dictRef['where'], "I will be back...")
    dictRef['bot'].allowedToLive = False
