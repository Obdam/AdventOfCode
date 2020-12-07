def parseData():
    answerGroups = []
    with open('/mnt/d/Code/AdventOfCode2020/2020/day6input.txt', 'r') as file:
        lines = file.read().split("\n\n")
        # Assumption: it does not matter how big a group is (a person in a group is separated by an \n)
        answerGroups = [line.replace("\n", "") for line in lines]
        # answerGroups = [group.replace(" ", "") for group in groups]
    return answerGroups    

if __name__ == "__main__":
    print(parseData())