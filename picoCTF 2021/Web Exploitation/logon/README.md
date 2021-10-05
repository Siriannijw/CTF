# logon
Category: Web Exploitation\
Points: 100

## Description
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? https://jupiter.challenges.picoctf.org/problem/13594/ ([link](https://jupiter.challenges.picoctf.org/problem/13594/)) or http://jupiter.challenges.picoctf.org:13594

## Solution
Loading the web page shows the following login screen.
![/index.html](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/logon/index.png?raw=true)

Clicking the *Sign In* button brings you to this page.
![/login](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/logon/login.png?raw=true)

In Firefox, the developer pane can be opened using the F12 key to access more details on the web page. Looking through the requests, the POST originally goes through */login*, and eventually */flag*. Looking at the headers, the */login* page *Response Headers* specifies "Set-Cookie: password=; username=; admin=False".
![Cookies!](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/logon/cookies.png?raw=true)

In Firefox, the *Response Headers* can be modified in the developer pane through *Resend > Edit and Resend*. Changing the *admin* cookie value to True, and resending the request, returns the flag page.
![Flag](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/logon/flag.png?raw=true)

This can also be done with curl using the arguments below:
```
$ curl -XGET --header "Cookie: password=; username=; admin=True" --output flag https://jupiter.challenges.picoctf.org/problem/13594/flag 
```

### Flag
```
picoCTF{th3_c0nsp1r4cy_l1v3s_d1c24fef}
```