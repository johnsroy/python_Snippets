def shift(letter, n):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index + n) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)

def rotate(s, n):
    return ''.join(c if c == ' ' else shift(c, n) for c in s)

print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>>'if your code works correctly you should be able to read this'
