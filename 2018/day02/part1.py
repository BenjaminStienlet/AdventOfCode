data_file = open('day2/input.txt')
data_in = data_file.readlines()
two_letters = 0
three_letters = 0
for box_id in data_in:
    dictionary = {}
    contains_two = False
    contains_three = False
    for c in box_id:
        if c in dictionary:
            dictionary[c] = dictionary[c] + 1
        else:
            dictionary[c] = 1

    for c in dictionary:
        if dictionary[c] == 3:
            contains_three = True
        if dictionary[c] == 2:
            contains_two = True

    two_letters += contains_two
    three_letters += contains_three

print('Result: %d' % (two_letters * three_letters))
