# crackme-py
Category: Reverse Engineering\
Points: 30

## Description
[crackme.py](https://mercury.picoctf.net/static/be2ba466c6154e42c756bf737ddcecc3/crackme.py)

## Solution
Edit the *crackme.py* script to use the *decode_secret* function at the bottom of the script, passing the *bezos_cc_secret* variable, to decode the flag.

```python
decode_secret(bezos_cc_secret)
```

### Flag
```
picoCTF{1|\/|_4_p34|\|ut_4593da8a}
```