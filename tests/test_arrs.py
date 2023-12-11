from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([2, 1, 4], 2, "test") == 4
    assert arrs.get([5, 10, -1], 4, "test") == 'test'
    assert arrs.get([1, 2, 3, 4, 5], 10, default="Not found") == "Not found"
    assert arrs.get([1, 2, 3, 4, 5], 3) is not None
    assert arrs.get([], 0, default="Empty") == "Empty"
    assert arrs.get([1, 2, 3, 4, 5], 3) == int("4")


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
