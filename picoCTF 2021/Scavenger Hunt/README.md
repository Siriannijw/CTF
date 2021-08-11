# Scavenger Hunt
Category: Web Exploitation\
Points: 50

## Description
There is some interesting information hidden around this site [http://mercury.picoctf.net:39491/](http://mercury.picoctf.net:39491/). Can you find it?

## Solution
This challenge was similar to Insp3ct0r
```
$ wget -q http://mercury.picoctf.net:39491/
$ wget -q http://mercury.picoctf.net:39491/mycss.css
$ wget -q http://mercury.picoctf.net:39491/myjs.js
```

First part of code in the HTML.\
*index.html*
```HTML
<!-- Here's the first part of the flag: picoCTF{t -->
```

Second part in the CSS.\
*mycss.css*
```CSS
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

It's different at the Javascript, which mentions Google indexing.
*myjs.js*
```Javascript
/* How can I keep Google from indexing my website? */
```

Search engine indexing is configurable through the *robots.txt* file.
```
$ wget -q http://mercury.picoctf.net:39491/robots.txt
$ cat robots.txt
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

The next part mentions that the server is Apache. This could be a number of things. Common mods are are mod_status and mod_info which default to the pages pages on */server-status* and */server-info* respectively. These were not availble. Another thought was the Apache configuration file, *.htaccess*, which had the next part of the flag.
```
$ wget -q http://mercury.picoctf.net:39491/.htaccess
$ cat .htaccess
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

The next clue mentions Macs. The previous flag makes be think that the Apache server is hosting a directory with no fettering. MacOS creates *.DS_Store* files anytime a folder is indexed by *Finder*. The commands below got hte last part of the flag.
```
$ wget -q http://mercury.picoctf.net:39491/.DS_Store
$ cat .DS_Store
Congrats! You completed the scavenger hunt. Part 5: _f7ce8828}
```

### Flag
```
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_f7ce8828}
```