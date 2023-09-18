from merge_sort import merge_sort


def test_case_1():
    assert merge_sort([1]) == [1]


def test_case_2():
    assert merge_sort([2, 1]) == [1, 2]


def test_case_3():
    assert merge_sort([3, 2, 1]) == [1, 2, 3]


def test_case_4():
    assert merge_sort([1, 2, 1]) == [1, 1, 2]


def test_case_5():
    assert merge_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
