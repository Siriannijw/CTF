# MacroHard WeakEdge
Category: Forensics\
Points: 60

## Description
I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm)

## Solution
The file provided is a *.pptm*. This is a powerpoint file that contains macros. Using LibreOffice Impress, macro's can be viewed at *Tools > Macros > Organize Macros > LibreOffice Basic*. There was only one macro with the code below:
```VBAModule
Rem Attribute VBA_ModuleType=VBAModule
Sub Module1
Rem Sub not_flag()
Rem     Dim not_flag As String
Rem     not_flag = "sorry_but_this_isn't_it"
Rem End Sub
Rem 
End Sub
```

The *.pptm* format is actually a zip with a specific archive structure. Unzipping and searching the folder did not show any results.
```
$ wget -q https://mercury.picoctf.net/static/9a7436948cc502e9cacf5bc84d2cccb5/Forensics%20is%20fun.pptm
$ unzip -q -d Forensics\ is\ fun Forensics\ is\ fun.pptm
$ grep -R 'picoCTF' Forensics\ is\ fun
```

Looking through the directory structure more, there's a file called *ppt/slideMasters/hidden* with the contents below:
```
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

Removing whitespace and decoding it with base64 gives the flag.
```
$ cat ppt/slideMasters/hidden | tr -d ' ' | base64 --decode -
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```

### Flag
```
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}
```