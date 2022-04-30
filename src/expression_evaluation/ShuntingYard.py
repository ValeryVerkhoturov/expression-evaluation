import math
from enum import Enum


class ShuntingYard:

    def __init__(self):
        pass

    def evaluate(self, input: str):
        pass


class Associativity(Enum):
    LEFT = "left"
    RIGHT = "right"


# [name, priority, associativity, param_num, operation]
class Operator(Enum):
    PLUS = ['+', 2, Associativity.LEFT, 2, lambda a, b: a + b]
    MINUS = ['-', 2, Associativity.LEFT, 2, lambda a, b: a - b]
    MULTIPLY = ['*', 3, Associativity.LEFT, 2, lambda a, b: a * b]
    DIVIDE = ['/', 3, 'left', 2, lambda a, b: a / b]
    POWER = ['^', 4, 'right', 2, lambda a, b: math.pow(a, b)]