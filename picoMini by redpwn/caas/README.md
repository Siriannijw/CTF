# caas
Category: Web Exploitation\
Points: 150

## Description
Now presenting [cowsay as a service](https://caas.mars.picoctf.net/)

## Solution


index.js

```JavaScript
(async () => {
  await new Promise(r => window.addEventListener('load', r));
  document.querySelector('code').textContent =
    `${window.origin}/cowsay/{message}`;
})();
```


### Flag