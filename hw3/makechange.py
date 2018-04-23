import math

def parse():
    input = open("amount.txt", "r")
    out = open("change.txt", "w")
    lines = input.readlines()
    denominations = []
    count = 0
    for line in lines:
        out.write(line)
        line = line.strip()
        line = line.split()
        if count == 0:
            count = 1
            denominations.clear()
            for num in line:
                denominations.append(int(num))
        else:
            count = 0
            amount = int(line[0])
            min = calculate(denominations, amount)
            out.write(str(min))

    input.close()
    out.close()


def calculate(denominations, amount):
    denomSolutions = []
    for x in range(0, amount):
        denomSolutions.append(0)

    C = [0]
    for i in range(1, amount):
        C.append(math.inf)
        for denomination in denominations:
            diff = i - denomination
            if diff >= 0:
                solution = 1 + C[diff]
                if solution < C[i]:
                    C[i] = solution
                    denomSolutions[i] = denomination
    return C[len(C) - 1]


parse()
