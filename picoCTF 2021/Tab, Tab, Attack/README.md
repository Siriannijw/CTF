# Tab, Tab, Attack
Category: General Skills\
Points: 20

## Description
Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip)

## Solution
This one was fairly stright forward to get. Download, unzip, and run the zipped binary.
```
$ wget https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip
--2021-07-06 19:24:05--  https://mercury.picoctf.net/static/3afd18a65e42b80526aa87f9766c588b/Addadshashanammu.zip
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4520 (4.4K) [application/octet-stream]
Saving to: 'Addadshashanammu.zip'

Addadshashanammu.zip                         100%[=============================================================================================>]   4.41K  --.-KB/s    in 0s      

2021-07-06 19:24:05 (658 MB/s) - 'Addadshashanammu.zip' saved [4520/4520]

$ unzip Addadshashanammu.zip 
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet  
$ ./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet 
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}
```

### Flag
```
picoCTF{l3v3l_up!_t4k3_4_r35t!_d32e018c}
```