def stooge_sort(arr, start, end):
    n = end - start + 1
    if n == 2 and arr[start] > arr[end]:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
    elif n > 2:
        third = n // 3
        stooge_sort(arr, start, end - third)
        stooge_sort(arr, start + third, end)
        stooge_sort(arr, start, end - third)
