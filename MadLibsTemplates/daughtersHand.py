# This version is using a dictionary data storage. 
# https://www.madtakes.com/libs/177.html

sncount = swcount = vcount = ncount = 0

def sillynam():
    global sncount
    sillyname = input("A silly name: ")

    if sillyname not in sillynamedict:
        sillynamedict[sncount] = sillyname
        sncount+=1

    return

def sillywor():
    global swcount
    sillyword = input("A silly word: ")

    if sillyword not in sillyworddict:
        sillyworddict[swcount] = sillyword
        swcount+=1
    else:
        print("That word already exists in the dictionary, please try a new word.")
        sillywor()
    
    return

def ver():
    global vcount
    verb = input("A verb: ")

    if verb not in verbdict:
        verbdict[vcount] = verb
        vcount+=1
    else:
        print("That word already exists in the dictionary, please try a new word.")
        ver()
    
    return

def nn():
    global ncount
    noun = input("A noun: ")

    if noun not in noundict:
        noundict[ncount] = noun
        ncount+=1
    else:
        print("That word already exists in the dictionary, please try a new word.")
        nn()
    
    return

def bdypart():
    sillyname = input("A body part: ")
    sillynamedict[0] = sillyname

    return

def femname():
    sillyname = input("A female name: ")
    sillynamedict[0] = sillyname

    return

def vrbed():
    verbed = input("A verb ending in ed: ")
    verbeddict[0] = verbed

    return

def nns():
    nouns = input("A plural noun: ")
    nounsdict[0] = nouns

    return

def jorb():
    job = input("A job: ")
    jobdict[0] = job

    return

def numm():
    numb = input("A number: ")
    numbdict[0] = numb

    return

def madLib():
    print("We are writing a Mad Lib using data storage Dictionary on, Can I \
Have Your Daughter`s Hand?.\n\n\
You need to write unique words each time!\n\
Let's get started by adding some crazy words to pizazz this story!\n\n")
    global sncount, sillyname, sillynamedict, \
        swcount, sillyword, sillyworddict, \
        vcount, verb, verbdict, \
        ncount, noun, noundict, \
        bodypart, bodypartsdict, \
        female, femaledict, \
        verbed, verbeddict, \
        nouns, nounsdict, \
        job, jobdict, \
        numb, numbdict

    sillynamedict = {}
    sillyworddict = {}
    verbdict = {}
    noundict = {}
    bodypartsdict = {}
    femaledict = {}
    verbeddict = {}
    nounsdict = {}
    jobdict = {}
    numbdict = {}
    sillynam()
    sillywor()
    ver()
    nn()
    bdypart()
    femname()
    vrbed()
    nn()
    nns()
    ver()
    nn()
    jorb()
    numm()
    ver()
    sillywor()
    sillynam()
    print("\n")

    madLib = f"\
Will you let me {sillynamedict.get(0)} your {sillyworddict.get(0)}? Ever since \n\
I have laid {verbdict.get(0)} on \
{noundict.get(0)}, I have  {bodypartsdict.get(0)} madly in love with her. I wish that she \
will be the \n\
{femaledict.get(0)} of my {verbeddict.get(0)} and \
that someday we will {sillynamedict.get(0)} happily ever after. I have a \n\
{noundict.get(1)} as a/an {nounsdict.get(0)} Plant Operator that pays \
${verbdict.get(1)} each month. I \n\
promise to {noundict.get(2)} {verbdict.get(2)} with kindness and \
respect. \n\n\
Sincerely, \n\
{sillynamedict.get(1)} {sillynamedict.get(1)}"
    print(madLib)