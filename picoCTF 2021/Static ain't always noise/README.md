# Static ain't always noise
Category: General Skills\
Points: 20

## Description
Can you look at the data in this binary: [static](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/static)? This [BASH script](https://mercury.picoctf.net/static/ff4e569d6b49b92d090796d4631a2577/ltdis.sh) might help!

## Solution
Ignoring the fact you can *cat* the static file and see the flag, I downloaded the script included in the description. The script appears to run *objdump* on the static binary and run the output through *strings*. The commands below resulted in finding the flag.
```
$ ./ltdis.sh       
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
$ ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
$ cat static.ltdis.strings.txt | grep picoCTF
   1020 picoCTF{d15a5m_t34s3r_ccb2b43e}
```

### Flag
```
picoCTF{d15a5m_t34s3r_ccb2b43e}
```