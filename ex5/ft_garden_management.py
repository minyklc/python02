#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:

    '''Plant class about plant's name, plant's watering and
       level of sunlight it has gotten'''

    def __init__(self, name: str, water: int, sun: int) -> None:
        self.a1 = name
        self.a2 = water
        self.a3 = sun


class GardenManager:

    '''GardenManager manages a garden by adding plants, watering them and
       checking health and raises error if needed'''

    def __init__(self) -> None:
        self.plants = []
        self.tank = 10

    def add_plant(self, plant: Plant) -> None:
        if plant.a1 is None:
            raise PlantError("Error adding plant: Plant name cannot be empty!")
        self.plants.append(plant)
        print(f"Added {plant.a1} successfully")

    def water_plants(self, water: int) -> None:
        try:
            print("Opening watering system")
            for plant in self.plants:
                if self.tank < water:
                    raise WaterError("Caught GardenError: "
                                     "Not enough water in tank")
                plant.a2 += water
                self.tank -= water
                print(f"Watering {plant.a1} - success")
        except GardenError as error:
            print(error)
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        try:
            for plant in self.plants:
                if plant.a2 < 1:
                    raise ValueError(f"Error checking {plant.a1}: "
                                     f"Water level {plant.a2} "
                                     "is too low (min 1)")
                elif plant.a2 > 10:
                    raise ValueError(f"Error checking {plant.a1}: "
                                     f"Water level {plant.a2} "
                                     "is too high (max 10)")
                elif plant.a3 < 2:
                    raise ValueError(f"Error checking {plant.a1}: "
                                     f"Sunlight hours {plant.a3} "
                                     "is too low (min 2)")
                elif plant.a3 > 12:
                    raise ValueError(f"Error checking {plant.a1}: "
                                     f"Sunlight hours {plant.a3} "
                                     "is too high (max 12)")
                else:
                    print(f"{plant.a1}: healthy "
                          f"(water: {plant.a2}, sun: {plant.a3})")
        except ValueError as error:
            print(f"{error}")


def test_garden_management() -> None:

    '''test_garden_management() create a garden, adds plants,
       waters and checks the health of them, and test error recovery'''

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    garden = GardenManager()
    try:
        garden.add_plant(Plant('tomato', 0, 7))
        garden.add_plant(Plant('lettuce', 10, 9))
        garden.add_plant(Plant(None, 5, 9))
    except GardenError as e:
        print(e)
    print()

    print("Watering plants...")
    garden.water_plants(5)
    print()

    print("Checking plant health...")
    garden.check_health()
    print()

    print("Testing error recovery...")
    try:
        if garden.tank < 1:
            raise WaterError("Caught GardenError: Not enough water in tank")
    except WaterError as error:
        print(error)
    finally:
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
