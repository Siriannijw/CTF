# $ python3 -c "print( chr(0) * (50000 - 32) + '\n' + chr(0) * 32 )"
#   | nc mercury.picoctf.net 20266
# ******************Welcome to our OTP implementation!******************
# This is the encrypted flag!
# 5b1e564b6e415c0e394e0401384b08553a4e5c597b6d4a5c5a684d50013d6e4b
# 
# What data would you like to encrypt? 
# [...] 
# Here ya go!
# 6227667c5c7865385c7862365c7831625c7839384b5c7864385c7861365e5c78

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