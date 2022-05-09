import pytest

from math_eval.associativity import Associativity
from math_eval.operators import Operator, OperatorList


# Constants
OPERATOR_TOKEN = '%'
OPERATOR_PRIORITY = 3
OPERATOR_ASSOCIATIVITY = Associativity.LEFT
OPERATOR_OPERATION = (lambda a, b: a % b)


# Fixures
@pytest.fixture
def operator():
    return Operator(OPERATOR_TOKEN, OPERATOR_PRIORITY, OPERATOR_ASSOCIATIVITY, OPERATOR_OPERATION)


@pytest.fixture
def operator_list():
    return OperatorList.new_operator_list_with_default_operations()


@pytest.fixture
def operators_for_comparison() -> tuple:
    def create_empty_operator(priority):
        return Operator('', priority, Associativity.LEFT, lambda a, b: 0)

    return create_empty_operator(1), create_empty_operator(1), create_empty_operator(2)


# Tests
def test_operator_init(operator):
    assert operator.token == OPERATOR_TOKEN
    assert operator.priority == OPERATOR_PRIORITY
    assert operator.associativity == OPERATOR_ASSOCIATIVITY
    assert operator.function == OPERATOR_OPERATION


def test_operator_lt(operators_for_comparison):
    assert (operators_for_comparison[0] < operators_for_comparison[1]) is False
    assert operators_for_comparison[1] < operators_for_comparison[2]
    assert (operators_for_comparison[2] < operators_for_comparison[0]) is False


def test_operator_le(operators_for_comparison):
    assert operators_for_comparison[0] <= operators_for_comparison[1]
    assert operators_for_comparison[1] <= operators_for_comparison[2]
    assert (operators_for_comparison[2] <= operators_for_comparison[0]) is False


def test_operator_eq(operators_for_comparison):
    assert operators_for_comparison[0] == operators_for_comparison[1]
    assert (operators_for_comparison[1] == operators_for_comparison[2]) is False
    assert (operators_for_comparison[2] == operators_for_comparison[0]) is False


def test_operator_ne(operators_for_comparison):
    assert (operators_for_comparison[0] != operators_for_comparison[1]) is False
    assert operators_for_comparison[1] != operators_for_comparison[2]
    assert operators_for_comparison[2] != operators_for_comparison[0]


def test_operator_gt(operators_for_comparison):
    assert (operators_for_comparison[0] > operators_for_comparison[1]) is False
    assert (operators_for_comparison[1] > operators_for_comparison[2]) is False
    assert operators_for_comparison[2] > operators_for_comparison[0]


def test_operator_ge(operators_for_comparison):
    assert operators_for_comparison[0] >= operators_for_comparison[1]
    assert (operators_for_comparison[1] >= operators_for_comparison[2]) is False
    assert operators_for_comparison[2] >= operators_for_comparison[0]


def test_operator_list_init(operator_list: OperatorList):
    assert OperatorList(operator_list.operators).operators == operator_list.operators


def test_operator_list_add_operator(operator: Operator, operator_list: OperatorList):
    operator_list.add_operator(operator)

    assert operator in operator_list.operators


def test_operator_list_add_operator_exception(operator: Operator, operator_list: OperatorList):
    operator_list.add_operator(operator)

    with pytest.raises(Exception):
        operator_list.add_operator(operator)


def test_operator_list_get_operator(operator: Operator, operator_list: OperatorList):
    operator_list.add_operator(operator)
    assert operator_list.get_operator(operator.token) == operator


def test_operator_list_get_non_existent_operator(operator: Operator, operator_list: OperatorList):
    assert operator_list.get_operator(operator.token) is None


def test_operator_list_has_operator(operator: Operator, operator_list: OperatorList):
    operator_list.add_operator(operator)

    assert operator_list.has_operator(operator.token)


def test_operator_list_has_not_operator(operator: Operator, operator_list: OperatorList):
    assert not operator_list.has_operator(operator.token)
