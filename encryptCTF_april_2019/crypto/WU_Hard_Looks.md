# WU Hard Looks

#### Written and solved by Balr0g404

![Hard_looks](/home/audran/Documents/flagados/encryptCTF/Hard_looks.png)

Well, this challenge **does** look hard ! I first though about a morse code, but this is not. 

We can see that we have only two different characters, so we can think about **binary**. Unfortunately, we can observe that we have only **510** characters. Since we now that an ASCII character is encoded with **8** bits, we are missing **2** bits. Dammned !

Let's assume that "-" is 1 and that "_" is 0. If we decode the beginning of the ciphertext, we obtain **11011000**.

However, since the flag has the format **encryptCTF{FLAG}**, we can easely guess what we should have at the beginning by encoding **encrypt** in binary. We then obtain for the first 8 bits **0011011000**.

Good news, this is exactly the same as the one we found above, with **just two more 0s at the beginning** ! We can now write a python script to resolve the challenge:

 ```python
#!/usr/bin/python
#coding: utf-8

data = "--_--___--_-_-__--_--__--__-_-__--_--___--__--__--_---__--__-___--_---__---__-__--_---__--______--_---__--_-____--_-____--__--__--_-_-__--_-____--_-____--_--___--_---_--___-___--_-_-__--_---__--__--__--_-____--__--__--_-_-__--_-_-_--__--___--__--__--___-__--__--__--_---__--_-_-_--__--___--_-____---_____--__--__--_-____--_-_-__--__-___--_-____--_-____--_-_-_--__--___--__--__--__--__--_-___--__-_-__--__--__--______--_-_-__--_-_-__--_-____--_---__--_-____---_____--__--_--__--___--__-___--___-__--_---_--__-__"

bitstring = "00" #We add the two missing 0s
j = 0

for i in data:
    if j == 8:
        bitstring +=
        j = 0
    if ord(i) == 45:
        bitstring += "1"
    else:
        bitstring += "0"

    j += 1

print bitstring

 ```



We obtain the following binary chain:

0011011000 11010100 11011001 10010100 11011000 11001100 11011100 11001000 11011100 11100100 11011100 11000000 11011100 11010000 11010000 11001100 11010100 11010000 11010000 11011000 11011101 10001000 11010100 11011100 11001100 11010000 11001100 11010100 11010101 10011000 11001100 11000100 11001100 11011100 11010101 10011000 11010000 11100000 11001100 11010000 11010100 11001000 11010000 11010000 11010101 10011000 11001100 11001100 11010001 10010100 11001100 11000000 11010100 11010100 11010000 11011100 11010000 11100000 11001101 10011000 11001000 11000100 11011101 100100

With a binary to ascii decoder, we obtain the following string: **656e63727970744354467b5734355f31375f483452445f334e305547483f217d**

It Iooks hard like hexa, isnt'it ? 

Flag: encryptCTF{W45_17_H4RD_3N0UGH?!}