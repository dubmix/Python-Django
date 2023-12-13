import sys

def check_odd_or_even(nb):
    if nb % 2 == 0:
        return "I'm even."
    else:
        return "I'm odd."

if len(sys.argv) < 2:
    exit()
try:
    try:
        nb = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an int")
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided")
    print(check_odd_or_even(nb))

except AssertionError as error:
    print("AssertionError:", error)