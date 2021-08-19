# Pixelated
Category: Cryptography\
Points: 100

## Description
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled2.png)

## Solution
The description provides two images with seemingly random noise below.
![scrambled1.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/Pixelated/scrambled1.png?raw=true)
![scrambled2.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/Pixelated/scrambled2.png?raw=true)

The two images and random noise makes me think that the pixel values of one is a one-time pad, that was applied to the original image. To test this theory, I used the *pypng* library to get the pixel values for each image to XOR. The script below was the end result.\
*xor.py*
```Python
import png

width1, height1, values1, info1 = png.Reader(filename="scrambled1.png").read()
width2, height2, values2, info2 = png.Reader(filename="scrambled2.png").read()

xor = lambda a, b: a ^ b
row = lambda row1, row2: map(xor, row1, row2)
rows = list(map(row, values1, values2))

img = png.Image(rows, info1)
img.save("unscrambled.png")
```

Running the script resulted in the image below.
![unscrambled.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/Pixelated/unscrambled.png?raw=true)

Looking closely, there's definitly a letter or two that are visible. I filled the white background with black to make the slightly off-white colors visible.
![unscrambled-filled.png](https://github.com/Siriannijw/CTF/blob/main/picoCTF%202021/Pixelated/unscrambled-filled.png?raw=true)

### Flag
```
picoCTF{0542dc1d}
```