import sys

GREEN = '\033[92m'
RESET_PRINT = '\033[0m'

def analyze_text(text: str):
    '''
    analyze_text(text)
    "text" is the input of the function

    The function prints:
      - the number of characters in the text
      - the number of upper case letters
      - the number of lower case letters
      - the number of punctuation marks
      - the number of spaces
      - the number of digits
    '''
    total_chars = len(text)
    upper_count = sum(1 for char in text if char.isupper())
    lower_count = sum(1 for char in text if char.islower())
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    punctuation_count = sum(1 for char in text if char in punctuation_chars)
    space_count = sum(1 for char in text if char.isspace())
    digit_count = sum(1 for char in text if char.isdigit())

    print(f"The text contains {total_chars} characters:")
    print(f"  {upper_count} upper case letters")
    print(f"  {lower_count} lower case letters")
    print(f"  {punctuation_count} punctuation symbols")
    print(f"  {space_count} spaces")
    print(f"  {digit_count} digits")

def main():
    '''
    main()
      1. Analyzes the given text and prints various information about its content.
      2. Asks for input if no argument is given.
      3. Raises AssertionError if too many arguments provided.
    '''
    try:
        if len(sys.argv) < 2:
            try:
                text = input("Please provide a text to analyze!\n")
                text += "\n"
            except EOFError:
                pass
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        elif len(sys.argv) > 2:
            raise AssertionError("Too many arguments provided")
        analyze_text(text)
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    #docstring = analyze_text.__doc__
    #print(f"{GREEN}{docstring}{RESET_PRINT}")
    #docstring = main.__doc__
    #print(f"{GREEN}{docstring}{RESET_PRINT}")
    main()