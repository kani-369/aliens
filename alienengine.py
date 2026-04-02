"""
Alien Inventory Systems
Intentional bug for testing the Self-Healing SRE Agent
"""

def calculate_total_energy(items):
    total = 0

    for item in items:
        try:
            # Attempt to get energy, if not present, KeyError will be caught
            total += item["energy"]
        except KeyError:
            # If 'energy' key is missing, default its contribution to 0.
            # This explicitly handles the KeyError reported in the logs.
            total += 0
            # Optional: print(f"Warning: Item '{item.get('name', 'Unknown')}' is missing 'energy' key. Assuming 0 energy.")

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
