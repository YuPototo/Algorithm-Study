from longest_common import longest_common_prefix


def test_1():
    strs = ["flower", "flow", "flight"]
    assert longest_common_prefix(strs) == "fl"


def test_2():
    assert longest_common_prefix([""]) == ""


def test_3():
    assert longest_common_prefix(["a"]) == "a"


def test_4():
    assert longest_common_prefix(["ab", "a"]) == "a"


def test_5():
    assert longest_common_prefix(["cir", "car"]) == "c"
