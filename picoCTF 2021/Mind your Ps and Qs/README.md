# Mind your Ps and Qs
Category: Cryptography\
Points: 20

## Description
In RSA, a small *e* value can be problematic, but what about *N*? Can you decrypt this? [values](https://mercury.picoctf.net/static/38f30029ab93478310e906d3d084a4c1/values)

## Solution
The challenge description mentions RSA, along with the title 'Mind your Ps and Qs'. This suggested to me that we need to calculate the decryption key for RSA.\

After refreshing on the RSA algorithm, *n* is the product of two prime numbers. With *n* being such a large prime number, it took a bit to find a site that could calculate using BigInteger. Luckily, [decode.fr](https://www.dcode.fr/prime-factors-decomposition) provided the option, and managed to output *p* and *q* in a few minutes.

I implemented the rest of the RSA algorithm in python.
```python
# Values
c = 240986837130071017759137533082982207147971245672412893755780400885108149004760496
n = 831416828080417866340504968188990032810316193533653516022175784399720141076262857
e = 65537

# Prime factorization of n via https://www.dcode.fr/prime-factors-decomposition
# n = p * q
p = 1593021310640923782355996681284584012117
q = 521911930824021492581321351826927897005221

# ϕ(n) = (p - 1) * (q - 1)
N = (p - 1) * (q - 1)

# Decryption key
# d = e^-1 mod ϕ(n)
d = pow(e, -1, N)

# Message
# m = c^d mod n
decode = pow(c, d, n)
print(decode)
```

The script output the following:
```
13016382529449106065927291425342535437996222135352905256639592405461024281868413
```

After some thought, I appended the code snippit below that converts the number to binary and outputs each byte as a char.
```python
# Binary with '0b' prefix removed
binary = bin(decode)[2:]

# Pad binary
rem = len(binary) % 8
pad = 8 - rem
prefix = '0' * pad
binary = prefix + binary

# Convert bytes to chars
flag = ''
for n in range(0, len(binary), 8):
	byte = binary[n:n+8]
	flag += chr(int(str(byte), 2))
print(flag)
```

### Flag
```
picoCTF{sma11_N_n0_g0od_23540368}
```