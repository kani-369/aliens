"""
Alien Inventory System
Intentional bug for testing the Self-Healing SRE Agent
"""

def calculate_total_energy(items):
    total = 0

    for item in items:
        # BUG: assumes every item has an "energy" key
        total += item["energy"]

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
