def insert_sort(arr):
    """

    :type arr: list
    """
    if len(arr) < 2:
        return arr

    for i in range(len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
