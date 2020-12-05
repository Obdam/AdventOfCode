import re
validKeys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
validExcKeys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def parseData():
    data = []
    with open('/mnt/c/Users/Cas Obdam/Documents/CodeProjects/AdventOfCode/2020/day4input.txt', 'r') as file:
        lines = file.read().split("\n\n")
        items = [line.replace("\n", " ") for line in lines]
        for item in items:
            passpDict = {}
            objectList = re.split(' ', item)
            for obj in objectList:
                newItem = re.split(r'(-+|:)', obj)
                passpDict.update({newItem[0]: newItem[2]})
            data.append(passpDict)
    return data


def checkValidPassports(data):
    valid = 0
    for passport in data:
        if passport.keys() >= validKeys:
            valid += checkPassportfields(passport)
        elif passport.keys() >= validExcKeys:
            valid += checkPassportfields(passport)
    return valid

def checkPassportfields(passport):
    validPassKeys = 0
    if 'byr' in passport:
        if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
            validPassKeys += 1
    if 'iyr' in passport:
        if int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
            validPassKeys += 1
    if 'eyr' in passport:
        if int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
            validPassKeys += 1
    if 'hgt' in passport:
        height = passport.get('hgt')
        if 'cm' in height:
            numberHeight = int(height.replace('cm', ''))
            if numberHeight >= 150 and numberHeight <= 193:
                validPassKeys += 1
        elif 'in' in height:
            numberHeight = int(height.replace('in', ''))
            if numberHeight >= 59 and numberHeight <= 76:
                validPassKeys += 1
    if 'hcl' in passport:
        if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', passport['hcl']):
            validPassKeys += 1
    if 'ecl' in passport:
        if passport['ecl'] in eyeColors:
            validPassKeys += 1
    if 'pid' in passport:
        if len(str(passport['pid'])) == 9:
            validPassKeys += 1
    if 'cid' in passport:
        validPassKeys += 1

    if validPassKeys == len(validKeys) or validPassKeys == len(validExcKeys):
        return 1
    else:
        return 0


def main():
    data = parseData()
    print(checkValidPassports(data))


if __name__ == "__main__":
    main()
