import math
import numbers
import typing


class Function:

    def __init__(self, name: str, param_num: numbers.Number, function: typing.Callable) -> None:
        self.name = name
        self.param_num = param_num
        self.function = function


_functions = [Function("log", 2, lambda a, b: math.log(a, b)), Function("sqrt", 1, lambda a: math.sqrt(a))]


def add_function(function: Function) -> None:
    if all(map(lambda func: func.name != function.name, _functions)):
        _functions.append(function)
    else:
        raise Exception("Function with name {} already exists.".format(function.name))
