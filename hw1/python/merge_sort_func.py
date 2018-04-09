import math

def merge_sort(arr):
    """

    :type arr: list
    """
    length = len(arr)

    if length < 2:
        return arr

    middle = int(math.floor(length / 2))
    left = arr[0:middle]
    right = arr[middle:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)


def merge(left, right):
    results = []

    while len(left) and len(right):
        if left[0] < right[0]:
            results.append(left.pop(0))
        else:
            results.append(right.pop(0))

    while len(left):
        results.append(left.pop(0))

    while len(right):
        results.append(right.pop(0))

    return results