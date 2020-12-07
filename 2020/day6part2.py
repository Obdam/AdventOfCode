def parseData():
    answerGroups = []
    with open('/mnt/d/Code/AdventOfCode2020/2020/day6input.txt', 'r') as file:
        lines = file.read().split("\n\n")
        groups = [line.replace("\n", " ") for line in lines]
        for group in groups:
            newGroup = group.split(' ')
            answerGroups.append(newGroup)
    return answerGroups


def collectUniqueAnswers(group):
    uniqueAnswerLetters = []
    for word in group:
        for letter in word:
            if letter not in uniqueAnswerLetters:
                uniqueAnswerLetters.append(letter)

    return uniqueAnswerLetters

def calculateFullAnsweredQuestion(answerGroups):
    fullAnsweredQuestionCount = 0
    for group in answerGroups:
        uniqLetters = collectUniqueAnswers(group)
        # Check per unique letter in group if it's answered by everyone.
        for uniqLetter in uniqLetters:
            totalAnswered = 0
            for person in group:
                for letter in person:
                    if letter == uniqLetter:
                        totalAnswered += 1
            
            if totalAnswered == int(len(group)):
                fullAnsweredQuestionCount += 1
    
    return fullAnsweredQuestionCount
                

if __name__ == "__main__":
    print(calculateFullAnsweredQuestion(parseData()))