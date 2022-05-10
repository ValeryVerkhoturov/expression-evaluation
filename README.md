# Expression evaluation

## Theory

### Shunting yard algorithm

The shunting yard algorithm is a method for parsing arithmetical or logical expressions, or a combination of both, 
specified in infix notation. It can produce either a postfix notation string, 
also known as Reverse Polish notation (RPN), or an abstract syntax tree (AST). 
The algorithm was invented by Edsger Dijkstra and named the "shunting yard" algorithm 
because its operation resembles that of a railroad shunting yard.

### Reverse Polish notation
Reverse Polish notation (RPN), also known as Polish postfix notation or simply postfix notation, 
is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), 
in which operators precede their operands. 
It does not need any parentheses as long as each operator has a fixed number of operands.

### A simple conversion

1. Input: 3 + 4
2. Push 3 to the output queue (whenever a number is read it is pushed to the output)
3. Push + (or its ID) onto the operator stack
4. Push 4 to the output queue
5. After reading the expression, pop the operators off the stack and add them to the output.
6. In this case there is only one, "+".
7. Output: 3 4 +

### Example

```python
from math_eval.shunting_yard_algorithm import ShuntingYardAlgorithm

sya = ShuntingYardAlgorithm.new_with_default_operations()
rpn = sya.parse("100+1/2") # ['100', '1', '2', '/',  '+']
print(sya.eval_rpn(rpn)) # Output: 100.5
```
