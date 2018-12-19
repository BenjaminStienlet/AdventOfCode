# Read data
# data_file = open('day1/input.txt')
# data_in = data_file.readlines()
# frequency = 0

# # Sum frequency
# for i in data_in:
#     frequency += int(i)

# print('Result: %d' % frequency)

# Single line solution - Sum all frequencies
print('Result: %d' % sum(map(int, open('day1/input.txt').readlines())))