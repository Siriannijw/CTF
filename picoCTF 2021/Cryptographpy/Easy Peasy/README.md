# Easy Peasy
Category: Cryptography\
Points: 40

## Description
A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) *nc mercury.picoctf.net 20266* [otp.py](https://mercury.picoctf.net/static/84c434ada6e2f770b5000292cadae7eb/otp.py)

## Solution

### Code Analysis
The code operates as follows:

1. *startup* function
   - Loads the flag file
   - Loads the key file
   - XOR the flag with the key
   - Output the encrypted text as two hex values per character
   - Return the current position in the key

2. *encrypt* function loop
   - Input string from the user
   - XOR the input with the key starting at the last key position
   - Output the encrypted text as two hex values per character
   - Return the current position in the key

The critical vulnerability begins on line 34 of the *encrypt* function. When the stop key position exceeds the KEY_LEN of 50000 bytes, the program reuses the key from the beginning. This is insecure, because one-time pad is only supposed to be used *once*. Since we are able to control the input and reuse the section of the key previously used to encrypt the flag, the key can be derived.

### Getting The Key
The URL and port name provided in the description is a server hosting the same python script. Using netcat, there's the following output:
```
$ nc mercury.picoctf.net 20266 
******************Welcome to our OTP implementation!******************
This is the encrypted flag!
5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b

What data would you like to encrypt?
```

To obtain the key, pass 50,000 zeroed bytes to the program, and the resulting XOR will be the key. 
```
$ python3 -c "print( chr(0) * (50000 - 32) + '\n' + chr(0) * 32)" | nc mercury.picoctf.net 20266
[...]
What data would you like to encrypt? Here ya go!
6227667c5c7865385c7862365c7831625c7839384b5c7864385c7861365e5c78
```

### Decrypting The Flag
We now have the key in hex. To decrypt the flag, the python script decodes the flag and key hex strings into integers, and XOR's them together, and converts the integers back into ASCII characters.

*decrypt.py*
```python
# Convert hex string to integer array
def hex_to_int(h, byte=2):
	result = []
	for i in range(0, len(h), byte):
		result.append(int(''.join(h[i:i+byte]), 16))
	return result

# XOR given otp with encrypted text
def decrypt(otp, et):
	result = ''
	for i in range(len(et)):
		result += chr(et[i] ^ otp[i])
	return result

# hex encoded otp
hex_otp = '6227667c5c7865385c7862365c7831625c7839384b5c7864385c7861365e5c78'
otp = hex_to_int(hex_otp)

# This is the encrypted flag!
hex_ef = '5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b'
ef = hex_to_int(hex_ef)

flag = decrypt(otp, ef)
print(flag)
```

### Flag
```
picoCTF{99072996e6f7d397f6ea0128b4517c23}
```