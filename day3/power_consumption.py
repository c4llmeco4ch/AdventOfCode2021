file_path = 'input.txt'
with open(file_path) as f:
    lines = f.readlines()
line_length = len(lines[0].strip())
one_count = [0] * line_length
for line in lines:
    one_count = [a + int(b) for a, b in zip(one_count, line.strip())]

# Part 1
gamma = [1 if val >= len(lines) // 2 else 0 for val in one_count]
epsilon = int(''.join([str(int(not num)) for num in gamma]), 2)
gamma = int(''.join([str(i) for i in gamma]), 2)
print(f'P1: Gamma = {gamma} | Epsilon = {epsilon}')
print(f'Answer = {gamma * epsilon}')
