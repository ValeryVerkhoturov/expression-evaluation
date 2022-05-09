from math_eval.associativity import Associativity


def test_enum():
    assert Associativity.LEFT.value is not None
    assert Associativity.RIGHT.value is not None
