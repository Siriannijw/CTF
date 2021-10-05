# First Grep
Category: General Skills\
Points: 100

## Description
Can you find the flag in [file](https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file)? This would be really tedious to look through manually, something tells me there is a better way.

## Solution
Per the description, use grep to find the flag:
```
$ wget -q https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file
$ grep picoCTF file 
picoCTF{grep_is_good_to_find_things_dba08a45}
```

### Flag
```
picoCTF{grep_is_good_to_find_things_dba08a45}
```