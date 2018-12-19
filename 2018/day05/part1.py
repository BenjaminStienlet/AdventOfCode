data_file = open('day5/input.txt')
data_in = data_file.readlines()
polymers = data_in[0]
change_made = True
while change_made:
    new_polymers = ''
    change_made = False
    i = 0
    while i < len(polymers):
        if i < len(polymers) - 1:
            if polymers[i].lower() == polymers[i + 1].lower():
                if polymers[i].isupper() != polymers[i + 1].isupper():
                    change_made = True
                    i += 2
        else:
            new_polymers += polymers[i]
            i += 1

    polymers = new_polymers

print('Result: %d' % len(polymers))
