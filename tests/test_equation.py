from equation import eq


def test_equation():
    assert eq(1, 1) == -1


def test_equation2():
    assert eq(2, 1) == -0.5
