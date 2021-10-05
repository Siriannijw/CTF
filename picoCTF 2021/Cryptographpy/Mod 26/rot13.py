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