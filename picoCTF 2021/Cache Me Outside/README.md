# Cache Me Outside
Category: Binary Exploitation\
Points: 70

## Description
While being super relevant with my meme references, I wrote a program to see how much you understand heap allocations. *nc mercury.picoctf.net 8054* [heapedit](https://mercury.picoctf.net/static/85f5530e5e150bf7d34b46fabbb11933/heapedit) [Makefile](https://mercury.picoctf.net/static/85f5530e5e150bf7d34b46fabbb11933/Makefile) [libc.so.6](https://mercury.picoctf.net/static/85f5530e5e150bf7d34b46fabbb11933/libc.so.6)

## Solution
Included in the provided files is the binary hosted on URL, the Makefile for the binary, and a libc shared library.

| Argument    | Purpose                                           |
| ----------- | ------------------------------------------------- |
| -Xlinker    | Pass following option to the linker               |
| -rpath=./   | Set run-time search path                          |
| -Wall       | Enable all warnings                               |
| -m64        | 64 bit architecture                               |
| -pedantic   | More strict warnings                              |
| -no-pie     | Disable address space layout randomization (ASLR) |
| --std=gnu99 | Use C99 standard                                  |


```
$ readelf -x .rodata heapedit

Hex dump of section '.rodata':
  0x00400b00 01000200 00000000 7200666c 61672e74 ........r.flag.t
  0x00400b10 78740000 00000000 596f7520 6d617920 xt......You may 
  0x00400b20 65646974 206f6e65 20627974 6520696e edit one byte in
  0x00400b30 20746865 2070726f 6772616d 2e004164  the program..Ad
  0x00400b40 64726573 733a2000 25640056 616c7565 dress: .%d.Value
  0x00400b50 3a200020 256300                     : . %c.
```

```
40086f:       e8 5c fe ff ff          callq  4006d0 <fgets@plt>
400874:       48 b8 74 68 69 73 20    movabs $0x2073692073696874,%rax
40087b:       69 73 20 
40087e:       48 ba 61 20 72 61 6e    movabs $0x6d6f646e61722061,%rdx
400885:       64 6f 6d 
400888:       48 89 45 90             mov    %rax,-0x70(%rbp)
40088c:       48 89 55 98             mov    %rdx,-0x68(%rbp)
400890:       48 b8 20 73 74 72 69    movabs $0x2e676e6972747320,%rax
400897:       6e 67 2e 
40089a:       48 89 45 a0             mov    %rax,-0x60(%rbp)
40089e:       c6 45 a8 00             movb   $0x0,-0x58(%rbp)
4008a2:       48 c7 85 68 ff ff ff    movq   $0x0,-0x98(%rbp)
4008a9:       00 00 00 00 
4008ad:       c7 85 64 ff ff ff 00    movl   $0x0,-0x9c(%rbp)
4008b4:       00 00 00 
4008b7:       eb 7a                   jmp    400933 <main+0x12c>
[...]
4008e9:       48 be 43 6f 6e 67 72    movabs $0x73746172676e6f43,%rsi // Contrats
[...]
400933:       83 bd 64 ff ff ff 06    cmpl   $0x6,-0x9c(%rbp)
```


### Flag
```
```