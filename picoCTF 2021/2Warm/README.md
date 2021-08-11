# 2Warm
Category: General Skills\
Points: 50

## Description
Can you convert the number 42 (base 10) to binary (base 2)? 

## Solution
Using the built-in *bin* function in python prints out the binary equivalent.
```
$ python -c "print(bin(42))"
0b101010
```
Remove the preceding '0b' and format the flag.\

This can also be accomplished by hand.

| 32 | 16 | 8 | 4 | 2 | 1 |
| -- | -- | - | - | - | - |
| 1  | 0  | 1 | 0 | 1 | 0 |

32 + 8 + 2 = 42

### Flag
```
picoCTF{101010}
```