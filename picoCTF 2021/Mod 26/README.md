# Mod 26
Category: Cryptography\
Points: 10

## Description
Cryptography can be easy, do you know what ROT13 is?\
**cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}**

## Solution
The description informs that the given cipher text was encoded with ROT13. To decipher the text, a python implementation was made below.
```python
# Encoded text
synt = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"

OFF_a = 97  # 'a' ASCII decimal value
OFF_A = 65  # 'A' ASCII decimal value
ROT = 13    # Rotation offset
MOD = 26    # Modulus - Number of alphabet characters

# ROT13 cipher
def rot13(c, offset):
    o = ord(c)
    o -= offset
    o += ROT
    o %= MOD
    o += offset
    return chr(o)

# Rotate only alpha characters
def decode(c):
    if c.islower():
        return rot13(c, OFF_a)
    elif c.isupper():
        return rot13(c, OFF_A)
    else:
        return c

flag = ''.join([decode(c) for c in synt])
print(flag)
```

### Flag
```
picoCTF{next_time_I'll_try_2_rounds_of_rot13_TLcKBUdK}
```