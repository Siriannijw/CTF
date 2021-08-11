# The Numbers
Category: Cryptography\
Points: 50

## Description
The [numbers](https://jupiter.challenges.picoctf.org/static/f209a32253affb6f547a585649ba4fda/the_numbers.png)... what do they mean?

## Solution
The image contains the following text:
```
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```
This appears to follow the flag formatting structure. Matching the first characters up with "picoCTF", it lines up with their position in the alphabet. Offsetting these values with the value of *ord('A')-1 (64)* in the ASCII and converting the decimal number should make them printable. The flag was obtained with the command below:
```
python -c "print(''.join([chr(n+64) for n in [16, 9, 3, 15, 3, 20, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]]))"
PICOCTFTHENUMBERSMASON
```

### Flag
```
PICOCTF{THENUMBERSMASON}
```