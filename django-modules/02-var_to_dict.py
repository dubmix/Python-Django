#!/usr/bin/python3

def print_dict(var: dict):
    for k, i in var.items():
        print(i, ":", k)

def var_to_dict():
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1988'),
        ('Cobain', '1966'),
        ('White', '1975')
        ]

    dict = {}
    for key, value in d:
            dict[key] = dict.get(key, value)
    return dict

if __name__ == '__main__':
    print_dict(var_to_dict())