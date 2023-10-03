from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    common = strs[0]
    for i in range(0, len(strs)):
        if i + 1 >= len(strs):
            return common
        common = lcp_2(common, strs[i + 1])


def lcp_2(str_1: str, str_2: str) -> str:
    common = ""
    for i in range(0, len(str_1)):
        if i >= len(str_2):
            return common
        if str_1[i] == str_2[i]:
            common += str_1[i]
        else:
            return common
    return common


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
