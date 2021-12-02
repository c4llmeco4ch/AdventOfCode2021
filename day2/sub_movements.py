# Part 1

file_path = 'instructions.txt'

x, y = 0, 0
with open(file_path) as f:
    for line in f.readlines():
        instr, amount = (s := line.split())[0], int(s[1]) # :=, the walrus operator, will be discussed in another write-up
        if instr == 'forward':
            x += amount
        else:
            y += amount if instr == 'down' else -amount
print(f'Part 1 -> X: {x}, Y: {y}')
print(f'Answer: {x * y}')

# Part 2

x, y, aim = 0, 0, 0
with open(file_path) as f:
    for line in f.readlines():
        instr, amount = (s := line.split())[0], int(s[1]) # see line 8
        if instr == 'forward':
            x += amount
            y += aim * amount
        else:
            aim += amount if instr == 'down' else -amount
print(f'Part 2 -> X: {x}, Y: {y}')
print(f'Answer: {x * y}')