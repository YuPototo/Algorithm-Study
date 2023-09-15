from insert_sort_dec import insert_sort_dec


def test_case_1():
    assert insert_sort_dec([1]) == [1]


def test_case_2():
    assert insert_sort_dec([1, 2]) == [2, 1]


def test_case_3():
    assert insert_sort_dec([3, 2, 1]) == [3, 2, 1]


def test_case_4():
    assert insert_sort_dec([1, 2, 1]) == [2, 1, 1]


def test_case_5():
    assert insert_sort_dec([5, 2, 4, 6, 1, 3]) == [6, 5, 4, 3, 2, 1]
