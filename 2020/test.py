import re

bigbrain = [{'hgt': '173cm', 'byr': '1925', 'pid': '070222017',
             'iyr': '2013', 'hcl': '#ceb3a1', 'ecl': 'gry', 'eyr': '2024'}, {'hcl': '#bc352c', 'pid': '321838059', 'byr': '1930',
                                                                             'hgt': '178cm', 'cid': '213', 'eyr': '2023', 'ecl': 'amb', 'iyr': '2017'}]

validPassKeys = 0

for passport in bigbrain:
    if re.search(r'^#(?:[0-9a-f]{3}){1,2}$', passport['hcl']):
        validPassKeys += 1

print(validPassKeys)
