#!/usr/bin/env python
import sys,pyperclip

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def print_h():
    print '#---------------------------------------'
    print '# gen [number] [sequenceToSearch] [-f | -c]'
    print '# gen 40'
    print '# gen 40 ei6d'
    print '# gen 40 -f'
    print '# gen 40 -c'
    print '# gen 40 -f -c'
    print '#---------------------------------------'

input = ""
search = ""
gen = ""
format = ""
f = False
c = False
if len(sys.argv) < 2:
    print_h()
    sys.exit()
elif len(sys.argv) < 3:
    if(RepresentsInt(sys.argv[1]) != False):
        input = int(sys.argv[1])
    else:
        print "Please give an number"
        sys.exit()
elif len(sys.argv) < 4:
    if(RepresentsInt(sys.argv[1]) != False):
        input = int(sys.argv[1])
    else:
        print "Please give an number"
        sys.exit()
    if sys.argv[2] != "-f" and sys.argv[2] != "-c":
        search = sys.argv[2]
    for item in sys.argv:
        if item == "-f":
            f = True
        if item == "-c":
            c = True



liste=[65,97,48]
i = 0
index = 0
while i < input :
    # print chr(liste[2])
    gen+=chr(liste[index])
    index+=1
    if index == 3:
        index = 0
        liste[2]+=1

    if liste[2] == 58:
        liste[2] =48
        liste[1]+=1
    if liste[1] == 123:
        liste[1] = 97
        liste[0] +=1
    if liste[0] == 91:
        liste[0] = 65
    i+=1

if search == "":
    if f:
        pyt = "gen = \"\"\n"
        pyt += "gen += \""
        compt = 0
        for i in range (0,len(gen)):
            if compt == 15:
                pyt +="\"\n"
                if i != len(gen)-2:
                    pyt += "gen += \""
                compt = 0
            pyt+=gen[i]
            compt+=1

        pyt +="\""
        if c:
            pyperclip.copy(pyt)
        print pyt
    else:
        if c:
            pyperclip.copy(gen)
        print gen

else :
    try:
        print gen.index(search)
    except:
        print 'NOT FOUND'
