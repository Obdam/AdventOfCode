map = []
row = 0
right = 3
trees = 0

with open("/mnt/d/Code/AdventOfCode2020/2020/day3input.txt", 'r') as file:
    for line in file:
        map.append(str(line).strip())

while row + 1 < len(map):
    