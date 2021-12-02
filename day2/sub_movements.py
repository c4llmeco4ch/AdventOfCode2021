# Part 1

x, y = 0, 0
with open('instructions.txt') as f:
    for line in f.readlines():
        instr, amount = (s := line.split())[0], int(s[1])
        if instr == 'forward':
            x += amount
        else:
            y += amount if instr == 'down' else -amount
print(f'Part 1 -> X: {x}, Y: {y}')
print(f'Answer: {x * y}')

# Part 2

x, y, aim = 0, 0, 0
with open('instructions.txt') as f:
    for line in f.readlines():
        instr, amount = (s := line.split())[0], int(s[1])
        if instr == 'forward':
            x += amount
            y += aim * amount
        else:
            aim += amount if instr == 'down' else -amount
print(f'Part 2 -> X: {x}, Y: {y}')
print(f'Answer: {x * y}')