#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_operations() -> None:

    '''garden_operations() tests custom errors about
       the state of the plant and the amount of wtaer in the tank.
       for PlantError, the state of the plants is determined
       by the age of them in day, and the amount of tank's water in L'''

    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    garden = {'strawberry': 25, 'tomato': 300}
    for plant in garden:
        try:
            if garden[plant] > 150:
                raise PlantError("Caught PlantError: "
                                 f"The {plant} plant is wilting!")
        except GardenError as error:
            print(f"{error}\n")

    print("Testing WaterError...")
    storage = {'tank': 2, 'tank2': 11}
    for stored in storage:
        try:
            if storage[stored] < 5:
                raise WaterError("Caught WaterError: "
                                 f"Not enough water in the {stored}!")
        except GardenError as error:
            print(f"{error}\n")

    print("Testing catching all garden errors...")
    garden = {'tank': 2, 'tomato': 300}
    for stored in garden:
        try:
            if stored == 'tank' and garden[stored] < 5:
                raise PlantError("Caught a garden error: "
                                 f"The {plant} plant is wilting!")
            if stored == 'tomato' and garden[stored] > 150:
                raise WaterError("Caught WaterError: "
                                 f"Not enough water in the {stored}!")
        except GardenError as error:
            print(f"{error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_operations()
