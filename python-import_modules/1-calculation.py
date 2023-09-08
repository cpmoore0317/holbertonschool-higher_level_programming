#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

a = 10
b = 5

operations = [
    ("+", add),
    ("-", sub),
    ("*", mul),
    ("/", div)
]

for op_symbol, operation in operations:
    result = operation(a, b)
    print(f"{a} {op_symbol} {b} = {result}")
