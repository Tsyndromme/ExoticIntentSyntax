import random

class Building:
    def __init__(self, value, vulnerability):
        self.value = value
        self.vulnerability = vulnerability

def generate_buildings(num_buildings):
    buildings = []
    for _ in range(num_buildings):
        value = random.randint(50_000, 10_000_000)
        vulnerability = random.uniform(0.1, 1.0)
        buildings.append(Building(value, vulnerability))
    return buildings

def earthquake_damage(earthquake_magnitude, buildings):
    damage = 0
    for building in buildings:
        damage_factor = 1 - (10 ** (1 - earthquake_magnitude / 10))
        building_damage = building.value * building.vulnerability * damage_factor
        damage += building_damage
    return damage

def main():
    num_buildings = int(input("Enter the number of buildings: "))
    earthquake_magnitude = float(input("Enter the earthquake magnitude (Richter scale): "))

    buildings = generate_buildings(num_buildings)
    total_damage = earthquake_damage(earthquake_magnitude, buildings)

    print(f"\nEarthquake Magnitude: {earthquake_magnitude}")
    print(f"Total Damage: ${total_damage:,.2f}")
    print("\nSummary:")
    print(f"An earthquake with a magnitude of {earthquake_magnitude} on the Richter scale")
    print(f"caused an estimated total damage of ${total_damage:,.2f} to {num_buildings} buildings.")

if __name__ == "__main__":
    main()
