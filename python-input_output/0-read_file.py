#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    read_file("my_file_0.txt")