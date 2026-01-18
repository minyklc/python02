#!/usr/bin/env python3

def test_watering_system() -> None:

    '''test_watering_system() sends in parameter to water_plants()
       a good garden and an invalid garden'''

    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    good_garden = ['tomato', 'lettuce', 'carrot']
    water_plants(good_garden)
    print("Watering completed successfully!\n")

    print("Testing with error...")
    bad_garden = ['tomato', None]
    water_plants(bad_garden)
    print("\nCleanup always happens, even with errors!")


def water_plants(plant_list: tuple | list) -> None:

    '''water_plants() checks for each plants in the garden
       if the name is a valid name, invalid name is an empty name (None),
       and the watering system is then closed.'''

    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Error: Cannot water {plant} "
                                 f"- invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(f"{error}")
    finally:
        print("Closing watering system (cleanup)")


if __name__ == "__main__":
    test_watering_system()
