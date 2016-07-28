

def identify(dictRef):
    dictRef['bot'].talk(dictRef['where'], 'Name: {n}' \
            .format(n=dictRef['bot'].name))
    dictRef['bot'].talk(dictRef['where'], 'Owner(s): {o}' \
            .format(o=dictRef['bot'].owners))
    dictRef['bot'].talk(dictRef['where'], 'ThreadID: {t}' \
            .format(t=dictRef['bot'].threadID))
    dictRef['bot'].talk(dictRef['where'], 'Channels: {c}' \
            .format(c=dictRef['bot'].channels))
