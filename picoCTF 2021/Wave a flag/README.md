# Wave a flag
Category: General Skills\
Points: 10

## Description
Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a00f554b16385d9970dae424f66ee1ab/warm) has extraordinarily helpful information...

## Solution
Downloading and running the given binary resulted in the following:
```bash
$ ./warm
-bash: ./warm: Permission denied
```

Adding the execution flag allowed the program to run and output the flag
```bash
$ chmod +x warm
$ ./warm
$ ./warm
Hello user! Pass me a -h to learn what I can do!
$ ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```

### Flag
```
picoCTF{b1scu1ts_4nd_gr4vy_18788aaa}
```