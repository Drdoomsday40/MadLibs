# This version is using a list data storage. (to use an array, import NumPy as np)
# https://www.madtakes.com/libs/169.html

"""
def isWord(user_input):
    try:
        user_input.isalpha()
    except:
        adjective.pop()
        print("Try again using letters.")
    else:
        return
"""

def adj():
    adjective.append(input("Adjective: "))
    return 
    # print(type(user_input), type(adjective))
    # isWord(user_input)
    # == str(adjective): return adjective.append(input)
    # else: return

def nn():
    noun.append(input("Noun: "))
    return

def nns():
    nouns.append(input("Plural Nouns: "))
    return

def vED():
    verbED.append(input("A Verb ending in \"ed\": "))
    return

def plc():
    place.append(input("A place: "))
    return

def vING():
    verbING.append(input("A Verb ending in \"ing\": "))
    return
    
def adv():
    adverb.append(input("An adverb: "))
    return

def fm():
    female.append(input("A female's Name: "))
    return

def madLib():
    print("We are writing a Mad Lib using Lists data storage on, The Raven.\n\
        Let's get started by adding some crazy words to pizazz this story!\n\n")
    global adjective, noun, nouns, verbED, verbING, adverb, place, female 
    adjective = noun = nouns = verbED = verbING = adverb = place = female = []
    adj(), adj(), adj()
    nn(), nn()
    vED()
    nn(), nn()
    plc()
    nn()
    adj()
    vING()
    nn()
    vED()
    adv()
    nns()
    adj(), adj(), adj()
    fm()
    # adjective.append(input("Adjective: "))
    # adjective.append(input("Adjective: "))
    # adjective.append(input("Adjective: "))
    """
    ADJ
    ADJ
    ADJ
    NOUN	
    NOUN	
    VERB ENDING IN "ED"	
    NOUN	
    NOUN	
    PLACE	
    NOUN	
    PLACE (same again)
    ADJECTIVE	
    VERB ENDING IN "ING"	
    NOUN	
    VERB ENDING IN "ED"	
    ADVERB	
    NOUN (PLURAL)	
    ADJECTIVE	
    ADJECTIVE	
    ADJECTIVE	
    FEMALE NAME"""
    print("\n")
    madLib = f"\
Once upon a midnight {adjective[0]}, \n\
while I pondered {adjective[1]} and {adjective[2]},\n\
Over many a quaint and curious {noun[0]} of forgotten {noun[1]},\n\
While I {verbED[0]}, nearly napping, suddenly there came a {noun[2]},\n\
As of {noun[3]} gently rapping, rapping at my {place[0]} door.\n\
``Tis some  {noun[4]},` I muttered, `tapping at my {place[0]} door -\n\
Only this, and nothing more.`\n\
\n\
Ah, distinctly I remember it was in the {adjective[3]} December,\n\
And each separate {verbING[0]} ember wrought its {noun[5]} upon the floor.\n\
Eagerly I {verbED[1]} the morrow; - {adverb[0]} I had sought to borrow\n\
From my {nouns[0]} surcease of sorrow - \
sorrow for the {adjective[4]} Lenore -\n\
For the {adjective[5]} and  {adjective[6]} maiden whom the angels named {female[0]} -\n\
Nameless here for evermore."

    print(madLib)