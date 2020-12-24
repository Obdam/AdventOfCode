import copy


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


def try_corrupted_instruction(instructions):
    for i in range(len(instructions)):
        command = instructions[i]
        test_set = copy.deepcopy(instructions)
        if command[0] == 'jmp':
            test_set[i][0] = 'nop'
            end_result = test_corrupted_instruction(test_set)
        elif command[0] == 'nop':
            test_set[i][0] = 'jmp'
            end_result = test_corrupted_instruction(test_set)


def test_corrupted_instruction(test_set):
    index = 0
    known_indexes = []
    accumulator = 0
    while index not in known_indexes and index < len(test_set):
        known_indexes.append(index)
        instruction = test_set[index]

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
    if index == len(test_set):
        print('The accumulator on the end is', accumulator)
        return True
    else:
        return False


if __name__ == "__main__":
    instructions = parse_data()
    try_corrupted_instruction(instructions)
