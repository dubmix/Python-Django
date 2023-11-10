#!/usr/bin/python3

def read_target():
    with open("numbers.txt") as file:
        for line in file.readlines():
            print_line(line.strip())

def print_line(line: str):
    numbers = line.split(",")
    for number in numbers:
        print(number, end=" ")
    print()

if __name__ == '__main__':
    read_target()