import re
data_file = open('day7/input.txt')
data_in = data_file.readlines()
regex = re.compile('Step (\\w) must be finished before step (\\w) can begin.')
steps = set()
step_before = {}
for line in data_in:
    reg_res = regex.match(line)
    from_step, to_step = reg_res.group(1, 2)
    steps.add(from_step)
    steps.add(to_step)
    if to_step not in step_before:
        step_before[to_step] = []
    step_before[to_step].append(from_step)

steps_remaining = sorted(steps)
steps_performed = []
while len(steps_remaining) > 0:
    for step in steps_remaining:
        if step not in step_before:
            steps_performed.append(step)
            steps_remaining.remove(step)
            new_step_before = {}
            for from_step in step_before:
                if step in step_before[from_step]:
                    step_before[from_step].remove(step)
                if len(step_before[from_step]) > 0:
                    new_step_before[from_step] = step_before[from_step]

            step_before = new_step_before
            break

print(('').join(steps_performed))
