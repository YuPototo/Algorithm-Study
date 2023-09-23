from sum_arr import sum_arr


def test_sum_arr():
    assert sum_arr([1, 2, 3, 4, 5]) == 15
    assert sum_arr([1, 2, 3, 4, 5, 6]) == 21
