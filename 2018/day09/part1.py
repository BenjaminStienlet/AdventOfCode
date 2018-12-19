import re
data_file = open('day9/input.txt')
data_in = data_file.readlines()
regex = re.compile('(\\d+) players; last marble is worth (\\d+) points')
reg_res = regex.match(data_in[0])
nr_players, nr_marbles = map(int, reg_res.group(1, 2))
points = [0] * nr_players
current_player = 0
marbles = [0, 1]
marble_index = 1
for marble in range(2, nr_marbles + 1):
    if marble % 23 == 0:
        marble_index = (marble_index - 7) % len(marbles)
        points[current_player] += marble + marbles[marble_index]
        marbles = marbles[0:marble_index] + marbles[marble_index + 1:]
    else:
        marble_index = (marble_index + 2) % len(marbles)
        if marble_index == 0:
            marble_index = len(marbles)
        marbles = marbles[0:marble_index] + [marble] + marbles[marble_index:]
    current_player = (current_player + 1) % nr_players

print('Result: %d' % max(points))
