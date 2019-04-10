from PIL import Image
import math
import time
import socket
import base64
def decod(img):
    im = Image.open(img)
    pix = im.load()
    mid = 150
    nofound = True
    insquare = False
    arrayPT = []
    middle = []
    def vertAsc(i,j): # run vertically up
        r,g,b = pix[i,j]
        while( r < mid and g < mid and b < mid and i >= 0):
            i -=1
            r,g,b=pix[i,j]
        arrayPT.append((i+1,j))

    def horiDesc(i,j): # run horizontaly down
        r,g,b = pix[i,j]
        while( r < mid and g < mid and b < mid and j >=0):
            j -=1
            r,g,b = pix[i,j]
        arrayPT.append((i,j+1))
        vertAsc(i,j+1)

    def vertDesc(i,j): # run vertically down
        r,g,b = pix[i,j]
        while(r < mid and g < mid and b < mid and i < im.width):
            i+=1
            if (i < im.width):
                r,g,b = pix[i,j]
        arrayPT.append((i-1,j))
        horiDesc(i-1,j)

    def getMiddle(): #get hte middle of square
        return(((arrayPT[0][0]+arrayPT[1][0]+arrayPT[2][0]+arrayPT[3][0])/4,(arrayPT[0][1]+arrayPT[1][1]+arrayPT[2][1]+arrayPT[3][1])/4))

    def getRayon(i,j): # get radius or circle
        r,g,b = pix[i,j]
        decalage = 0
        while ( r < mid and g < mid and b < mid and j < im.height):

            decalage+= 1
            j+=1
            if (j < im.height):
                r,g,b = pix[i,j]

        return decalage

    def yolo(i,j): # return True if coordinate (i,j) if in one detected circle
        for x,y in middle:
            if (i >= x - getRayon(x,y) - 10 and i <= x + getRayon(x,y ) +10 ) and (j>= y - getRayon(x,y) -10 and j <= y + getRayon(x,y)+10):
                return True
        return False

    for i in range(im.width):
        for j in range(im.height):
            r,g,b = pix[i,j]
            if nofound:  # if no circle was detected
                if r < mid and g < mid and b < mid:
                    nofound = False
                    arrayPT.append((i,j))
            else: # else parcours the circle
                if r > mid and g > mid and b > mid:
                    arrayPT.append((i,j-1))
                    vertDesc(i,j-1)
                    if getMiddle() not in middle:
                        if not yolo(getMiddle()[0],getMiddle()[1]):
                            middle.append(getMiddle())
                    arrayPT = []
                    nofound = True

    auxiliary = []
    fuck = False
    # print middle
    for i in range(len(middle)):  # verification of no duplicate coordinate
        fuck = False
        for j in range(i+1,len(middle)):
            if (middle[i][0] >= middle[j][0]-20 and middle[i][0] <= middle[j][0] +20) and (middle[i][1] >= middle[j][1]-20 and middle[i][1] <= middle[j][1] +20):
                fuck = True
        if not fuck:
            auxiliary.append(middle[i])

    middle = auxiliary
    auxiliary = []
    for x,y in middle:
        r,g,b = pix[x,y]
        if  r < mid and b < mid and g < mid:
            auxiliary.append((x,y))
    middle = auxiliary


    # print 'number : '+str(len(middle))
    dif = []
    for i in range(len(middle)):
        for j in range(i+1,len(middle)):
            dif.append(math.sqrt(pow((middle[j][0]-middle[i][0]),2)+pow((middle[j][1]-middle[i][1]),2)))

    min = 100000.00000000

    for i in dif:

        if min > i:
            min = i

    return min

def netcat(hostname, port):
    number = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))

    img = ""
    data = ''
    while 1:

        data = s.recv(1024)
        if data == "":
            break

        img += data
        if '>>>' in img:
            print 'decoding captcha : '+str(number)
            img = img.split('to continue:\n')[1]
            f = open('decod.jpg','w')
            f.write(base64.b64decode(img))
            f.close()
            sending = decod('decod.jpg')
            # time.sleep(1)
            s.send(str(sending).encode('utf')+'\n')
            print 'sent!'+str(sending)
            img = ''
            number+=1
        if number >= 99:
            print data


    print "Connection closed."
    s.close()

netcat("p1.tjctf.org", 8005)
