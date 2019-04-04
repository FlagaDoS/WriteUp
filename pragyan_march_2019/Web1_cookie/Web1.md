## Web 1 - Cookie 

First check cookie of request : we can see ' flag=....' in cookie send and cookie get form the response.

Let's go check what is the hash after flag 

After checking it's MD5 of sent flag is **pc**

the MD5 get from requests is **tf** 

Just for check, i make a requests GET with the MD5 of **tf** and send it, i get a responses with flag in cookie with a MD5 which means ''**{** *someOtherLetter* ''

So let's make a script who did the job : 

```python
import requests
import hashlib
import sys
# Script md5 decrypt got from : https://stackoverflow.com/questions/2760911/is-a-there-md5-decrypt-function-in-python
def decryptMD5(testHash):
        s = []
        while True:
                m = hashlib.md5()
                for c in s:
                        m.update(chr(c))
                hash = m.hexdigest()
                if hash == testHash:
                        return ''.join([chr(c) for c in s])
                wrapped = True
                for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 256
                        if s[i] != 0:
                                wrapped = False
                                break
                if wrapped:
                        s.append(0)



sess = requests.Session()
flag = ''

url = 'http://159.89.166.12:13500/'

r = sess.get(url)

cookie = str((sess.cookies)).split('flag=')[1].split(' ')[0]
flag += decryptMD5(cookie)
headers = {'flag':cookie}

while flag[len(flag)-1] != '}':
    r = sess.get(url,headers=headers)
    cookie = str((sess.cookies)).split('flag=')[1].split(' ')[0]
    headers = {'flag':cookie}
    flag += decryptMD5(cookie)
    print flag

```



And get the flag :D