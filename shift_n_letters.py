def shift_1_letter(letter):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index+1) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)



def shift_n_letters(letter, n):
    letter_index = ord(letter) - ord('a') # one of 0, 1, 2, ..., 25
    shifted_index = (letter_index + n) % 26 # still one of 0, 1, 2, ..., 25
    return chr(ord('a') + shifted_index)

print shift_1_letter('a')
#>>> b
print shift_1_letter('n')
#>>> o
print shift_1_letter('z')
#>>> a
print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
