import sys

sys.path.append('paiza/sources/D')
import D145


def test_main():
    assert 4 == D145.main('30 7')
    assert 33 == D145.main('99 3')
