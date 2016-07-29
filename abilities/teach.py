
#probably need to rmove this ability it's not useful I don't think
#will replace with ability "teach"
import abilityhandler

def getLesserByName(name, lesserlist):
    for less in lesserlist:
        if(less.name == name):
            return less
    return None

def knowsAbility(abilityName, teacher):
    if(teacher.abilityBits & abilityhandler.Abilities().getAbilValByName(abilityName)):
        return True
    return False

def teach(dictRef):
    teacher = dictRef['bot']
    data = dictRef['data'].split(' ', 3)
    if(len(data) < 4):
        teacher.talk(dictRef['where'], "Usage: [teacher] teach [student] [ability]")
    else:
        studentName = data[2]
        ability = data[3]
        student = getLesserByName(studentName, teacher.lessers)
        #verify it has this bot as a lesser of itself
        if(student != None):
            #verify this bot can teach the ability
            if knowsAbility(ability, teacher):
                teacher.gesture(dictRef['where'], "waves his hand over {s}".format(s=studentName))
                student.abilityBits = student.abilityBits | abilityhandler.Abilities().getAbilValByName(ability)
        else:
            #bot doesn't have it as a lesser
            teacher.talk(dictRef['where'], "I don't recognize this lesser")



