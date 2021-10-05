# It is my Birthday
Category: Web Exploitation\
Points: 100

## Description
I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. [http://mercury.picoctf.net:50970/](http://mercury.picoctf.net:50970/)

## Solution
Loading the browser:
![Flag](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/It%20is%20my%20Birthday/index.png?raw=true)

The source referenced *index.php*, but that file redirects to *index.html*.\

Submitting two blank files:
```
Not a PDF!
```

Submitting two blank PDFs:
```
Files are not different!
```

Submitting two different PDFs:
```
MD5 hashes do not match!
```

Submitting two different PDFs with matching MD5 hashes from:\
[md5-1.pdf](https://github.com/corkami/collisions/blob/master/examples/free/md5-1.pdf)\
[md5-2.pdf](https://github.com/corkami/collisions/blob/master/examples/free/md5-2.pdf)\
*index.php*
```HTML
// FLAG: picoCTF{c0ngr4ts_u_r_1nv1t3d_73b0c8ad}
```

### Flag
```
picoCTF{c0ngr4ts_u_r_1nv1t3d_73b0c8ad}
```