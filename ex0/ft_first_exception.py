#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:

    '''check_temperature() tries to convert the input to an integer,
       and if it fails to, it is handled by the except ValueError,
       and after converted, checks if it's below 0 or above 40,
       else it returns the temperature in integer'''

    try:
        temp_int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temp_int < 0:
        print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        return None
    elif temp_int > 40:
        print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        return None
    else:
        print(f"Temperature {temp_int}°C is perfect for plants!")
        return temp_int


def test_temperature_input() -> None:

    '''test_temperature_input() tests for each value in inputs table with
       check_temperature , that will verify if the temperature is a valid
       input, and is between 0 and 40 included'''

    print("=== Garden Temperature Checker ===\n")

    inputs = ["25", "abc", "100", "-50"]
    for nb in inputs:
        print(f"Testing temperature: {nb}")
        check_temperature(nb)
        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
