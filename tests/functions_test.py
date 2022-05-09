import math

import pytest

from math_eval.functions import Function, FunctionList


# Constants
FUNCTION_NAME = "customFunction"
FUNCTION_PARAM_NUM = 1
FUNCTION_FUNCTION = lambda a: math.exp(a)


# Fixtures
@pytest.fixture
def function():
    return Function(FUNCTION_NAME, FUNCTION_PARAM_NUM, FUNCTION_FUNCTION)


@pytest.fixture
def function_list():
    return FunctionList.new_function_list_with_default_operations()


# Tests
def test_init(function):
    assert function.name == FUNCTION_NAME
    assert function.param_num == FUNCTION_PARAM_NUM
    assert function.function == FUNCTION_FUNCTION


def test_new_function_list_with_default_operations():
    assert len(FunctionList.new_function_list_with_default_operations().functions) != 0


def test_function_list_init(function_list):
    assert FunctionList(function_list.functions).functions == function_list.functions


def test_function_list_add_function(function: Function, function_list: FunctionList):
    before_addition = len(function_list.functions)
    function_list.add_function(function)
    after_addition = len(function_list.functions)

    assert before_addition + 1 == after_addition


def test_function_list_add_function_exception(function: Function, function_list: FunctionList):
    function_list.add_function(function)

    with pytest.raises(Exception):
        function_list.add_function(function)


def test_function_list_has_function(function: Function, function_list: FunctionList):
    function_list.add_function(function)

    assert function_list.has_function(function.name)


def test_function_list_has_not_function(function: Function, function_list: FunctionList):
    assert not function_list.has_function(function)

