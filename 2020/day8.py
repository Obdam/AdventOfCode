def parse_data():
    data = []
    with open('/mnt/d/Code/AdventOfCode2020/2020/day8input.txt', 'r') as file:
        lines = file.read().split("\n")
        for line in lines:
            data_obj = []
            line = line.split(" ")
            data_obj.append(line[0].strip())
            data_obj.append(line[1][0].strip())
            data_obj.append(int(line[1][1:].strip()))
            data.append(data_obj)
    return data


def single_iteration(instructions):
    index = 0
    known_indexes = set()
    accumulator = 0
    while index not in known_indexes:
        known_indexes.add(index)
        instruction = instructions[index]

        if instruction[0] == 'acc':
            index += 1
            if instruction[1] == '+':
                accumulator += instruction[2]
            else:
                accumulator -= instruction[2]

        elif instruction[0] == 'jmp':
            if instruction[1] == '+':
                index += instruction[2]
            else:
                index -= instruction[2]
        else:
            index += 1

    return accumulator


if __name__ == "__main__":
    # Part 1
    instructions = parse_data()
    # print(single_iteration(instructions))
    for thing in instructions:
        print(instructions[thing])
