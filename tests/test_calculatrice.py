import calculatrice as calc


def test_convert():
    assert calc.convert('I') == 1
    assert calc.convert('V') == 5
    assert calc.convert('X') == 10
    assert calc.convert('L') == 50
    assert calc.convert('C') == 100
    assert calc.convert('D') == 500
    assert calc.convert('M') == 1000
