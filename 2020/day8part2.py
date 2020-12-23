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


def find_corrupted_instruction(instructions):
    for command in instructions:
        test_set = instructions
        if command[0] == 'jmp':
            test_set[instructions.index(command)][0] = 'nop'
            end_result = test_new_instruction(test_set)
            if end_result:
                continue
            else:
                continue
        elif command[0] == 'nop':
            test_set[instructions.index(command)][0] = 'jmp'
            end_result = test_new_instruction(test_set)
            if end_result:
                continue
            else:
                continue
        else:
            continue


def test_new_instruction(test_set):
    index = 0
    known_indexes = []
    accumulator = 0
    while index not in known_indexes:
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

    if test_set.index(test_set[-1]) in known_indexes:
        print('The accumulator on the end is', accumulator)
        return True
    else:
        return False


if __name__ == "__main__":
    instructions = parse_data()
    find_corrupted_instruction(instructions)
