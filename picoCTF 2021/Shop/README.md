# Shop
Category: Reverse Engineering\
Points: 50

## Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://mercury.picoctf.net/static/a94b408ab46e6bd72f915d68be8aebc0/source). The shop is open for business at *nc mercury.picoctf.net 42159*.

## Solution

### Not So Easy...


### Just Run It

### T

```
$ ./source
Welcome to the market!
=====================
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option:
```

```
(gdb) info locals
inventory.cap = 4
inventory.len = 3
inventory.ptr = 0x1844a100
user_inv.cap = 4
user_inv.len = 3
user_inv.ptr = 0x1844a140
wallet = 40
(gdb) set var wallet = 100
(gdb) info locals
inventory.cap = 4
inventory.len = 3
inventory.ptr = 0x1844a100
user_inv.cap = 4
user_inv.len = 3
user_inv.ptr = 0x1844a140
wallet = 100
(gdb) c
Continuing.
You have 40 coins
        Item            Price   Count
(0) Quiet Quiches       10      12
(1) Average Apple       15      8
(2) Fruitful Flag       100     1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
panic: open flag.txt: no such file or directory
```

```
(gdb) info functions
All defined functions:

File /opt/hacksports/shared/staging/Shop_2_2090033420886329/problem_files/source.go:
        void main.check(error);
        void main.get_flag(void);
        void main.main(void);
        void main.menu([]main.item, []main.item, int, []main.item, []main.item, int);
        void main.openShop(void);
        void main.sell([]main.item, int, []main.item, int);
        void main.stockUp([]main.item, []main.item);
```

```
(gdb) call main.get_flag()
runtime: newstack at main.get_flag+0xfe sp=0x1843fbec stack=[0x1843e000, 0x18440000]
        morebuf={pc:0x1843fbff sp:0x1843fbf0 lr:0x0}
        sched={pc:0x80d453e sp:0x1843fbec lr:0x0 ctxt:0x0}
runtime: unknown pc 0x1843fbff
```


### Flag
```
```