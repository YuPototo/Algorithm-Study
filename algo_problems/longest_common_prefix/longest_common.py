from typing import List
import math


## Divide and Conquer
# def longest_common_prefix(strs: List[str]) -> str:
#     return longest_common_prefix_helper(strs, 0, len(strs) - 1)


# def longest_common_prefix_helper(strs: List[str], l: int, r: int) -> str:
#     # base case: if l == r, return strs[l]
#     if l == r:
#         return strs[l]
#     else:
#         # divide the array into two halves
#         mid = (l + r) // 2
#         # recursively call the function on the two halves
#         # lcp_left is the longest common prefix of the left half
#         lcp_left = longest_common_prefix_helper(strs, l, mid)

#         # lcp_right is the longest common prefix of the right half
#         lcp_right = longest_common_prefix_helper(strs, mid + 1, r)

#         # return the longest common prefix of lcp_left and lcp_right
#         return common_prefix(lcp_left, lcp_right)


# def common_prefix(left: str, right: str):
#     min_length = min(len(left), len(right))
#     for i in range(min_length):
#         if left[i] != right[i]:
#             return left[:i]
#     return left[:min_length]

# -----

## Vertical Scanning: it's like my first approach
# def longest_common_prefix(strs: List[str]) -> str:
#     if not strs:
#         return ""
#     for i in range(len(strs[0])):
#         c = strs[0][i]
#         for j in range(1, len(strs)):
#             if i == len(strs[j]) or strs[j][i] != c:
#                 return strs[0][:i]
#     return strs[0]


## Horizontal scanning: from leetcode
# def longest_common_prefix(strs: List[str]) -> str:
#     if not strs:
#         return ""
#     prefix = strs[0]
#     for i in range(1, len(strs)):
#         while strs[i].find(prefix) != 0:
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix


# -----

## My approach when reading leet code prompt
# def longest_common_prefix(strs: List[str]) -> str:
#     common = strs[0]
#     for i in range(0, len(strs)):
#         if i + 1 >= len(strs):
#             return common
#         common = lcp_2(common, strs[i + 1])


# def lcp_2(str_1: str, str_2: str) -> str:
#     common = ""
#     for i in range(0, len(str_1)):
#         if i >= len(str_2):
#             return common
#         if str_1[i] == str_2[i]:
#             common += str_1[i]
#         else:
#             return common
#     return common


# -----


# # Following approach is my intuitive approach
# def longest_common_prefix(strs: List[str]) -> str:
#     i = 0  # charecter index
#     common = ""
#     first_str = strs[0]
#     if len(first_str) == 0:
#         return ""
#     while True:
#         if i >= len(first_str):
#             return common
#         new_char = first_str[i]
#         if new_char == "":
#             return common
#         for j in range(1, len(strs)):
#             word = strs[j]
#             if i >= len(word):
#                 return common
#             if new_char != word[i]:
#                 return common
#         common += new_char
#         i += 1
