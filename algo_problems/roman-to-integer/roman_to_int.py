def roman_to_int(s: str) -> int:
    num = 0
    passed_index = -1
    for i in range(len(s)):
        if i <= passed_index:
            continue
        group_start = i
        group_end = i
        c = s[i]
        for j in range(i + 1, len(s)):
            cj = s[j]
            if cj == c:
                group_end = j
                passed_index = j
            elif is_negate_case(c, cj):
                group_end = j
                passed_index = j
                break
            else:
                group_end = i
                passed_index = i
                break
        group_char = s[group_start : group_end + 1]
        num += group_to_int(group_char)
    return num


def group_to_int(s: str) -> int:
    roman_int_map = {
        "I": 1,
        "II": 2,
        "III": 3,
        "V": 5,
        "X": 10,
        "XX": 20,
        "XXX": 30,
        "L": 50,
        "C": 100,
        "CC": 200,
        "CCC": 300,
        "D": 500,
        "M": 1000,
        "MM": 2000,
        "MMM": 3000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }
    return roman_int_map[s]


def is_negate_case(c: str, c_next: str):
    if c == "I" and (c_next == "V" or c_next == "X"):
        return True
    if c == "X" and (c_next == "L" or c_next == "C"):
        return True
    if c == "C" and (c_next == "D" or c_next == "M"):
        return True
    return False
