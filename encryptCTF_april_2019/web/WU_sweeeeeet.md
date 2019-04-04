# WU Sweeeeeet

#### Written and solved by Balr0g404

![Sweeeeeet](/home/audran/Documents/flagados/encryptCTF/Sweeeeeet.png)

By entering the given URL into our browser, we arrive on a webpage with some text:

![S1](/home/audran/Documents/flagados/encryptCTF/S1.png)

The flag is not here, damn ! But I think, according to the name of the challenge, that the flag is something sweeeeeet.... What could be so sweet ? A **cookie** maybe ? Let's check the cookie(s) we have:

![S2](/home/audran/Documents/flagados/encryptCTF/S2.png)

Ohoh, interesting ! We have two different cookies: **FLAG** and **UID**. The FLAG cookie is clearly useless, but the UID let us thinks about the **User ID** of an Unix-based system. The data of the cookie looks like a **MD5** hash. Just to be sure, let confirm this with the **hash-identifier** programm:

![S3](/home/audran/Documents/flagados/encryptCTF/S3.png)

Since the MD5 is a very weak hash, we can try to crack it on the well-known https://crackstation.net/ ! We are lucky, it works, and we see that the hashed data is the number "**100**". 

On a Unix-based system, we know that each user has a specific UID, and especially the superuser has the UID **0**. So why not try to tell the webpage that we are **root** ?

We just compute the MD5 of "0" and resend the cookie with this value.

![S4](/home/audran/Documents/flagados/encryptCTF/S4.png)

![S6](/home/audran/Documents/flagados/encryptCTF/S6.png)

Enjoy !