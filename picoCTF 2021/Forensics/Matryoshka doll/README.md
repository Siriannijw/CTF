# Matryoshka doll
Category: Forensics\
Points: 30

## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](https://mercury.picoctf.net/static/5eb456e480e485183c9c1b16952c6eda/dolls.jpg)

## Solution
The image in the description looks to be a picture of a nesting doll. There were a few things wrong with it though. The *exif* program says that the file is corrupt.
```
$ exif dolls.jpg
Corrupt data
The data provided does not follow the specification.
ExifLoader: The data supplied does not seem to contain EXIF data.
```

Looking at the file header and footer, the image is a PNG, not a JPG. The footer also doesn't appear to match any type.
```
$ hd dolls.jpg | head -n1
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
$ hd dolls.jpg | tail -n3
0009f160  05 06 00 00 00 00 01 00  01 00 59 00 00 00 99 c8  |..........Y.....|
0009f170  05 00 00 00                                       |....|
```

Searching the file for the PNG footer, the bytes following the PNG footer matches a zip header.
```
$ hd dolls.jpg | grep "ae 42 60 82"
00042860  00 00 00 00 49 45 4e 44  ae 42 60 82 50 4b 03 04  |....IEND.B`.PK..|
```

Unzipping the file a few times reveals the flag.
```
$ unzip dolls.jpg
Archive:  dolls.jpg
warning [dolls.jpg]:  272492 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/2_c.jpg
$ cd base_images/
$ unzip 2_c.jpg
Archive:  2_c.jpg
warning [2_c.jpg]:  187707 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/3_c.jpg
$ cd base_images/
$ unzip 3_c.jpg
Archive:  3_c.jpg
warning [3_c.jpg]:  123606 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: base_images/4_c.jpg
$ cd base_images/
$ unzip 4_c.jpg
Archive:  4_c.jpg
warning [4_c.jpg]:  79578 extra bytes at beginning or within zipfile
  (attempting to process anyway)
  inflating: flag.txt
$ cat flag.txt
picoCTF{336cf6d51c9d9774fd37196c1d7320ff}
```

### Flag
```
picoCTF{336cf6d51c9d9774fd37196c1d7320ff}
```