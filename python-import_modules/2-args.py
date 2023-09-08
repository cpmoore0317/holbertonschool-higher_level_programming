#!/usr/bin/python3

import sys

args = sys.argv[1:]

num_args = len(args)

if num_args == 0:
    print("0 argument" + ("" if num_args == 1 else "s") + ".")
else:
    print(f"{num_args} argument" + ("" if num_args == 1 else "s") + ":")
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
