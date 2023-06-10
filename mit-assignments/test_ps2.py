import ps2

def test_combinations():
    assert ps2.combinations(50) == [(2, 2, 1), (5, 0, 1)]
    assert ps2.combinations(51) == [(1, 5, 0), (4, 3, 0), (7, 1, 0)]
    assert ps2.combinations(52) == [(2, 0, 2)]
    assert ps2.combinations(53) == [(1, 3, 1), (4, 1, 1)]
    assert ps2.combinations(54) == [(0, 6, 0), (3, 4, 0), (6, 2, 0), (9, 0, 0)]
    assert ps2.combinations(55) == [(1, 1, 2)]

    


