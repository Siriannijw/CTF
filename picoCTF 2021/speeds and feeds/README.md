# speeds and feeds
Category: Reverse Engineering\
Points: 50

## Description
There is something on my shop network running at *nc mercury.picoctf.net 59953*, but I can't tell what it is. Can you?

## Solution
Connecting to the socket in the description results quite a bit of output. Pushing that to a file, there's over 1000 lines that all looks similar to the text below:
```
$ nc mercury.picoctf.net 59953
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
G0X0.8276Y3.8621
[...]
```
G0Z0.1 is repeated quite a number of times. Searching that, resulted in mentions of G-Code for CNC machines.\

Using [https://ncviewer.com/](https://ncviewer.com/), the flag was viewable.
![picoCTF{num3r1cal_c0ntr0l_f3fea95b}](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/speeds%20and%20feeds/speeds%20and%20feeds.png?raw=true)

### Flag
```
picoCTF{num3r1cal_c0ntr0l_f3fea95b}
```