import calculatrice as calc


def test_convert():
    assert calc.convert_1_input('I') == 1
    assert calc.convert_1_input('V') == 5
    assert calc.convert_1_input('X') == 10
    assert calc.convert_1_input('L') == 50
    assert calc.convert_1_input('C') == 100
    assert calc.convert_1_input('D') == 500
    assert calc.convert_1_input('M') == 1000

def test_convert_add2():
    assert calc.convert_same_add2('II') == 2
    assert calc.convert_same_add2('VV') == 10
    assert calc.convert_same_add2('XX') == 20
    assert calc.convert_same_add2('LL') == 100
    assert calc.convert_same_add2('CC') == 200
    assert calc.convert_same_add2('DD') == 1000
    assert calc.convert_same_add2('MM') == 2000

def test_convert_same_caract_n():
    assert calc.convert_same_caract_n("III") == 3
    assert calc.convert_same_caract_n("IIIII") == 5
    assert calc.convert_same_caract_n('VVV') == 15
    assert calc.convert_same_caract_n('VVVVV') == 25
    assert calc.convert_same_caract_n('XXX') == 30
    assert calc.convert_same_caract_n('XXXXX') == 50
    assert calc.convert_same_caract_n('LLL') == 150
    assert calc.convert_same_caract_n('CCC') == 300
    assert calc.convert_same_caract_n('DDD') == 1500
    assert calc.convert_same_caract_n('MMM') == 3000

def test_convert_add():
    assert calc.convert_add("IV") == 6
    assert calc.convert_add("MIV") == 1006
    assert calc.convert_add("MCMXLIV") == 2166


def test_soustration_2_caract():
    assert calc.soustraction_2_caract('IV') == 4
    assert calc.soustraction_2_caract('IX') == 9
