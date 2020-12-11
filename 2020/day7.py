import re


def parseData():
    rules = {}
    with open('/mnt/d/Code/AdventOfCode2020/2020/day7input.txt', 'r') as file:
        lines = file.read().split("\n")
        groups = [line.split("contain") for line in lines]
        for group in groups:
            group[0] = group[0].strip()
            group[1] = group[1].strip()
            ruleBags = group[1].split(',')
            rules[group[0].strip()] = {}
            for rule in ruleBags:
                rule = rule.strip()
                rule = rule.strip('.')
                if rule == 'no other bags':
                    continue
                else:
                    rule = re.split(r'(\d+) (.+?) bags?[,.]', rule)
                    rules[group[0].strip()][rule[0][1:].strip()] = rule[0][0]
    return rules


def checkBags(rules):
    totalCount = 0
    for rule in rules:
        shinyFrequency = 0
        ruleKeys = rules[rule].keys()
        if 'shiny gold' in rule:
            continue
        for ruleKey in ruleKeys:
            if 'shiny gold' in ruleKey:
                totalCount += 1
            else:
                shinyFrequency += checkParentBag(ruleKey, rules)
        if shinyFrequency >= 1:
            totalCount += 1              
        
    print(totalCount)         

def checkParentBag(ruleKey, rules):
    shinyCount = 0
    if 'bags' not in ruleKey:
        ruleKey = ruleKey + 's'
    keyList = rules[ruleKey].keys()
    for key in keyList:
        if 'shiny gold' in key:
            shinyCount += 1
        else:
            continue

    return shinyCount

if __name__ == "__main__":
    data = parseData()
    checkBags(data)
