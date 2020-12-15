import re
shinycollection = []


def parsedata():
    rules = {}
    with open('/mnt/d/Code/AdventOfCode2020/2020/day7input.txt', 'r') as file:
        lines = file.read().split("\n")
        groups = [line.split("contain") for line in lines]
        for group in groups:
            group[0] = group[0].strip()
            # print(group[0])
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


def checkshiny(rule, data):
    for child in rule:
        if 'shiny gold' in child and child not in shinycollection:
            return True
        if 'bags' not in child:
            child = child + 's'
            if checkshiny(data[child], data):
                return True
        else:
            if checkshiny(data[child], data):
                return True
    return False


if __name__ == "__main__":
    data = parsedata()
    for rule in data:
        if checkshiny(data[rule], data):
            shinycollection.append(rule)
    print(len(shinycollection))
