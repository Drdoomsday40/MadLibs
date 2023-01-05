# This mad lib uses f string method to write out multiple string functions
# with less writing for iteration.
# alternatives:
# print("Hello " + mystring) is concatonation
# print("Hello {}".format(mystring)) 
#
# This is generally a better method as concatonation needs additional
# quotation marks multiple times and + signs that can cause common errors.
# It also places it directly where needed so you do not have to 
# # look side to side to compare with multiple functions in a row.
#
# https://www.madtakes.com/libs/186.html

def madLib():
    print("We are writing a Mad Lib using Fstring method on, the Prologue of Romeo and Juliet.\n\
Let's get started by adding some crazy words to pizazz this story!\n\n")

    
    pluralNoun1 = input("Plural Noun: ")
    place1 = input("Place: ")
    noun1 = input("Noun: ")
    pluralNoun2 = input("Plural Noun: ")
    noun2 = input("Noun: ")
    adj1 = input("Adjective: ")
    verb1 = input("Verb: ")
    number1= input("Number: ")
    adj2 = input("Adjective: ")
    bodyPart1 = input("Body Part: ")
    verb2 =input("Verb: ")
    print("\n\n")

    madLib = f"\
Two {pluralNoun1}, both alike in dignity,\n\
In fair {place1}, where we lay our scene,\n\
From ancient {noun1} break to new mutiny,\n\
Where civil blood makes civil hands unclean.\n\
From forth the fatal loins of these two foes\n\
A pair of star-cross`d {pluralNoun2} take their life;\n\
Whole misadventured piteous overthrows\n\
Do with their {noun2} bury their parents` strife.\n\
The fearful passage of their {adj1} love,\n\
And the continuance of their parents` rage,\n\
Which, but their children`s end, nought could {verb1},\n\
Is now the {number1} hours` traffic of our stage;\n\
The which if you with {adj2} {bodyPart1} attend,\n\
What here shall {verb2}, our toil shall strive to mend."

    print(madLib)