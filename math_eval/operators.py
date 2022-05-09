import math
import numbers
import typing

from math_eval.associativity import Associativity


class Operator:

    def __init__(self, token: str, priority: numbers.Number, associativity: Associativity,
                 function: typing.Callable[[numbers.Number, numbers.Number], numbers.Number]) -> None:
        self.token = token
        self.priority = priority
        self.associativity = associativity
        self.function = function


_operators = [Operator('+', 2, Associativity.LEFT, lambda a, b: a + b),
              Operator('-', 2, Associativity.LEFT, lambda a, b: a - b),
              Operator('*', 3, Associativity.LEFT, lambda a, b: a * b),
              Operator('/', 3, Associativity.LEFT, lambda a, b: a / b),
              Operator('^', 4, Associativity.LEFT, lambda a, b: math.pow(a, b))]


def add_operator(operator: Operator) -> None:
    if all(map(lambda op: operator.token != op.token, _operators)):
        _operators.append(operator)
    else:
        raise Exception("Operations with token {} already exists.".format(operator.token))
