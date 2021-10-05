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