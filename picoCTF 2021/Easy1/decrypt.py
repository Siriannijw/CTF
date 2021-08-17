import string

ALPHABET = string.ascii_uppercase

def decode(e, k):
	index_e = ALPHABET.index(e)
	index_k = ALPHABET.index(k)
	index_d = (index_e - index_k) % len(ALPHABET)
	return ALPHABET[index_d]

enc = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

flag = ""
for i in range(len(enc)):
	flag += decode(enc[i], key[i])
print(flag)