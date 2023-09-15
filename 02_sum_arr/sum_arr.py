def sum_arr(arr: list[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_arr(arr[1:])
