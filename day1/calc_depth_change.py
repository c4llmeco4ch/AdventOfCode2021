# Part 1
with open('measurements.txt') as f:
    lines = f.readlines()
    count = 0
    for pos, num in enumerate(lines[:-1]):
        if int(num) < int(lines[pos + 1]):
            count += 1
    print(count)

# Part 2
with open('measurements.txt') as f:
    lines = f.readlines()
    groups = [sum(int(i) for i in lines[pos : pos + 3]) for pos in range(len(lines) - 2)]
    count = sum(1 for pos, val in enumerate(groups[:-1]) if val < groups[pos + 1])
    print(count)
