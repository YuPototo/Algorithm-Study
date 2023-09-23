from bubble_sort import bubble_sort


def test_case_1():
    assert bubble_sort([1]) == [1]


def test_case_2():
    assert bubble_sort([2, 1]) == [1, 2]


def test_case_3():
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]


def test_case_4():
    assert bubble_sort([1, 2, 1]) == [1, 1, 2]


def test_case_5():
    assert bubble_sort([5, 2, 4, 6, 1, 3]) == [1, 2, 3, 4, 5, 6]
