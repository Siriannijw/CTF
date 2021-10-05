import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(enc):
	dec = ""
	for i in range(0, len(enc), 2):
		e1 = ALPHABET.index(enc[i])
		e2 = ALPHABET.index(enc[i+1])
		d1 = "{0:04b}".format(e1)
		d2 = "{0:04b}".format(e2)
		dec += chr(int(d1 + d2, 2))
	return dec

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

for key in ALPHABET:
	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	enc = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
	b16 = ""
	for i, c in enumerate(enc):
		b16 += shift(c, key[i % len(key)])

	flag = b16_decode(b16)
	print(flag)
