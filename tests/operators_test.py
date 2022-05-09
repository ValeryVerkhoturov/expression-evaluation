import copy

import pytest

from math_eval import operators
from math_eval.associativity import Associativity
from math_eval.operators import Operator

reference_functions = copy.deepcopy(operators._operators)


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


@pytest.fixture
def operators_for_comparison() -> tuple:
    def create_empty_operator(priority):
        return Operator('', priority, Associativity.LEFT, lambda a, b: 0)

    return create_empty_operator(1), create_empty_operator(1), create_empty_operator(2)


def test_lt(operators_for_comparison):
    assert (operators_for_comparison[0] < operators_for_comparison[1]) is False
    assert operators_for_comparison[1] < operators_for_comparison[2]
    assert (operators_for_comparison[2] < operators_for_comparison[0]) is False


def test_le(operators_for_comparison):
    assert operators_for_comparison[0] <= operators_for_comparison[1]
    assert operators_for_comparison[1] <= operators_for_comparison[2]
    assert (operators_for_comparison[2] <= operators_for_comparison[0]) is False


def test_eq(operators_for_comparison):
    assert operators_for_comparison[0] == operators_for_comparison[1]
    assert (operators_for_comparison[1] == operators_for_comparison[2]) is False
    assert (operators_for_comparison[2] == operators_for_comparison[0]) is False


def test_ne(operators_for_comparison):
    assert (operators_for_comparison[0] != operators_for_comparison[1]) is False
    assert operators_for_comparison[1] != operators_for_comparison[2]
    assert operators_for_comparison[2] != operators_for_comparison[0]


def test_gt(operators_for_comparison):
    assert (operators_for_comparison[0] > operators_for_comparison[1]) is False
    assert (operators_for_comparison[1] > operators_for_comparison[2]) is False
    assert operators_for_comparison[2] > operators_for_comparison[0]


def test_ge(operators_for_comparison):
    assert operators_for_comparison[0] >= operators_for_comparison[1]
    assert (operators_for_comparison[1] >= operators_for_comparison[2]) is False
    assert operators_for_comparison[2] >= operators_for_comparison[0]


@pytest.fixture
def renew_operators():
    operators._operators = copy.deepcopy(reference_functions)


def test_add_operator(renew_operators):
    operator = Operator('%', 3, Associativity.LEFT, lambda a, b: a % b)
    operators.add_operator(operator)

    assert operator in operators._operators


def test_add_function_exception(renew_operators):
    operator = Operator('%', 3, Associativity.LEFT, lambda a, b: a % b)
    operators.add_operator(operator)

    with pytest.raises(Exception):
        operators.add_operator(operator)


def test_get_function_by_token(renew_operators):
    requested_token = '+'
    assert operators.get_operator(requested_token).token == requested_token


def test_get_function_by_non_existent_token(renew_operators):
    requested_token = 'non-existent token'
    assert operators.get_operator(requested_token) is None
