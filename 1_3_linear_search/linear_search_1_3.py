def linear_search(arr: list[int], el: int) -> int:
    for i in range(len(arr)):
        if arr[i] == el:
            return i
    return None


# Time complexity
#   Best case: O(1), when el is the first element
#   Average case: O(n)
#   Worst case: O(n), when el is the last element
#   Space complexity: O(1)
