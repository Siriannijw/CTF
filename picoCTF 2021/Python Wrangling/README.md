# Python Wrangling 
Category: General Skills\
Points: 10

## Description
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/ende.py) using [this password](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/pw.txt) to get [the flag](https://mercury.picoctf.net/static/1b247b1631eb377d9392bfa4871b2eb1/flag.txt.en)?

## Solution
The pw.txt contains a password.
```bash
$ cat pw.txt
dbd1bea4dbd1bea4dbd1bea4dbd1bea4
```

Running the python script with '-h' gives the following usage text.
```bash
$ python ende.py -h            
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'
```

Using the '-d' option and with the python script and intering the given password decodes 'flag.txt.en' and outputs the flag.
```bash
$ python ende.py -d flag.txt.en
Please enter the password:dbd1bea4dbd1bea4dbd1bea4dbd1bea4
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```

### Flag
```
picoCTF{4p0110_1n_7h3_h0us3_dbd1bea4}
```