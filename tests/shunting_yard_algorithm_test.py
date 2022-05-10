import pytest

from math_eval.functions import FunctionList
from math_eval.operators import OperatorList

from math_eval.shunting_yard_algorithm import ShuntingYardAlgorithm


# Constants
OPERATOR_LIST = OperatorList.new_with_default_operations()
FUNCTION_LIST = FunctionList.new_with_default_operations()


# Fixtures
@pytest.fixture
def shunting_yard_algorithm() -> ShuntingYardAlgorithm:
    return ShuntingYardAlgorithm.new_with_default_operations()


# Tests
def test_shunting_yard_algorithm_init():
    instance = ShuntingYardAlgorithm(OPERATOR_LIST, FUNCTION_LIST)

    assert instance.operator_list == OPERATOR_LIST
    assert instance.function_list == FUNCTION_LIST


def test_shunting_yard_algorithm_evaluate(shunting_yard_algorithm: ShuntingYardAlgorithm):
    assert shunting_yard_algorithm.parse("10+2") == ['10', '2', '+']
    assert shunting_yard_algorithm.parse("10 * 2") == ['10', '2', '*']
    assert shunting_yard_algorithm.parse("10.1+2.1") == ['10.1', '2.1', '+']
    assert shunting_yard_algorithm.parse("+10") == ['+10']
    assert shunting_yard_algorithm.parse("-10") == ['-10']
    assert shunting_yard_algorithm.parse("-10*2") == ['-10', '2', '*']
    assert shunting_yard_algorithm.parse("1+2+3") == ['1', '2', '+', '3', '+']
    assert shunting_yard_algorithm.parse("1^2^3") == ['1', '2', '3', '^', '^']



