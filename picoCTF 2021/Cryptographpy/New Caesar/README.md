# New Caesar
Category: Cryptography\
Points: 60

## Description
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) *kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm* [new_caesar.py](https://mercury.picoctf.net/static/d9c139d91d2dfec8fd197ca6d970381a/new_caesar.py)

## Solution
The description provides an encrypted flag and the respective python file used to encrypt it, sans the original flag and key.\

The core of the encryption involves encoding the flag and then shifting the resulting characters using the key.
```python
b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```

The encoding process splits each character into two. This is accomplished by splitting the ASCII character's binary value and mapping that two the first 16 characters in the alphabet.
```python
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc
```

The shifting function uses the character **key[i % len(key)]** to offset the encoded character.
```python
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
```

Now that the algorithm is understood, the missing key is... the key. Fortunately, assertions left in the code show that the key is simply 1 character from the first 16 bytes in the alphabet.
```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

[...]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1
```

After understanding the encryption algorithm, I created the following script that did the reverse of *new_caesar.py* to retrieve the flag.
```python
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# Recombine character encoding
def b16_decode(enc):
	dec = ""
	for i in range(0, len(enc), 2):
		e1 = ALPHABET.index(enc[i])
		e2 = ALPHABET.index(enc[i+1])
		d1 = "{0:04b}".format(e1)
		d2 = "{0:04b}".format(e2)
		dec += chr(int(d1 + d2, 2))
	return dec

# Unshift bytes
def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	# Add instead of subtract offset
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

# Attempt all characters in the encoding alphabet
for key in ALPHABET:
	assert all([k in ALPHABET for k in key])
	assert len(key) == 1

	# Encrypted flag from the description
	enc = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

	# Everything's in reverse so shift first
	b16 = ""
	for i, c in enumerate(enc):
		b16 += shift(c, key[i % len(key)])

	# Decode shifted characters
	flag = b16_decode(b16)
	print(flag)
```

Out of all the outputs, the line below was the closest to readable text. Submitting as a formatted flag resulted in points.
```
[...]
et_tu?_1ac5f3d7920a85610afeb2572831daa8
[...]
```

### Flag
```
picoCTF{et_tu?_1ac5f3d7920a85610afeb2572831daa8}
```