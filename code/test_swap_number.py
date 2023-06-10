import swap_number

def test_swapPositions():
    assert swap_number.swapPositions([23, 65, 19, 90], 1, 3) == [19, 65, 23, 90]
    assert swap_number.swapPositions([1, 2, 3, 4, 5], 2, 5) == [1, 5, 3, 4, 2]