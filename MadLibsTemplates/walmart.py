# This version is using Tuples data storage.
# https://www.madtakes.com/libs/172.html

global walmartTuple
global tempList
walmartTuple = ("",)
tempList = []

def v():
    global walmartTuple
    global tempList
    walmartTuple = ()
    tempList = list(walmartTuple)
    tempList.append(input("A Verb: "))
    walmartTuple = tuple(tempList)

    return

def adj(tup):
    #global walmartTuple
    #global tempList
    walmartTuple = (tup)
    tempList = list(walmartTuple)
    tempList.append(input("An Adjective: "))
    walmartTuple = tuple(tempList)
    return 



def madLib():
    print("We are writing a Mad Lib using the data storage type Tuple, \
        based on the story, Can I Have Your Daughter`s Hand?.\n\n\
You need to write unique or similar words each time!\n\
Let's get started by adding some crazy words to pizazz this story!\n\n")

    # 15 items in this tuple
    """global walmartTuple
    global tempList
    walmartTuple = ("",)
    tempList = []"""

    v()
    #adj()

    print("\n")
    print("Come ", walmartTuple[0], " at Walmart, where you'll receive ", walmartTuple[1], " discounts on all of your favorite brand name ", walmartTuple[0])
