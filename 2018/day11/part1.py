import math

data_file = open('day11/input.txt')
grid_serial = int(data_file.readline())
grid_size = 300

grid = [[0] * grid_size for i in range(grid_size)]
for y in range(len(grid)):
    for x in range(len(grid[y])):
        rack_id = (x + 1) + 10
        power_level = rack_id * (y + 1)
        power_level += grid_serial
        power_level *= rack_id
        if power_level > 100:
            power_level = int(str(power_level)[-3])
        else: 
            power_level = 0
        power_level -= 5
        grid[y][x] = power_level

square_size = 3
best_co = (0,0)
best_score = 0
for y in range(len(grid) - square_size):
    for x in range(len(grid[y]) - square_size):
        score = sum(grid[y][x:x+square_size]) + sum(grid[y+1][x:x+square_size]) + sum(grid[y+2][x:x+square_size])
        if score > best_score:
            best_score = score
            best_co = (x+1, y+1)
print("Result: %d,%d" % best_co)
