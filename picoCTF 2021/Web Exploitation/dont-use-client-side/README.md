# dont-use-client-side
Category: Web Exploitation\
Points: 100

## Description
Can you break into this super secure portal? *https://jupiter.challenges.picoctf.org/problem/37821/* ([link](https://jupiter.challenges.picoctf.org/problem/37821/)) or http://jupiter.challenges.picoctf.org:37821

## Solution
Loading the web page, there's a password input field, with a button to verify the given password. The input field in the HTML on the web page calls a *verify* method from the onClick attribute. Within the HTML there is a script tag that defines the *verify* method. The method checks the passphrase by comparing it against segments of the expected phrase. Piecing those pieces together in order gives the flag.
```Javascript
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'a3c8') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_1') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '9}') {
                  alert("Password Verified")
[...]
```

### Flag
```
picoCTF{no_clients_plz_1a3c89}
```