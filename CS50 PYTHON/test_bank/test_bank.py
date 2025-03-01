from bank import value


def test_greeting():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi there world") == 20
    assert value("HI THERE WORLD") == 20
    assert value("whatssup world") == 100
    assert value("WHATSSUP WORLD") == 100
