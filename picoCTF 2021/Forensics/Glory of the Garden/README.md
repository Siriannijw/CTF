# Glory of the Garden
Category: Forensics\
Points: 50

## Description
This [garden](https://jupiter.challenges.picoctf.org/static/43c4743b3946f427e883f6b286f47467/garden.jpg) contains more than it seems.

## Solution
Looking at EXIF data didn't give any hints as to what could be different about the image. Changing over to a hex editor, it was quickly found at the end of the file using Ctrl+F looking for "picoCTF".
```
00230568:  666c 6167 2022 7069 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  :flag "picoCTF{more_than_
00230580:  6d33 3374 735f 7468 655f 3379 3336 3537 4261 4232 437d 220a  :m33ts_the_3y3657BaB2C}".
```

An easier way would be:
```
$ strings garden.jpg | grep picoCTF
Here is a flag "picoCTF{more_than_m33ts_the_3y3657BaB2C}"
```

### Flag
```
picoCTF{more_than_m33ts_the_3y3657BaB2C}
```