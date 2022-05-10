import math
import numbers
import typing


class Function:

    def __init__(self, name: str, param_num: numbers.Number, function: typing.Callable) -> None:
        self.name = name
        self.param_num = param_num
        self.function = function


class FunctionList:

    @staticmethod
    def new_with_default_operations():
        default_operations = [Function("log", 2, lambda a, b: math.log(a, b)),
                              Function("sqrt", 1, lambda a: math.sqrt(a))]

        return FunctionList(default_operations)

    def __init__(self, functions: list[Function]):
        self.functions: typing.Final[list[Function]] = functions

    def add_function(self, function: Function) -> None:
        if all(map(lambda func: func.name != function.name, self.functions)):
            self.functions.append(function)
        else:
            raise Exception("Function with name {} already exists.".format(function.name))

    def has_function(self, func_name: str) -> bool:
        return bool(len(tuple(filter(lambda func: func.name == func_name, self.functions))) != 0)