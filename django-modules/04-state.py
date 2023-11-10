#!/usr/bin/python3

import sys

def get_value(dict: dict, value):
    for key, item in dict.items():
        if item == value:
            return key

def print_state(value: str):

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    value = get_value(capital_cities, value)
    if not value:
        print("Unknown capital city")
        return
    else:
        print(get_value(states, value))

def main():
    if len(sys.argv) != 2:
        return
    else:
        print_state(sys.argv[1])

if __name__ == '__main__':
    main()