from linear_search_1_3 import linear_search


def test_linear_search():
    assert linear_search([1], 1) == 0
    assert linear_search([1, 2, 3], 1) == 0
    assert linear_search([1, 2, 3], 2) == 1
    assert linear_search([1, 2, 3], 4) == None
