"""
Alien Inventory Systems
Intentional bug for testing the Self-Healing SRE Agentuhi
"""

def calculate_total_energy(items):
    total = 0

    for item in items:
        # Use .get() with a default of 0 to handle items missing the 'energy' key
        total += item.get("energy", 0)

    return total


def main():
    inventory = [
        {"name": "Plasma Core", "energy": 50},
        {"name": "Dark Matter Cell"},   # Missing "energy" key
        {"name": "Quantum Battery", "energy": 120}
    ]

    total_energy = calculate_total_energy(inventory)

    print("Total energy:", total_energy)


if __name__ == "__main__":
    main()
