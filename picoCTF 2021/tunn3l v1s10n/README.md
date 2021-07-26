# tunn3l v1s10n
Category: Forensics\
Points: 40

## Description
We found this [file](https://mercury.picoctf.net/static/d0129ad98ba9258ab59e7700a1b18c14/tunn3l_v1s10n). Recover the flag.

## Solution
The *file* utility reported the file to be data. Looking at the hex output of the file suggests that it's a bitmap image.
```
$ xxd tunn3l_v1s10n | head -n4
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
```

Trying to open it as an image doesn't seem to work. Converting it to a PNG gives a partial image.\
Looking closer at the hex values, in the context of the bitmap fields, the image offset and header size are not what they're supposed to be.

| Field          | Bytes   | Value   | Hex         |
| -------------- | ------- | ------- | ----------- |
| File Signature | 1  - 2  |         | 42 4d       |
| Image size     | 3  - 6  | 2893454 | 8e 26 2c 00 |
| Must be zero   | 7  - 10 | 0       | 00 00 00 00 |
| Image offset   | 11 - 14 | 47824   | ba d0 00 00 |
| Header size    | 15 - 18 | 47824   | ba d0 00 00 |
| Image Width    | 19 - 22 | 1134    | 6e 04 00 00 |
| Image Height   | 23 - 26 | 306     | 32 01 00 00 |
| Num of Planes  | 27 - 28 | 1       | 01 00       |
| Bits per pixel | 29 - 30 | 24      | 18 00       |

Correcting the *image offset* and *header size* values to *0x36* and *0x28*, respectively, caused a new image to appear. After some increasing of the *image height* field, the flag was revealed.
```
$ xxd -p tunn3l_v1s10n > tunn3l_v1s10n.hex
$ vim tunn3l_v1s10n.hex
$ xxd -r -p > tunn3l_v1s10n.bmp
```

### Flag
```
picoCTF{qu1t3_a_v13w_2020}
```