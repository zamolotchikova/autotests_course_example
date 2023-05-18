letter_dict = {}
our_str = 'letter'
new_str = ''

for i in our_str:
    letter_dict[i] = letter_dict.get(i, 0) + 1
    new_str = new_str + (str(i) + '_' + str(letter_dict[i]))

print(new_str)
