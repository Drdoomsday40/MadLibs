# This version is using a set data storage. 
# https://www.madtakes.com/libs/167.html

def adv():
    adverb.add(input("An adverb: "))
    return

def nn():
    noun.add(input("Noun: "))
    return

def liqu():
    liquid.add(input("Liquid: "))
    return

def v():
    verb.add(input("Verb: "))
    return

def numb():
    number.add(input("Number: "))
    return

def nns():
    nouns.add(input("Plural Nouns: "))
    return

def adj():
    adjective.add(input("Adjective: "))
    return 

def sick():
    sickness.add(input("Illness: "))
    return

def occup():
    occupation.add(input("Occupation: "))
    return

def bods():
    bodies.add(input("Body Parts: "))
    return

def body():
    bodyPart.add(input("Body Part: "))
    return

def madLib():
    print("We are writing a Mad Lib using data storage Sets on, How to Wash Your Face.\n\
        You need to write unique words each time!\n\
        Let's get started by adding some crazy words to pizazz this story!\n\n")
    global adverb, noun, liquid, verb, number, nouns, adjective, sickness, occupation, bodies, bodyPart
    adverb = set()
    noun = set()
    liquid = set()
    verb = set()
    number = set()
    nouns = set()
    adjective = set()
    sickness = set()
    occupation = set()
    bodies = set()
    bodyPart = set()
    adv()
    nn()
    liqu()
    v()
    numb()
    nns()
    v()
    adj()
    nn()
    nns()
    sick()
    occup()
    bods()
    body()
    print("\n")
    madLib = f"\
In order to wash your face {adverb.pop()}, you must wet your {noun.pop()} in warm \n\
{liquid.pop()}. Then, {verb.pop()} it across your face {number.pop()} times. This will \n\
wash off any remaining {nouns.pop()}. When you are done you should {verb.pop()} the cloth \n\
in {adjective.pop()} water to clean it. You should also wash your face with a {noun.pop()} \n\
to keep it smooth and shiny. This will keep also keep away {nouns.pop()}. Don`t \n\
worry. It is normal to experience {sickness.pop()} the first time you try \n\
this. Consult your {occupation.pop()} if you break out in {bodies.pop()}. \n\
This works well on your {bodyPart.pop()} too!"

    print(madLib)