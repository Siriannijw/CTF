# login
Category: Web Exploitation\
Points: 100

## Description
My dog-sitter's brother made this website but I can't get in; can you help?

[login.mars.picoctf.net](https://login.mars.picoctf.net/)

## Solution
The web page is simple.
![index.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/login/index.png?raw=true)

Looking at the HTML source code, there's an input form for the username and password. In the head element, there's a reference to *index.js*. That can be pulled using *wget https://login.mars.picoctf.net/index.js*. The JavaScript adds an event listener to  *submit* which checks the username and password. Submitted values are encoded in base 64 and checked against hard coded strings.\

*index.js*
```Javascript
"YWRtaW4"!==t.u?
alert("Incorrect Username"):

"cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ"!==t.p?
alert("Incorrect Password"):

void alert(`Correct Password! Your flag is ${atob(t.p)}.`);
```

Decoding those reveals the plaintext username and password.
```
$ echo YWRtaW4= | base64 -d
admin
$ echo cGljb0NURns1M3J2M3JfNTNydjNyXzUzcnYzcl81M3J2M3JfNTNydjNyfQ== | base64 -d
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```

### Flag
```
picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}
```