#!/usr/bin/env python3

def test_error_types(error: ValueError | ZeroDivisionError
                     | FileNotFoundError | KeyError,
                     arg: str | None) -> None:

    '''test_error_types() displays the error messages
       in correlation with the type of error detected'''

    if arg == "multiple":
        print("Caught an error, but program continues!\n")
    elif error == ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    elif error == ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    elif error == FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{arg}'\n")
    elif error == KeyError:
        print(f"Caught KeyError: '{arg}'\n")


def garden_operations() -> None:

    '''garden_operations() tries every type of errors and sends the
       error got to test_error_types() to display error messages'''

    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("a")
    except ValueError:
        test_error_types(ValueError, arg=None)

    print("Testing ZeroDivisionError...")
    try:
        b = 0
        b = 40 / b
    except ZeroDivisionError:
        test_error_types(ZeroDivisionError, arg=None)

    print("Testing FileNotFoundError...")
    try:
        file = "missing.txt"
        f = open(file, "r")
        f.close()
    except FileNotFoundError:
        test_error_types(FileNotFoundError, file)

    print("Testing KeyError...")
    try:
        missing = r'missing\_plant'
        flower = {'anemone': 1, 'bluebell': 2, 'cactus': 3}
        flower[missing]
    except KeyError:
        test_error_types(FileNotFoundError, missing)

    print("Testing multiple errors together...")
    try:
        b = int("0")
        b = 40 / b
    except (ValueError, ZeroDivisionError):
        if b == 0:
            test_error_types(ZeroDivisionError, "multiple")
        else:
            test_error_types(ValueError, "multiple")

    print("All error types tested successfully!")


if __name__ == "__main__":
    garden_operations()
