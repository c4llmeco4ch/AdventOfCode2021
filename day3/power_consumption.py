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

# Part 2
def determine_split(my_list, pos):
    totals = [0, 0]
    for line in my_list:
        totals[int(line[pos])] += 1
    return totals

most, least = list(lines), list(lines)
for pm in range(line_length):
    m0, m1 = determine_split(most, pm)
    most = list(filter(lambda x: x[pm] == ('1' if m1 >= m0 else '0'), most))
    if len(most) == 1:
        oxy = int(most[0], 2)
        break
print("Least:")
for pl in range(line_length):
    l0, l1 = determine_split(least, pl)
    least = list(filter(lambda x: x[pl] == ('0' if l1 >= l0 else '1'), least))
    if len(least) == 1:
        co2 = int(least[0], 2)
        break
print(f'P2: Oxy = {oxy} | CO2 = {co2}')
print(f'Answer = {oxy * co2}')