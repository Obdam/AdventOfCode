# Parse answer data as list objects, so you get a list with answers per group.
def parseData():
    answerGroups = []
    with open('day6input.txt', 'r') as file:
        # answerGroups = file.read().split("\n\n")
        for line in file:
            print(line)

    return answerGroups    


if __name__ == "__main__":
    parseData()
