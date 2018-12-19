data_file = open('day2.txt')
data_in = data_file.readlines()

two_letters = 0
three_letters = 0

for i in range(len(data_in)):
    for j in range(i):
        nr_diff = 0
        result = ''
        for k in range(len(data_in[i])):
            if data_in[i][k] != data_in[j][k]:
                nr_diff += 1
            else:
                result += data_in[i][k]

        if nr_diff == 1:
            print('Result: %s' % result)
            exit()
