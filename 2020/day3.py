map = []
row = 0
column = 0
trees = 0

with open('/mnt/d/Code/AdventOfCode2020/2020/day3input.txt', 'r') as file:
    for line in file:
        map.append(str(line).strip())

while row < len(map):
    if map[row][column % len(map[0])] == '#':
        trees += 1

    column += 3
    row += 1
    
print(trees)