# keygenme-py
Category: Reverse Engineering\
Points: 30

## Description
[keygenme-trial.py](https://mercury.picoctf.net/static/b016c61bd2cc0be05a59da1dde67a2ac/keygenme-trial.py)

## Solution
Downloading and running the python script, we are greeted with a message.
```
$ python3 keygenme-trial.py 

===============================================
Welcome to the Arcane Calculator, GOUGH!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, GOUGH (a/b/c/d)?
```

It seems to be a trial version of a game. There's a few options of interest, the "Enter License Key" and the "[LOCKED]" option. There's no information on which stars we can travel to for option "a" so we'll get into the code.\

There's immmediatly some variables of interest. The dynamic key part seems to be something that's needed.
```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

Further down there's a *check key* function that uses the *username_trial* variable as input to the sha256 hash algorithm. Characters from the hash digest are chosen to make up the 8 characters of the *key_part_dynamic1_trial* variable.\

That code was separated out to make a small python program that outputs the expected dynamic key parts, instead of checking it.\

*keygen.py:*
```python
import hashlib

username_trial = b"GOUGH"

digest = hashlib.sha256(username_trial).hexdigest()

print(digest[4], digest[5], digest[3], digest[6],\
      digest[2], digest[7], digest[1], digest[8])
```

Running the script output the following characters:
```
$ python3 keygen.py 
f 9 1 1 a 4 8 6
```

Reconstructing the full flag, and using that as input to option *c*, results in unlocking the full game.

### Flag
```
picoCTF{1n_7h3_|<3y_of_f911a486}
```