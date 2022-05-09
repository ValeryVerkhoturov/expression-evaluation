import math
import numbers
import typing

from math_eval.associativity import Associativity


class Operator:

    def __init__(self, token: str, priority: numbers.Number, associativity: Associativity,
                 function: typing.Callable[[numbers.Number, numbers.Number], numbers.Number]) -> None:

        self.token: str = token
        self.priority: numbers.Number = priority
        self.associativity: Associativity = associativity
        self.function: typing.Callable[[numbers.Number, numbers.Number], numbers.Number] = function

    def __lt__(self, other):
        if isinstance(other, Operator):
            return self.priority < other.priority

        raise TypeError("Wrong comparison.")

    def __le__(self, other):
        if isinstance(other, Operator):
            return self.priority <= other.priority

        raise TypeError("Wrong comparison.")

    def __eq__(self, other):
        if isinstance(other, Operator):
            return self.priority == other.priority

        raise TypeError("Wrong comparison.")

    def __ne__(self, other):
        if isinstance(other, Operator):
            return self.priority != other.priority

        raise TypeError("Wrong comparison.")

    def __gt__(self, other):
        if isinstance(other, Operator):
            return self.priority > other.priority

        raise TypeError("Wrong comparison.")

    def __ge__(self, other):
        if isinstance(other, Operator):
            return self.priority >= other.priority

        raise TypeError("Wrong comparison.")


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
