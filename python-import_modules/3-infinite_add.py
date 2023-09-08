#!/usr/bin/python3

from sys import argv as arg
__name__ == "__main__":
total = 0
for i in range(len(arg) - 1):
    total += int(arg[i + 1])
print("{}".format(total))
