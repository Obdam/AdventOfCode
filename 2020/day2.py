import re

def importPasswords():
    passwords = []
    with open("day2Input.txt", "r") as file:
        for line in file:
            passwords.append(line)
    return passwords

def checkPasswordPolicy(passwords):
    validPasswords = 0
    for password in passwords:
        splittedPassword = re.split(r'(-+|:+| )', password)
        minNum = int(splittedPassword[0])
        maxNum = int(splittedPassword[2])
        policyLetter = str(splittedPassword[4]).strip()
        distortedPass = str(splittedPassword[8]).strip()

        count = 0
        for letter in distortedPass:
            if letter == policyLetter:
                count += 1

        if count >= minNum and count <= maxNum:
            validPasswords += 1

    return validPasswords

def checkRealPasswordPolicy(passwords):
    validPasswords = 0
    for password in passwords:
        splittedPassword = re.split(r'(-+|:+| )', password)
        minNum = int(splittedPassword[0])
        maxNum = int(splittedPassword[2])
        policyLetter = str(splittedPassword[4]).strip()
        distortedPass = str(splittedPassword[8]).strip()

        if distortedPass[maxNum - 1] == policyLetter:
            validPasswords += 1
        elif distortedPass[minNum - 1] == policyLetter:
            validPasswords += 1
        
        if (policyLetter == distortedPass[maxNum - 1] and policyLetter != distortedPass[minNum - 1]) or (policyLetter != distortedPass[maxNum - 1] and policyLetter == distortedPass[minNum - 1]):
            validPasswords += 1

    return validPasswords

def main():
    passwordDump = importPasswords()
    totalCorrect = checkRealPasswordPolicy(passwordDump)
    print("The total correct passwords are: ", totalCorrect)

if __name__ == "__main__":
    main()
