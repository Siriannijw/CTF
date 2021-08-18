# where are the robots
Category: Web Exploitation\
Points: 100

## Description
Can you find the robots? *https://jupiter.challenges.picoctf.org/problem/36474/* ([link](https://jupiter.challenges.picoctf.org/problem/36474/)) or http://jupiter.challenges.picoctf.org:36474

## Solution
The title *where are the robots* is a significant clue that the answer is in the *robots.txt* whose purpose is to specify permissions for website indexers.
```
$ wget -q http://jupiter.challenges.picoctf.org:36474/robots.txt
$ cat robots.txt 
User-agent: *
Disallow: /477ce.html
```

The file reveals a relative page hosted by the site.
```
$ wget -q http://jupiter.challenges.picoctf.org:36474/477ce.html
$ cat 477ce.html 
<!doctype html>
<html>
  <head>
    <title>Where are the robots</title>
    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="container">
      
      <div class="content">
        <p>Guess you found the robots<br />
          <flag>picoCTF{ca1cu1at1ng_Mach1n3s_477ce}</flag></p>
      </div>
      <footer></footer>
  </body>
</html>
```

### Flag
```
picoCTF{ca1cu1at1ng_Mach1n3s_477ce}
```