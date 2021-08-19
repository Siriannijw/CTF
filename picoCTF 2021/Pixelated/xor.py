import png

width1, height1, values1, info1 = png.Reader(filename="scrambled1.png").read()
width2, height2, values2, info2 = png.Reader(filename="scrambled2.png").read()

xor = lambda a, b: a ^ b
row = lambda row1, row2: map(xor, row1, row2)
rows = list(map(row, values1, values2))

img = png.Image(rows, info1)
img.save("unscrambled.png")