import re
data_file = open('Day3/Day3.txt')
data_in = data_file.readlines()
regex = re.compile('#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)')
claims = {}
max_x = 0
max_y = 0
for data_line in data_in:
    reg_res = regex.match(data_line)
    sq_id, sq_x, sq_y, sq_w, sq_h = map(int, reg_res.group(1, 2, 3, 4, 5))
    claims[sq_id] = (sq_x, sq_y, sq_w, sq_h)
    max_x = max(max_x, sq_x + sq_w)
    max_y = max(max_y, sq_y + sq_h)

grid = [[0] * max_x for i in range(max_y)]
for claim_id in claims:
    sq_x, sq_y, sq_w, sq_h = claims[claim_id]
    for i in range(sq_x, sq_x + sq_w):
        for j in range(sq_y, sq_y + sq_h):
            grid[j][i] += 1

for claim_id in claims:
    no_overlap = True
    sq_x, sq_y, sq_w, sq_h = claims[claim_id]
    for i in range(sq_x, sq_x + sq_w):
        for j in range(sq_y, sq_y + sq_h):
            if grid[j][i] > 1:
                no_overlap = False
                break

    if no_overlap:
        print('Result: %d' % claim_id)
        exit()
