import re

def parseData():
    rules = {}
    with open('/mnt/d/Code/AdventOfCode2020/2020/day7test.txt', 'r') as file:
        lines = file.read().split("\n")
        groups = [line.split("contain") for line in lines]
        for group in groups:
            ruleBags = group[1].split(',')
            rules[group[0].strip()] = {}
            for rule in ruleBags:
                rule = rule.strip()
                rule = rule.strip('.')
                rule = re.split(r'(\d+) (.+?) bags?[,.]', rule)
                rules[group[0].strip()][rule[0][1:].strip()] = rule[0][0]

    return rules

def checkShinyBags(rules):
    bagcolorCount = 0
    for bag in bagRules:
        print(bag)
        for key in bagRules[bag].keys():
            if 'shiny gold' in key:
                bagcolorCount += 1
                continue
            else:
                if 'o other bags' in key:
                    continue
                elif 'bags' not in key:
                    key = key + 's'
                    for key in bagRules[key].keys():
                        if 'shiny gold' in key:
                            bagcolorCount += 1
                else:
                    for key in bagRules[key].keys():
                        if 'shiny gold' in key:
                            bagcolorCount += 1
                        
    print(bagcolorCount)

if __name__ == "__main__":
    bagRules = parseData()
    checkShinyBags(bagRules)