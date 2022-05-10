import pytest

from math_eval.functions import FunctionList
from math_eval.operators import OperatorList

from math_eval.shunting_yard_algorithm import ShuntingYardAlgorithm


# Constants
OPERATOR_LIST = OperatorList.new_with_default_operations()
FUNCTION_LIST = FunctionList.new_with_default_operations()

EXPRESSION1 = "1/2+1+3/4"
EXPRESSION1_RPN = ['1', '2', '/', '1', '+', '3', '4', '/', '+']
EXPRESSION1_RESULT = float(1/2+1+3/4)

EXPRESSION2 = "1.1 + 2.2 / 3"
EXPRESSION2_RPN = ['1.1', '2.2', '3', '/', '+']
EXPRESSION2_RESULT = float(1.1 + 2.2 / 3)

EXPRESSION3 = "1/2"
EXPRESSION3_RPN = ['1', '2', '/']
EXPRESSION3_RESULT = float(1/2)
EXPRESSION4 = "2/1"
EXPRESSION4_RPN = ['2', '1', '/']
EXPRESSION4_RESULT = float(2/1)


# Fixtures
@pytest.fixture
def shunting_yard_algorithm() -> ShuntingYardAlgorithm:
    return ShuntingYardAlgorithm.new_with_default_operations()


# Tests
def test_shunting_yard_algorithm_init():
    instance = ShuntingYardAlgorithm(OPERATOR_LIST, FUNCTION_LIST)

    assert instance.operator_list == OPERATOR_LIST
    assert instance.function_list == FUNCTION_LIST


def test_shunting_yard_algorithm_parse(shunting_yard_algorithm: ShuntingYardAlgorithm):
    assert shunting_yard_algorithm.parse(EXPRESSION1) == EXPRESSION1_RPN
    assert shunting_yard_algorithm.parse(EXPRESSION2) == EXPRESSION2_RPN
    assert shunting_yard_algorithm.parse(EXPRESSION3) == EXPRESSION3_RPN
    assert shunting_yard_algorithm.parse(EXPRESSION4) == EXPRESSION4_RPN


def test_shunting_yard_algorithm_eval_rpn(shunting_yard_algorithm: ShuntingYardAlgorithm):
    assert shunting_yard_algorithm.eval_rpn(EXPRESSION1_RPN) == EXPRESSION1_RESULT
    assert shunting_yard_algorithm.eval_rpn(EXPRESSION2_RPN) == EXPRESSION2_RESULT
    assert shunting_yard_algorithm.eval_rpn(EXPRESSION3_RPN) == EXPRESSION3_RESULT
    assert shunting_yard_algorithm.eval_rpn(EXPRESSION4_RPN) == EXPRESSION4_RESULT



