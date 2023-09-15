# Insert Sort Increasing Order

Implement the insert sort algorithm, output should be a monotonically increasing array.

Reference: Introduction to Algorithms 4th Edition Chapter 2.1

## Time Complexity

### Worst Case

The time complexity of insert sort is O(n^2).

Reasoning:

1. The outer loop runs n times.
2. The inner loop runs i times for each outer loop.
3. The inner loop runs 1 + 2 + ... + n - 1 times in total.
4. 1 + 2 + ... + n - 1 = n * (n - 1) / 2 = O(n^2)
5. The time complexity of insert sort is O(n^2).

### Best Case

Best Case Time Complexity: O(n)

When the array is already sorted, the inner loop will never run.

Reasoning:

1. The outer loop runs n times.
2. The inner loop runs 1 time for each outer loop.
3. The inner loop runs n - 1 times in total.
4. The time complexity of insert sort is O(n).

## Space Complexity

The space complexity of insert sort is O(1).

Reasonging: The space complexity of insert sort is O(1) because it only uses a constant number of variables.
