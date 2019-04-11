#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
from sys import argv


#----------------
TM = 0 # Taille du message caché
CI = 0 # Channel indicateur
C1 = 0 # Channel 1
C2 = 0 # Channel 2
f_value = ''
o_value = ''
verbose = False
#----------------

fullcmd = []
for i in range(1,len(argv)):
    fullcmd.append(argv[i])


def help():
    print 'pit -f File [-o outputFile] [-v]'
try:
    if "-f" in fullcmd:

        if fullcmd[fullcmd.index('-f')+1][0] != '-':
            f_value = fullcmd[fullcmd.index('-f')+1]
        else :
            print '[-] bad file given'
            help()
            exit()
    else:
        print '[-] No file given (-f)'
        exit()
except:
    print '[-] Error -f'
    exit()
try:
    if "-o" in fullcmd:
        if fullcmd[fullcmd.index('-o')+1][0] != '-':
            o_value = fullcmd[fullcmd.index('-o')+1]
        else:
            print '[-] No ouput file given'
            exit()
except:
    print '[-] Error in -o option'
    exit()


if "-v" in fullcmd:
    verbose = True

def isPrime(number): # if it's prime number
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
    else:
        return False
#GET INDICATOR CHANNEL
def getCI(TM):
    TM = TM/8
    if TM % 2 == 0:
        return 'R'
    elif isPrime(TM):
        return 'B'
    else :
        return 'G'

def get2LSB(arg):
    bits = format(arg,'b')
    bits = '0'*(8-len(bits))+bits
    return bits[len(bits)-2]+bits[len(bits)-1]


img = Image.open(f_value,'r')
pix = img.load()

msglength = []
if verbose:
    print "Name file : "+f_value
    print "size of img : "+str(img.width)+"x"+str(img.height)
for i in range(3):
    msglength.append(format(pix[i,0][0],'b'))
    msglength.append(format(pix[i,0][1],'b'))
    if i < 2 :
        msglength.append(format(pix[i,0][2],'b'))

for i in range(len(msglength)):
    msglength[i] = '0'*(8-len(msglength[i]))+msglength[i]

msglength = ''.join(msglength)
TM = int(msglength,2)
if verbose:
    print 'Size of embedded message : '+str(TM)
    print 'Size in octets : '+str(TM/8)

CI = getCI(TM)
parity = format(TM,'b').count('1')

if CI == 'R':
    if parity % 2 == 0 :
        if verbose:
            print 'parity : EVEN'
        C1 = 'B'
        C2 = 'G'
    else :
        if verbose:
            print 'parity : ODD'
        C1 = 'G'
        C2 = 'B'
elif CI == 'G':
    if parity % 2 == 0:
        if verbose:
            print 'parity : EVEN'
        C1 = 'B'
        C2 = 'R'
    else:
        if verbose:
            print 'parity : ODD'
        C1 = 'R'
        C2 = 'B'
elif CI == 'B':
    if parity % 2 == 0:
        if verbose:
            print 'parity : EVEN'
        C1 = 'G'
        C2 = 'R'
    else:
        if verbose:
            print 'parity : ODD'
        C1 = 'R'
        C2 = 'G'

hiddendata = ''
count = TM
if verbose:
    print 'indicator channel : '+CI
    print 'Channel 1 : '+C1+';'
    print 'Channel 2 : '+C2+';'

tosub1 = 2
tosub2 = 4
i = 1 #begin to second line
while i < img.height and count > 0 :
    j = 0
    while j < img.width and count > 0:
        red = pix[j,i][0]
        green = pix[j,i][1]
        blue = pix[j,i][2]
        if  CI == 'R':
            if get2LSB(red) == '01':
                if C2 == 'G':
                    hiddendata += get2LSB(green)
                elif C2 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub1
            elif get2LSB(red) == '10':
                if C1 == 'G':
                    hiddendata += get2LSB(green)
                elif C1 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub1
            elif get2LSB(red) == '11':
                if C1 == 'G':
                    hiddendata += get2LSB(green)
                elif C1 == 'B':
                    hiddendata += get2LSB(blue)
                if C2 == 'G':
                    hiddendata += get2LSB(green)
                elif C2 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub2


        elif CI == 'G':
            if get2LSB(green) == '01':
                if C2 == 'R':
                    hiddendata += get2LSB(red)
                elif C2 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub1
            elif get2LSB(green) == '10':
                if C1 == 'R':
                    hiddendata += get2LSB(red)
                elif C1 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub1
            elif get2LSB(green) == '11':
                if C1 == 'R':
                    hiddendata += get2LSB(red)
                elif C1 == 'B':
                    hiddendata += get2LSB(blue)
                if C2 == 'R':
                    hiddendata += get2LSB(red)
                elif C2 == 'B':
                    hiddendata += get2LSB(blue)
                count -= tosub2


        elif CI == 'B':
            if get2LSB(blue) == '01':
                if C2 == 'R':
                    hiddendata += get2LSB(red)
                elif C2 == 'G':
                    hiddendata += get2LSB(green)
                count -= tosub1
            elif get2LSB(blue) == '10':
                if C1 == 'R':
                    hiddendata += get2LSB(red)
                elif C1 == 'G':
                    hiddendata += get2LSB(green)
                count -= tosub1
            elif get2LSB(blue) == '11':
                if C1 == 'R':
                    hiddendata += get2LSB(red)
                elif C1 == 'G':
                    hiddendata += get2LSB(green)
                if C2 == 'R':
                    hiddendata += get2LSB(red)
                elif C2 == 'G':
                    hiddendata += get2LSB(green)
                count -= tosub2

        j+=1
    i+=1

hiddenmessage = ''
for i in range(0,len(hiddendata),8):
    hiddenmessage += chr(int(hiddendata[i:i+8],2))

if o_value != '':
    f = open(o_value,'w')
    f.write(hiddenmessage)
    f.close()
    print o_value +' was created !'
else:
    print hiddenmessage
