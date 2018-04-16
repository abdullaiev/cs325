import random
import time
from merge_sort_func import merge_sort
from insert_sort_func import insert_sort
from stooge_sort_func import stooge_sort


def run_performance_tests(algorithm, use_case):
    for i in range(1, 8):
        test(algorithm, i * 500, use_case)


def test(algorithm, qty, use_case):
    arr = []

    if use_case == "sorted":
        arr = generate_sorted_array(qty)
    elif use_case == "reversed":
        arr = generate_reversed_array(qty)
    else:
        arr = generate_random_numbers(qty)

    start = time.time()
    if algorithm == "merge":
        merge_sort(arr)
    elif algorithm == "insert":
        insert_sort(arr)
    elif algorithm == "stooge":
        stooge_sort(arr, 0, len(arr) - 1)
    end = time.time()
    exec_time = end - start
    # get ms
    exec_time *= 1000

    log = ""
    log += algorithm.upper()
    log += " SORT. ARRAY IS "
    log += use_case.upper()
    log += ". QTY: "
    log += str(qty)
    log += ". TIME: "
    log += str(round(exec_time, 2))
    print(log)


def generate_random_numbers(qty):
    arr = []
    for i in range(qty):
        arr.append(random_number(10000))
    return arr


def generate_sorted_array(length):
    arr = []
    for i in range(length):
        arr.append(i)
    return arr


def generate_reversed_array(length):
    arr = []
    for i in range(length, 0, -1):
        arr.append(i)
    return arr


def random_number(max_num):
    return random.randint(1, max_num + 1)


print("=========MERGE SORT TESTS=========")
# run_performance_tests('merge', 'sorted')
run_performance_tests('merge', 'random')
#
print("=========INSERT SORT TESTS=========")
# run_performance_tests('insert', 'sorted')
run_performance_tests('insert', 'random')
# run_performance_tests('insert', 'reversed')


print("=========STOOGE SORT TESTS=========")
# run_performance_tests('stooge', 'sorted')
run_performance_tests('stooge', 'random')
# run_performance_tests('stooge', 'reversed')
