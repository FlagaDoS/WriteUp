#!/usr/bin/env python
# -*- coding: utf-8 -*-



# ------- Program updated at this URL
# https://github.com/taiQui/UsefulTools
# -------



from PIL import Image
from sys import argv,exit

# var ------------
f_value = ''
verbose = False
d_value = '.'
n_value = []
extension = ''
rgb_value =[]
type = 0
l = 0
# -----------------
def help():
    print '---------------------'
    print '# lsb [find | extract] [-rgb r:g:b[:Jump]] [-v] [-f : file ] [-d : directory ] [-n : sizeDown:sizeUp] [-l : HowManyLine]'
    print '---------------------'


fullcmd = []
for i in range(1,len(argv)):
    fullcmd.append(argv[i])
if len(fullcmd) < 2:
    help()
    exit()
elif len(fullcmd) == 2 and ('-v' in fullcmd ):
    help()
    exit()
try:
    if "-f" in fullcmd:
        if fullcmd[fullcmd.index('-f')+1][0] != '-':
            f_value = fullcmd[fullcmd.index('-f')+1]
            extension = f_value.split('.')
            extension = extension[len(extension)-1]
        else :
            print '[-] bad file given'
            help()
            exit()
except:
    print '[-] Error -f'
    exit()
try:
    if "-d" in fullcmd:
        if fullcmd[fullcmd.index('-d')+1][0] != '-':
            d_value = fullcmd[fullcmd.index('-d')+1]
        else :
            print '[-] bad output directory given'
            help()
            exit()
except:
    print '[-] Error : -d'
    exit()
try:
    if "-n" in fullcmd:
        if fullcmd[fullcmd.index('-n')+1][0] != '-':
            if len(fullcmd[fullcmd.index('-n')+1].split(':'))==2:
                if fullcmd[fullcmd.index('-n')+1].split(':')[0].isdigit() and fullcmd[fullcmd.index('-n')+1].split(':')[1].isdigit():
                    if int(fullcmd[fullcmd.index('-n')+1].split(':')[0])>int(fullcmd[fullcmd.index('-n')+1].split(':')[1]):
                        print '[-] Error delimiter'
                        help()
                        exit()
                    n_value.append(fullcmd[fullcmd.index('-n')+1].split(':')[0])
                    n_value.append(fullcmd[fullcmd.index('-n')+1].split(':')[1])
                    if int(n_value[1]) > 9:
                        print '[-] Up delimiter sup to 9 '
                        print '[-] put to 9'
                        n_value[1]='9'
                    if n_value[0] == n_value[1]:
                        n_value[1] = chr(ord(n_value[1])+1)
                else:
                    print '[-] Error NaN'
                    help()
                    exit()

            else:
                print '[-] Bad format number'
                help()
                exit()
        else :
            print '[-] bad number lsb given'
            help()
            exit()
    else :
        n_value.append('0')
        n_value.append('9')
except:
    print '[-] Arg \'-n\' ERROR '
    exit()
if "-v" in fullcmd:
    verbose = True

if "-rgb" in fullcmd:
    if fullcmd[fullcmd.index('-rgb')+1][0] != '-':
        if len(fullcmd[fullcmd.index('-rgb')+1].split(':'))>=3:
            if fullcmd[fullcmd.index('-rgb')+1].split(':')[0].isdigit() and fullcmd[fullcmd.index('-rgb')+1].split(':')[1].isdigit() and fullcmd[fullcmd.index('-rgb')+1].split(':')[2].isdigit()  :
                rgb_value.append(fullcmd[fullcmd.index('-rgb')+1].split(':')[0])
                rgb_value.append(fullcmd[fullcmd.index('-rgb')+1].split(':')[1])
                rgb_value.append(fullcmd[fullcmd.index('-rgb')+1].split(':')[2])
                if len(fullcmd[fullcmd.index('-rgb')+1].split(':')) == 4:
                    if fullcmd[fullcmd.index('-rgb')+1].split(':')[3].isdigit():
                        rgb_value.append(fullcmd[fullcmd.index('-rgb')+1].split(':')[3])
                    else:
                        print '[-] Error NaN for -rgb arguments'
                        exit()
                else:
                    rgb_value.append('1')
                if int(rgb_value[0])>8 or int(rgb_value[1])>8 or int(rgb_value[2])>8:
                    print '[-] Error arg > 8'
                    exit()
            else:
                print '[-] Error NaN for arguments rgb'
                help()
                exit()
        else:
            print '[-] Error given arguments for rgb'
            help()
            exit()
    else:
        print '[-] Error arguments -rgb '
        help()
        exit()
