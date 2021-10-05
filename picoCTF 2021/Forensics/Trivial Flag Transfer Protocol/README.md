# Trivial Flag Transfer Protocol
Category: Forensics\
Points: 90

## Description
Figure out how they moved the [flag](https://mercury.picoctf.net/static/88553d672efbccbc5868002f4c6eb737/tftp.pcapng).

## Solution
Briefly looking at the packet capture in Wireshark, there are TFTP packets. There appears to be requests for files. Files can be extracted from a TFTP session in Wireshark by doing the following: File > Export Objects > TFTP... > Save All
```
instructions.txt
plan 
program.deb
picture1.bmp
picture2.bmp
picture3.bmp
```

*instructions.txt*
```
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

*plan*
```
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```

The two text files appear to be some kind of cipher. Attempting rot13 gave teh following output:
```
$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
$ cat instructions.txt | rot13
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
$ cat plan | rot13
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

The debian package is for steghide, a program which hides data inside an existing file.
```
$ dpkg-deb -I program.deb 
 new Debian package, version 2.0.
 size 138310 bytes: control archive=1250 bytes.
     826 bytes,    18 lines      control              
    1184 bytes,    17 lines      md5sums              
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.
```

Installing steghide and using the passpharse **DUEDILIGENCE** from the *plan* file gave the flag on *picture3.bmp*.
```
$ steghide extract -sf picture1.bmp -p DUEDILIGENCE
steghide: could not extract any data with that passphrase!
$ steghide extract -sf picture2.bmp -p DUEDILIGENCE
steghide: the file format of the file "picture2.bmp" is not supported.
$ steghide extract -sf picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".
$ cat flag.txt 
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```

### Flag
```
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```