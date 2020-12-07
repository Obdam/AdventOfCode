# Parse answer data as list objects, so you get a list with answers per group.
def parseData():
    answerGroups = []
    with open('/mnt/d/Code/AdventOfCode2020/2020/day6input.txt', 'r') as file:
        lines = file.read().split("\n\n")
        # Assumption: it does not matter how big a group is (a person in a group is separated by an \n)
        groups = [line.replace("\n", "") for line in lines]
        answerGroups = [group.replace(" ", "") for group in groups]
    return answerGroups    

def countUniqueAnswers(answers):
    totalUniqueAnswers = 0
    for answer in answers:
        uniqueAnswerLetters = []
        for letter in answer:
            if letter not in uniqueAnswerLetters:
                uniqueAnswerLetters.append(letter)
        totalUniqueAnswers += len(uniqueAnswerLetters)

    return totalUniqueAnswers


if __name__ == "__main__":
    print(countUniqueAnswers(parseData()))


