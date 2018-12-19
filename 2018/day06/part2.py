import re
data_file = open('day6/input.txt')
data_in = data_file.readlines()
regex = re.compile('(\\d+), (\\d+)')
min_x = float('inf')
max_x = -float('inf')
min_y = float('inf')
max_y = -float('inf')
coordinates = []
for co in data_in:
    reg_res = regex.match(co)
    x, y = map(int, reg_res.group(1, 2))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    coordinates.append((x, y))

min_x -= 1
max_x += 1
min_y -= 1
max_y += 1
grid = [[0] * (max_x - min_x) for i in range(min_y, max_y)]
new_coordinates = []
for i, co in enumerate(coordinates):
    new_coordinates.append((co[0] - min_x, co[1] - min_y))

inf_coordinates = set()
count_coordinates = [
 0] * len(new_coordinates)
for y in range(len(grid)):
    for x in range(len(grid[y])):
        closest_coordinate = [-1]
        closest_distance = float('inf')
        for i, co in enumerate(new_coordinates):
            manhattan_distance = abs(x - co[0]) + abs(y - co[1])
            if manhattan_distance < closest_distance:
                closest_distance = manhattan_distance
                closest_coordinate = [i]
            else:
                if manhattan_distance == closest_distance:
                    closest_coordinate.append(i)

        if len(closest_coordinate) == 1:
            grid[y][x] = closest_coordinate[0]
            count_coordinates[closest_coordinate[0]] += 1
        else:
            grid[y][x] = -1
        if x == 0 or x == len(grid[y]) - 1:
            inf_coordinates.add(grid[y][x])

    if y == 0 or y == len(grid) - 1:
        inf_coordinates.add(grid[y][x])

max_area = 0
for i, co in enumerate(new_coordinates):
    if i not in inf_coordinates:
        max_area = max(count_coordinates[i], max_area)
        print(i, new_coordinates[i])

print('Result: %d' % max_area)
