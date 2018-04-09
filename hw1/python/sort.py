from merge_sort_func import merge_sort
from insert_sort_func import insert_sort

def parse_and_sort(input, output, sort_type):
    numbers = parse_input_file(input)
    result = sort(numbers, sort_type)
    write_to_file(result, output)
    return None


def parse_input_file(input):
    numbers = []
    f = open(input, "r")
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        line_arr = line.split()
        line_arr.pop(0)

        # Convert strings to numbers
        for i in range(len(line_arr)):
            line_arr[i] = float(line_arr[i])

        numbers.append(line_arr)
    return numbers


def sort(numbers, sort_type):
    result = ""

    for arr in numbers:
        if sort_type == "merge":
            sorted_arr = merge_sort(arr)
        elif sort_type == "insert":
            sorted_arr = insert_sort(arr)

        result += ''.join(str(int(num)) + ' ' for num in sorted_arr)
        result += '\n'

    return result


def write_to_file(str, file_name):
    f = open(file_name, "w")
    f.write(str)
    return None

