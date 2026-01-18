#!/usr/bin/env python3

def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    check_plant_health('tomato', 3, 8)
    print()

    print("Testing empty plant name...")
    check_plant_health(None, 4, 6)
    print()

    print("Testing bad water level...")
    check_plant_health('banana', 15, 10)
    print()

    print("Testing bad sunlight hours...")
    check_plant_health('cherry', 2, 0)
    print()

    print("All error raising tests completed!")


def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    try:
        if plant_name is None:
            raise ValueError("Error: Plant name cannot be empty!")
        elif water_level < 1:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too low (min 1)")
        elif water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             f"is too high (max 10)")
        elif sunlight_hours < 2:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        elif sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             f"is too high (max 12)")
        else:
            print(f"Plant '{plant_name}' is healthy!")
    except ValueError as error:
        print(f"{error}")


if __name__ == "__main__":
    test_plant_checks()
