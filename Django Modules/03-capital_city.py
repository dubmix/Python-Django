#!/usr/bin/python3

import sys

def print_city(key: str):

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

    k = states.get(key)
    if not k:
        print("Unknown state")
        return
    else:
        print(capital_cities.get(k))

def main():
    if len(sys.argv) != 2:
        return
    else:
        print_city(sys.argv[1])

if __name__ == '__main__':
    main()