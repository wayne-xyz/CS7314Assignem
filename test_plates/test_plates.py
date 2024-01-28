from plates import is_valid

def test_length():
    assert is_valid('a') == False
    assert is_valid('andrd123') == False
    assert is_valid('ban123') == True

def test_startLetter():
    assert is_valid('AB') == True
    assert is_valid('a153') == False
    assert is_valid('z3') == False

def test_numbersLast():
    assert is_valid('BMB2on') == False
    assert is_valid('g00fab') == False
    assert is_valid('mm001') == False
    assert is_valid('ll100') == True

def test_invalidChar():
    assert is_valid('gt0.1') == False
    assert is_valid('gt!') == False
    assert is_valid('gttt e') == False
