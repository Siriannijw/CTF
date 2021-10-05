# 13
Category: Cryptography\
Points: 100

## Description
Cryptography can be easy, do you know what ROT13 is? *cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}*

## Solution
This challenge can be solved by running the cipher text through the rot13 algorithm.
```
$ alias rot13="tr 'A-Za-z' 'N-ZA-Mn-za-m'"
$ echo cvpbPGS{abg_gbb_onq_bs_n_ceboyrz} | rot13
picoCTF{not_too_bad_of_a_problem}
```

### Flag
```
picoCTF{not_too_bad_of_a_problem}
```