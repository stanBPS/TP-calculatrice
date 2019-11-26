import calculatrice as calc


def test_convert():
    assert calc.convert('I') == 1
    assert calc.convert('V') == 5
    assert calc.convert('X') == 10
    assert calc.convert('L') == 50
    assert calc.convert('C') == 100
    assert calc.convert('D') == 500
    assert calc.convert('M') == 1000

def test_convert_add2():
    assert calc.convert_add2('II') == 2
    assert calc.convert_add2('VV') == 10
    assert calc.convert_add2('XX') == 20
    assert calc.convert_add2('LL') == 100
    assert calc.convert_add2('CC') == 200
    assert calc.convert_add2('DD') == 1000
    assert calc.convert_add2('MM') == 2000