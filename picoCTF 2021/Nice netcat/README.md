# Nice netcat...
Category: General Skills\
Points: 10

## Description
There is a nice program that you can talk to by using this command in a shell: **$ nc mercury.picoctf.net 22902**, but it doesn't speak English...

## Solution
Running the given command results in a line-delineated list of numbers.
```
$ nc mercury.picoctf.net 22902
112 
105 
99 
...
```

Pipe that through awk and convert the integer into a decimal gives the flag.
```
$ nc mercury.picoctf.net 22902 | awk '{printf "%c", $0}'
picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}
```

### Flag
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_d3dfd6df}
```