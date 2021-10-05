FLAG = "brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm"
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')

DICTIONARY = []
with open('/usr/share/dict/words') as f:
	DICTIONARY = f.readlines()
DICTIONARY = set([line.lower().replace("'s", "") for line in DICTIONARY])

STUDY_GUIDE = []
with open('public/study-guide.txt') as f:
	STUDY_GUIDE = f.readlines()
STUDY_GUIDE = [line.strip() for line in STUDY_GUIDE]

DIC_FREQUENCY = dict(zip(ALPHABET, [0] * len(ALPHABET)))
DIC_TOTAL = 0
for word in DICTIONARY:
	for letter in word:
		if letter in DIC_FREQUENCY:
			DIC_FREQUENCY[letter] += 1
			DIC_TOTAL += 1
for f in DIC_FREQUENCY:
	DIC_FREQUENCY[f] /= DIC_TOTAL / 100

ENC_FREQUENCY = dict(zip(ALPHABET, [0] * len(ALPHABET)))
ENC_TOTAL = 0
for word in STUDY_GUIDE:
	for letter in word:
		if letter in ENC_FREQUENCY:
			ENC_FREQUENCY[letter] += 1
			ENC_TOTAL += 1
for f in ENC_FREQUENCY:
	if ENC_FREQUENCY[f]:
		ENC_FREQUENCY[f] /= ENC_TOTAL / 100

PERMUTATION = dict(zip( \
		sorted(DIC_FREQUENCY.keys(), key=lambda key: DIC_FREQUENCY[key]), \
		sorted(ENC_FREQUENCY.keys(), key=lambda key: ENC_FREQUENCY[key])))

def printPermutation(dic):
	for d in dic:
		print(d, '{:.2f}'.format(dic[d]))

def decrypt(enc, dic):
	return ''.join([
        dic[e]
        if e in dic else e
        for e in enc
    ])

# Decrypt words with permutation and check dictionary
def check(dictionary):
	total = 0;
	for enc in STUDY_GUIDE:
		dec = decrypt(enc, dictionary)
		if dec in DICTIONARY:
		 	total += 1;
	return total

# Hash Permutation Algorithm
def permutation(keys, perm, size):
	res = {}

	if size is 1:
		p = dict(zip(keys, perm))
		res[check(p)] = p
		return res
	for i in range(size):
		res.update(permutation(keys, perm, (size - 1)))
		print(res)
		if (size % 2) is 1:
			perm[0], perm[size - 1] = perm[size - 1], perm[0]
		else:
			perm[i], perm[size - 1] = perm[size - 1], perm[i]
	return res


# if not permutaiton(ALPHABET, len(ALPHABET)):
# 	print("permutation not found")
# print(check(PERMUTATION))

# printPermutation(DIC_FREQUENCY)
# printPermutation(ENC_FREQUENCY)
# print(PERMUTATION)

perm = {}
perm.update(dict(zip(list('mwnflicimwbfrtqlvcwnflicirvfxtr'), list('dichlorodiphenyltrichloroethane'))))
perm.update(dict(zip(list('nqnlivcwsrvfqlrtrvcwtwvcxswtr'), list('cyclotrimethylenetrinitramine'))))
perm.update(dict(zip(list('vcwtwvcibfrtqlsrvfqltwvcxswtr'), list('trinitrophenylmethylnitramine'))))
perm.update(dict(zip(list('xtvwmwaravxulwafsrtvxcwxtwas'), list('antidisestablishmentarianism'))))
perm.update(dict(zip(list('fqmcizqmrfqmcinicvwniavrcitr'), list('hydroxydehydrocorticosterone'))))
perm.update(dict(zip(list('swnciabrnvcibfivisrvcwnxllq'), list('microspectrophotometrically'))))
perm.update(dict(zip(list('vfqcibxcxvfqciwmrnviswkr'), list(''))))
perm.update(dict(zip(list('yicsxlmrfqmraolbfizqlwn'), list(''))))

keys = list(set(ALPHABET) - set(perm.keys()))
vals = list(set(ALPHABET) - set(perm.values()))
size = len(keys)
print('len(keys)', len(keys))
print('len(vals)', len(vals))
print(perm)
print(keys)
print(vals)

res = dict(permutation(keys, vals, size))
perm.update(res[sorted(res)[-1]])
print(decrypt(FLAG, perm))