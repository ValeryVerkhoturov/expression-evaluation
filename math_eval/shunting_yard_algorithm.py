import typing
import re

from math_eval.functions import FunctionList
from math_eval.operators import OperatorList
from math_eval.consts import SPACING, OPEN_BRACKET, CLOSING_BRACKET
from math_eval.associativity import Associativity


class ShuntingYardAlgorithm:

    @staticmethod
    def new_with_default_operations():
        return ShuntingYardAlgorithm(OperatorList.new_with_default_operations(),
                                     FunctionList.new_with_default_operations())

    def __init__(self, operator_list: OperatorList, function_list: FunctionList):
        self.operator_list = operator_list
        self.function_list = function_list

    # def tokenize(self, infix_expression: str) -> [str]:
    #     return re.findall(r"(\b\w*[\.]?\w+\b|[\(\){}])"
    #                       .format(''.join(map(lambda op: "\\" + op.token, self.operator_list.operators))), infix_expression)

    # Parse infix math expression to reverse polish notation with operator_list, function_list
    def parse(self, infix_expression: str):
        stack = []
        sign: typing.Optional[str] = None
        prev_token: typing.Optional[str] = None
        output_rpn = []

        for token in infix_expression:
            if token == SPACING:  # Pass empty tokens
                continue

            if sign:
                token = sign + token
                sign = None

            if token == OPEN_BRACKET:
                stack.append(token)
            elif self.function_list.has_function(token):
                stack.append(token)
            elif token == CLOSING_BRACKET:
                operator = None
                while len(stack) > 0:
                    operator = stack.pop()
                    if operator != OPEN_BRACKET and not self.function_list.has_function(operator):
                        output_rpn.append(operator)
                # if operator is None:
                #     return None  # redundant closing brackets
            elif self.operator_list.has_operator(token):
                if prev_token is None or prev_token == OPEN_BRACKET:
                    sign = token
                    continue
                while len(stack):
                    # pop collected stack
                    current_operator = self.operator_list.get_operator(token)
                    operator = self.operator_list.get_operator(stack[-1])
                    if operator is None or current_operator is None:
                        break
                    if current_operator.associativity == Associativity.LEFT and \
                            current_operator <= operator or \
                            current_operator < operator:
                        output_rpn.append(stack.pop())
                    else:
                        break
                stack.append(token)
            else:
                if prev_token is None or \
                        prev_token == OPEN_BRACKET or \
                        self.operator_list.has_operator(prev_token):
                    output_rpn.append(token)  # new output token
                else:
                    output_rpn[-1] += token  # add character to prev output token for numbers and function names
            prev_token = token
        while len(stack) > 0:
            token = stack.pop()
            if token == OPEN_BRACKET:
                return None  # redundant opening brackets
            output_rpn.append(token)

        return output_rpn

    def eval_rpn(self, rpn) -> float:
        stack = []

        for token in rpn:
            if self.operator_list.has_operator(token):
                op = self.operator_list.get_operator(token) or self.function_list.get_function(token)
                stack.append(op.function(*reversed([stack.pop() for i in range(op.param_num)])))
            elif self.function_list.has_function(token):
                op = self.function_list.get_function(token)
                stack.append()
            else:
                stack.append(float(token))
        return stack[0]


if __name__ == "__main__":
    sya = ShuntingYardAlgorithm.new_with_default_operations()
    print(sya.eval_rpn(sya.parse(input())))

