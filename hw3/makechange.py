import time


def parse():
    # get file pointers for input and output
    input = open("amount.txt", "r")
    out = open("change.txt", "w")

    # read all lines from input file
    lines = input.readlines()
    denominations = []
    count = 0

    for line in lines:
        # duplicate input denomination and amount into the output file
        out.write(line)
        if '\n' not in line:
            out.write('\n')

        line = line.strip()
        line = line.split()

        if count == 0:
            # parse denominations if this is a first line
            count = 1
            denominations[:] = []
            for num in line:
                denominations.append(int(num))
        else:
            # parse change amount if this is a second line
            count = 0
            amount = int(line[0])

            # this function below will calculate the minimum number of coins and also print out the solution
            make_change(denominations, amount, out)

    input.close()
    out.close()


def make_change(denominations, amount, out):
    solutions = [0]
    coins = [0]

    # init solutions array used for DP calculations
    # init coins array used for back-tracing which coins were used for the solution
    for i in range(1, amount + 1):
        solutions.append(float('inf'))
        coins.append(0)

    # calculate the change from 1 coin up to the amount
    for i in range(1, amount + 1):
        # for every iteration, find the optimal solution for the sub-problem, trying all possible denominations
        for j in denominations:
            index = i - j
            # we can only access elements at non-negative position in the solutions array
            if index >= 0:
                solution = 1 + solutions[index]

                # if the sub-problem solutions is better than the current one, save it as optimal
                if solution < solutions[i]:
                    solutions[i] = solution
                    coins[i] = j

    # print the coins needed for the change
    solution_coins = get_solution_coins(coins, amount)
    print_solution_coins(denominations, solution_coins, out)

    # print the minimum number of coins required to make change to the amount
    min = str(solutions[len(solutions) - 1])
    min += '\n'
    out.write(min)


def get_solution_coins(coins, amount):
    # recursively reconstruct an array of used coins to make change
    solution_coins = []
    if amount > 0:
        solution_coins += get_solution_coins(coins, amount - coins[amount])
        solution_coins.append(coins[amount])
    return solution_coins


def print_solution_coins(denominations, solutions, out):
    results = []

    # print out how many coins of each denomination were used
    for denom in denominations:
        results.append(0)

        for solution in solutions:
            if denom == solution:
                results[len(results) - 1] += 1

    line = ""

    for result in results:
        line += str(result)
        line += " "

    line += '\n'
    out.write(line)


# this function is for experimental ruuning time tests
def run():
    out = open("out.txt", "w")
    denominations = [1]
    i = 2
    while i < 3500:
        denominations.append(i)
        i += 1

    amount = 3500
    start = time.time()
    make_change(denominations, amount, out)
    end = time.time()
    exec_time = end - start
    exec_time *= 1000
    print(exec_time)

# run()
parse()
