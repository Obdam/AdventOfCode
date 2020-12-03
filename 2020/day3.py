map = []
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
totalTrees = 1

with open('/mnt/c/Users/Cas Obdam/Documents/CodeProjects/AdventOfCode/2020/day3input.txt', 'r') as file:
    for line in file:
        map.append(str(line).strip())

# Task 1
row = 0
column = 0
trees = 0
while row < len(map):
    if map[row][column % len(map[0])] == '#':
        trees += 1

    column += 3
    row += 1
print(trees)

# Task 2
for slope in slopes:
    column = slope[0]
    row = slope[1]
    trees = 0
    while row < len(map):
        if map[row][column % len(map[0])] == '#':
            trees += 1

        column += slope[0]
        row += slope[1]

    totalTrees *= trees

print(totalTrees)