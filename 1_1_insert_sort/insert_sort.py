# Constraint
#  - arr length >= 1


def insert_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        el = arr[i]
        j = i - 1
        while j > -1 and arr[j] > el:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = el
    return arr
