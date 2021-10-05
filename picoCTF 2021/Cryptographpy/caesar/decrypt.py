import string

ALPHABET = string.ascii_lowercase

enc = "dspttjohuifsvcjdpoabrkttds"

for i in range(len(ALPHABET)):
	flag = ""
	for c in enc:
		offset = (ALPHABET.index(c) + i) % len(ALPHABET)
		flag += ALPHABET[offset]
	print(flag)
