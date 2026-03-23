"""
Alien Inventory Systems
Intentional bug for testing the Self-Healing SRE Agentuhi
"""

def calculate_total_energy(items):
    total = 0

    for item in items:
        # BUG: assumes every item has an "energy" key
        # FIX: Safely get 'energy' with a default of 0 if missing
        total += item.get("energy", 0)

    return total


def main():
    inventory = [
        {"name": "Plasma Core", "energy": 50},
        {"name": "Dark Matter Cell"},   # BUG: missing "energy"
        {"name": "Quantum Battery", "energy": 120}
    ]

    total_energy = calculate_total_energy(inventory)

    print("Total energy:", total_energy)


if __name__ == "__main__":
    main()
