# Bubble Sort

## How it works

```pseudocode
BUBBLE-SORT(A)
1 for i = 1 to A.length - 1
2   for j = A.length downto i + 1
3     if A[j] < A[j - 1]
4       exchange A[j] with A[j - 1]
```

## Time complexity

- Worst case: $O(n^2)$
- Best case: $O(n)$
