# GET aHEAD
Category: Web Exploitation\
Points: 20

## Description
Find the flag being held on this server to get ahead of the competition [http://mercury.picoctf.net:47967/](http://mercury.picoctf.net:47967/)

## Solution
Originally I looked at the page source was messing with GET and POST requests. However, I read the description again and realized it was much simpler...

The HTTP HEAD method requests ONLY the HTTP headers, which can be useful for browsers to get the expected size before downloading. In this case, the flag was returned as a header.
```
$ curl -I http://mercury.picoctf.net:47967/
HTTP/1.1 200 OK
flag: picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}
Content-type: text/html; charset=UTF-8
```

### Flag
```
picoCTF{r3j3ct_th3_du4l1ty_cca66bd3}
```