import copy
import math

import pytest

from math_eval import functions
from math_eval.functions import Function


reference_functions = copy.deepcopy(functions._functions)


@pytest.fixture
def renew_functions():
    functions._functions = copy.deepcopy(reference_functions)


def test_init():
    name = "exp"
    param_num = 1
    operation = (lambda a: math.exp(a))
    function = Function(name, param_num, operation)

    assert function.name == name
    assert function.param_num == param_num
    assert function.function == operation


def test_add_function(renew_functions):
    function = Function("exp", 1, lambda a: math.exp(a))
    functions.add_function(function)

    assert function in functions._functions


def test_add_function_exception(renew_functions):
    function = Function("exp", 1, lambda a: math.exp(a))
    functions.add_function(function)

    with pytest.raises(Exception):
        functions.add_function(function)
