# advanced-potion-making
Category: Forensics\
Points: 100

## Description
Ron just found his own copy of advanced potion making, but its been corrupted by some kind of spell. Help him recover it!\

Download advanced-potion-making: [advanced-potion-making](https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making)

## Solution
First things I checked when downloading a corrupted image was to check for a file type. File just says data. Strings also showed mostly garbage, except for a notable *IEND* at the end. This is a clear endicator of the final chuck in a PNG.
```
$ wget -q https://artifacts.picoctf.net/picoMini+by+redpwn/Forensics/advanced-potion-making/advanced-potion-making
$ file advanced-potion-making
advanced-potion-making: data
$ strings advanced-potion-making
[...]
IEND
```

Checking the first 4 bytes, the 2nd and 3rd byte differ from the PNG file signature *8950 4d47 0d0a 1a0a*. Fixing this didn't make the image parsable.
```
$ xxd advanced-potion-making | head -n 4
00000000: 8950 4211 0d0a 1a0a 0012 1314 4948 4452  .PB.........IHDR
00000010: 0000 0990 0000 04d8 0802 0000 0004 2de7  ..............-.
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
```

Following the file signature are chunks of data. The format is as follows:
| Length  | Chunk type | Chunk data | CRC     |
| ------- | ---------- | ---------- | ------- |
| 4 bytes | 4 bytes    | *Length*   | 4 bytes |

The first chunk is always *IHDR* with a fixed 13 (0000 000d) bytes. The specified length, *0012 1314*, is incorrect. Fixing this resulted in an all red image.\

Filling in the image revealed the flag.
![advanced-potion-making.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/advanced-potion-making/advanced-potion-making.png?raw=true)

### Flag
```
picoCTF{w1z4rdry}
```