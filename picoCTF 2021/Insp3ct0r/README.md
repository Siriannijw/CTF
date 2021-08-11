# Insp3ct0r
Category: Web Exploitation\
Points: 50

## Description
Kishor Balan tipped us off that the following code may need inspection: https://jupiter.challenges.picoctf.org/problem/41511/ ([link](https://jupiter.challenges.picoctf.org/problem/41511/)) or http://jupiter.challenges.picoctf.org:41511

## Solution
The description leads me to believe the flag is in the HTML of the web page. This can be viewed by downloading the HTML using *wget*, or by inspecting the web page in a browser by pressing the F11 key. Looking through the page source, there is a comment that gives part of the flag.\
*index.html*
```
<!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
```

The website also states:
```HTML
<p>I used these to make this site: <br/>
	HTML <br/>
	CSS <br/>
	JS (JavaScript)
</p>
```

The HTML header links to the CSS and JS files used to make the site:
```HTML
<link rel="stylesheet" type="text/css" href="mycss.css">
<script type="application/javascript" src="myjs.js"></script>
```

Those two files contained the last two pieces of the flag.
```
$ wget -q https://jupiter.challenges.picoctf.org/problem/41511/mycss.css
$ wget -q https://jupiter.challenges.picoctf.org/problem/41511/myjs.js
```
*mycss.css*
```
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
```
*myjs.js*
```
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?832b0699} */
```

### Flag
```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}
```