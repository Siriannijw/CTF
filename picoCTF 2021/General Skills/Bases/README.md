# Bases
Category: General Skills\
Points: 100

## Description
What does this **bDNhcm5fdGgzX3IwcDM1** mean? I think it has something to do with bases.

## Solution
The flag is encoded using base64.
```
$ echo bDNhcm5fdGgzX3IwcDM1 | base64 -d
l3arn_th3_r0p35
```

### Flag
```
picoCTF{l3arn_th3_r0p35}
```