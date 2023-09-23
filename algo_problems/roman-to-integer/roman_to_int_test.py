from roman_to_int import roman_to_int


def test_1():
    assert roman_to_int("III") == 3


def test_2():
    assert roman_to_int("IV") == 4


def test_3():
    assert roman_to_int("LVIII") == 58


def test_4():
    assert roman_to_int("MCMXCIV") == 1994


def test_5():
    assert roman_to_int("IX") == 9


def test_6():
    assert roman_to_int("DCXXI") == 621


def test_7():
    assert roman_to_int("MMMCXXX") == 3130
