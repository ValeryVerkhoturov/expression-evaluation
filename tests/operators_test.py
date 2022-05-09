import copy

import pytest

from math_eval import operators
from math_eval.associativity import Associativity
from math_eval.operators import Operator

reference_functions = copy.deepcopy(operators._operators)


@pytest.fixture
def renew_operators():
    operators._operators = copy.deepcopy(reference_functions)


def test_init():
    token = '%'
    priority = 3
    associativity = Associativity.LEFT
    operation = (lambda a, b: a % b)
    operator = Operator(token, priority, associativity, operation)

    assert operator.token == token
    assert operator.priority == priority
    assert operator.associativity == associativity
    assert operator.function == operation


def test_add_operator(renew_operators):
    operator = Operator('%', 3, Associativity.LEFT, lambda a, b: a % b)
    operators.add_operator(operator)

    assert operator in operators._operators


def test_add_function_exception(renew_operators):
    operator = Operator('%', 3, Associativity.LEFT, lambda a, b: a % b)
    operators.add_operator(operator)

    with pytest.raises(Exception):
        operators.add_operator(operator)