else:
    rgb_value.append('1')
    rgb_value.append('1')
    rgb_value.append('1')
    rgb_value.append('1')
if 'extract' in fullcmd:
    type = 0
elif 'find' in fullcmd:
    type = 1

if 'extract' in fullcmd and 'find' in fullcmd:
    print '[-] Error given 2 action '
    help()
    exit()

try:
    im = Image.open(f_value)
    imaux = Image.open(f_value)
except:
    print '[-] Error opening file'
    exit()
pix = im.load()
pixaux = imaux.load()

if "-l" in fullcmd:
    if fullcmd[fullcmd.index('-l')+1][0] != '-':
        if fullcmd[fullcmd.index('-l')+1].isdigit():
            l = int(fullcmd[fullcmd.index('-l')+1])
        else:
            print '[-] Error NaN for -l arguments'
            exit()
    else:
        print '[-] Error in arguments of -l'
        help()
        exit()
else:
    l = im.width

if verbose :
    print '[*] File loaded : '+f_value
    print '[*] Extension file : '+extension
    print '[*] Size : '+str(im.width)+"*"+str(im.height)
    print '[*] Delimiter : '+str(int(n_value[0]))+':'+str(int(n_value[1]))
if verbose:
    print '[*] Pixel loaded ...'
def find():
    if verbose:
        print '[*] FIND execution'
    for k in range(int(n_value[0]),int(n_value[1])):
        for i in range(0, im.width):
    	    for j in range(0,l):
    		    r,g,b = pix[j,i]
    		    raux = bin(r).split('b')[1]
    		    while len(raux) < 8:
    		        raux = '0'+raux
    		    gaux = bin(g).split('b')[1]
    		    while len(gaux) < 8:
    		        gaux = '0'+gaux
    		    baux = bin(b).split('b')[1]
    		    while len(baux) < 8:
    		        baux = '0'+baux
    		    pixaux[j,i] = (int(raux[k:9]+'0'*k,2),int(gaux[k:9]+'0'*k,2),int(baux[k:9]+'0'*k,2))

        imaux.save(d_value+'/decod'+str(k)+'.'+str(extension))
        if verbose:
            print '     [*]  file saved with '+str(int(8-k))+' lsb in '+d_value+'/decod'+str(k)+'.'+str(extension)


def extract():
    if verbose:
        print '[*] EXTRACT execution'
        print '[*] will take '+rgb_value[0]+" red - "+rgb_value[1]+" green - "+rgb_value[2]+' blue with a jumps of '+rgb_value[3]+' between each pixel'
    hidden = ''
    for i in range(0, l):#Line
        for j in range(0,im.width,int(rgb_value[3])): #collumn
            r,g,b = pix[j,i]
            r =format(int(r),'b')
            r = r.zfill(8-len(r))
            g =format(int(g),'b')
            g = g.zfill(8-len(g))
            b =format(int(b),'b')
            b = b.zfill(8-len(b))
            hidden+=r[8-int(rgb_value[0]):]+g[8-int(rgb_value[1]):]+b[8-int(rgb_value[2]):]
    plain = ''
    for i in range(0,len(hidden),8):
        plain+=chr(int(hidden[i:i+8],2))
    print 'plain text :'
    print plain
    f = open('ext.'+extension,'w')
    f.write(plain)
    f.close()
if type == 1:
    find()
elif type == 0:
    extract()
