import re

def parseData():
    boardingPasses = []
    with open('/mnt/c/Users/Cas Obdam/Documents/CodeProjects/AdventOfCode/2020/day5input.txt', 'r') as file:
        items = [line.replace("\n", " ") for line in file]
        for item in items:
            row = str(item[:7]).strip()
            rowColumn = str(item[7:]).strip()
            boardingPasses.append([row, rowColumn])
    return boardingPasses


def getPosition(string, start, end):
    # Locate row/column according to letters
    for letter in string:
        if letter == 'B' or letter == 'R':
            start = (end + 1 + start) / 2
        else:
            end -= (end + 1 - start) / 2

    if start == end:
        return int(start)

def calculateSeatId(tickets):
    totalSeatIds = []
    for ticket in tickets:
        row = getPosition(ticket[0], 0, 127)
        column = getPosition(ticket[1], 0, 7)
        seatID = row * 8 + column
        totalSeatIds.append(int(seatID))
    return totalSeatIds

def main():
    tickets = parseData()
    seatIds = calculateSeatId(tickets)
    seatRange = range(min(seatIds), max(seatIds) + 1)
    print(seatRange)

    for seat_id in seatRange:
        if seat_id not in seatIds:
            print(seat_id)

if __name__ == "__main__":
    main()
