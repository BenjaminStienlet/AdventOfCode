import re
data_file = open('day4/input.txt')
data_in = data_file.readlines()
data_in.sort()
regex_falls_asleep = re.compile('\\[\\d+-(\\d+-\\d+) \\d+:(\\d+)\\] falls asleep')
regex_wakes_up = re.compile('\\[\\d+-(\\d+-\\d+) \\d+:(\\d+)\\] wakes up')
regex_shift_start = re.compile('\\[\\d+-(\\d+-\\d+).*\\] Guard #(\\d+) begins shift')
shifts = {}
current_shift = None
falls_asleep = None
for data_line in data_in:
    reg_res = regex_shift_start.match(data_line)
    if reg_res is not None:
        if current_shift is not None:
            shifts[current_shift[0]] = (
             current_shift[1], current_shift[2])
        current_shift = [
         reg_res.group(1), int(reg_res.group(2)), [False] * 60]
        falls_asleep = None
    reg_res = regex_falls_asleep.match(data_line)
    if reg_res is not None:
        current_shift[0] = reg_res.group(1)
        falls_asleep = int(reg_res.group(2))
    reg_res = regex_wakes_up.match(data_line)
    if reg_res is not None:
        for i in range(falls_asleep, int(reg_res.group(2))):
            current_shift[2][i] = True

guards = {}
for timestamp in shifts:
    guard_id, timeslots = shifts[timestamp]
    if guard_id not in guards:
        guards[guard_id] = timeslots
    else:
        guards[guard_id] = list(map(sum, zip(guards[guard_id], timeslots)))

guard_most_asleep = None
time_most_asleep = 0
for guard_id in guards:
    time_asleep = sum(guards[guard_id])
    if time_asleep > time_most_asleep:
        time_most_asleep = time_asleep
        guard_most_asleep = int(guard_id)

chosen_minute = guards[guard_most_asleep].index(max(guards[guard_most_asleep]))
print('Result: %d' % (guard_most_asleep * chosen_minute))
