# Transformation
Category: Reverse Engineering\
Points: 20

## Description
I wonder what this really is... [enc](https://mercury.picoctf.net/static/0d3145dafdc4fbcf01891912eb6c0968/enc) **''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])**

## Solution
The code in the description is python code that encodes two UTF-8 characters into a UTF-16 character. To decode them a python script was made to split the UTF-16 characters into two bytes and convert each into its previous UTF-8 character.
```python
with open('enc', 'r') as f:
    #The original file
    enc = f.read()
    print(enc)
    
    flag = ''
    for i in range(0, len(enc)):
        o = ord(enc[i])
        one = o >> 8    # Shift off the 8 right-most bits to get the left-most bits
        two = o & 0xFF  # AND with all 1's in the 8 right-most bits to get the right-most bits
        flag += chr(one)
        flag += chr(two)
    print(flag)
```

### Flag
```
picoCTF{16_bits_inst34d_of_8_26684c20}
```