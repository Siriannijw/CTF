with open('enc', 'r') as f:
    #The original file
    enc = f.read()
    print(enc)
    
    flag = ''
    for i in range(0, len(enc)):
        o = ord(enc[i])
        one = o >> 8    # Shift off the 8 right-most bits to get the left-most bits
        two = o & 0xFF  # AND with all 1's in the 8 right-most bits to get the right-most bits
        flag += chr(one)
        flag += chr(two)
    print(flag)