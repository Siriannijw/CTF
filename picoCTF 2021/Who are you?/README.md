# Who are you?
Category: Web Exploitation\
Points: 100

## Description
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn [http://mercury.picoctf.net:38322/](http://mercury.picoctf.net:38322/)

## Solution
For this challenge, I used wget. Starting out, Looking at the page source, there's a message.\
*index.html*
```HTML
<h3 style="color:red">Only people who use the official PicoBrowser are allowed on this site!</h3>
```

Browsers are able to specify their name and version using the **User-Agent** header field. This is configurable in wget by adding the argument *--user-agent=PicoBrowser*.\
*index.html.1*
```HTML
<h3 style="color:red">I don&#39;t trust users visiting from another site.</h3>
```

Browsers are able to specify which site they are comming from using the **Referer** header field. This is configurable in wget by adding the argument *--referer=http://mercury.picoctf.net:38322/*.\
*index.html.2*
```HTML
<h3 style="color:red">Sorry, this site only worked in 2018.</h3>
```

Browsers are able to specify the system time using the **Date** header field. This is configurable in wget by adding the argument *--header="Date: Mon, 18 Jan 2018 02:36:04 GMT"*.\
*index.html.3*
```HTML
<h3 style="color:red">I don&#39;t trust users who can be tracked.</h3>
```

Browsers are able to request Do-Not-Track from websites using the **DNT** header field. This is configurable in wget by adding the argument *--header="DNT: 1"*.\
*index.html.4*
```HTML
<h3 style="color:red">This website is only for people from Sweden.</h3>
```

This one was annoying because it could have been a number of different header fields, including *Content-Language*, *Accept-Language*, *X-Country-Code* or many other non-standard headers that are used accross all web servers. The answer ended up being the **X-Forwarded-For** header field. Any IP within Sweden's allocated IP blocks can then be used as the value. This is configurable in wget by adding the argument *--header="X-Forwarded-For: 2.21.64.0"*.\
*index.html.5*
```HTML
<h3 style="color:red">You&#39;re in Sweden but you don&#39;t speak Swedish?</h3>
```

From our trials and tribulations from the last page, browsers are able to specify the expected language using the **Accept-Language** header field. This is configurable in wget by adding the arugment *--header="Accept-Language: sv"*.\
*index.html.6*
```HTML
<b>picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_b22d773c}</b>
```

Below is the final command used to get the flag:
```
$ wget -q --user-agent="PicoBrowser" --referer=http://mercury.picoctf.net:38322/ --header="Date: Mon, 18 Jan 2018 02:36:04 GMT" --header="DNT: 1" --header="X-Forwarded-For: 2.21.64.0" --header="Accept-Language: sv" http://mercury.picoctf.net:38322/
```

### Flag
```
picoCTF{http_h34d3rs_v3ry_c0Ol_much_w0w_b22d773c}
```