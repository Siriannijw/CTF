# caesar
Category: Cryptography\
Points: 100

## Description
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/6385b895dcb30c74dbd1f0ea271e3563/ciphertext).

## Solution
The Caesar cipher is a substitution algorithm. It's likely to be some sort of rotation, much like rot13.

*ciphertext*
```
picoCTF{dspttjohuifsvcjdpoabrkttds}
```

To find the offset of the rotation, I created the python script below that attempts each rotation possible of the alphabet.
```python
import string

ALPHABET = string.ascii_lowercase

enc = "dspttjohuifsvcjdpoabrkttds"

for i in range(len(ALPHABET)):
	flag = ""
	for c in enc:
		offset = (ALPHABET.index(c) + i) % len(ALPHABET)
		flag += ALPHABET[offset]
	print(flag)
```

The last one appears to be the correct offset.
```
$ python3 decrypt.py 
dspttjohuifsvcjdpoabrkttds
etquukpivjgtwdkeqpbcsluuet
furvvlqjwkhuxelfrqcdtmvvfu
gvswwmrkxlivyfmgsrdeunwwgv
hwtxxnslymjwzgnhtsefvoxxhw
ixuyyotmznkxahoiutfgwpyyix
jyvzzpunaolybipjvughxqzzjy
kzwaaqvobpmzcjqkwvhiyraakz
laxbbrwpcqnadkrlxwijzsbbla
mbyccsxqdrobelsmyxjkatccmb
nczddtyrespcfmtnzyklbuddnc
odaeeuzsftqdgnuoazlmcveeod
pebffvatgurehovpbamndwffpe
qfcggwbuhvsfipwqcbnoexggqf
rgdhhxcviwtgjqxrdcopfyhhrg
sheiiydwjxuhkrysedpqgziish
tifjjzexkyvilsztfeqrhajjti
ujgkkafylzwjmtaugfrsibkkuj
vkhllbgzmaxknubvhgstjcllvk
wlimmchanbylovcwihtukdmmwl
xmjnndiboczmpwdxjiuvlennxm
ynkooejcpdanqxeykjvwmfooyn
zolppfkdqeboryfzlkwxngppzo
apmqqglerfcpszgamlxyohqqap
bqnrrhmfsgdqtahbnmyzpirrbq
crossingtherubiconzaqjsscr
```

### Flag
```
picoCTF{crossingtherubiconzaqjsscr}
```