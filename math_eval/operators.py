import math
import numbers
import typing

from .associativity import Associativity


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


class OperatorList:

    @staticmethod
    def new_operator_list_with_default_operations():
        default_operations = [Operator('+', 2, Associativity.LEFT, lambda a, b: a + b),
                              Operator('-', 2, Associativity.LEFT, lambda a, b: a - b),
                              Operator('*', 3, Associativity.LEFT, lambda a, b: a * b),
                              Operator('/', 3, Associativity.LEFT, lambda a, b: a / b),
                              Operator('^', 4, Associativity.LEFT, lambda a, b: math.pow(a, b))]

        return OperatorList(default_operations)

    def __init__(self, operators):
        self.operators: typing.Final[list[Operator]] = operators

    def add_operator(self, operator: Operator) -> None:
        if all(map(lambda op: operator.token != op.token, self.operators)):
            self.operators.append(operator)
        else:
            raise Exception("Operations with token {} already exists.".format(operator.token))

    def get_operator(self, token: str) -> typing.Optional[Operator]:
        try:
            return next(filter(lambda op: op.token == token, self.operators))
        except StopIteration:
            return None

    def has_operator(self, token: str) -> bool:
        return bool(len(tuple(filter(lambda op: op.token == token, self.operators))) != 0)
