# Read data
data_file = open('day1/input.txt')
data_in = data_file.readlines()
frequency = 0
seen = {0}

# Loop until a frequency is found that is reached twice
while True:
    for i in data_in:
        frequency += int(i)
        if frequency in seen:
            print('Result: %d' % frequency)
            exit()
        # Keep track of the frequencies that have been seen
        seen.add(frequency)
