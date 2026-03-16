# alienengine.py
# Simple Alien Engine module with an intentional bug

class AlienEngine:
    def __init__(self):
        self.aliens = [
            {"name": "Zorg", "power": 90},
            {"name": "Blip"},  # BUG: power key missing
            {"name": "Xenon", "power": 70}
        ]

    def calculate_total_power(self):
        total_power = 0

        for alien in self.aliens:
            # BUG HERE
            # This will crash if "power" key does not exist
            total_power += alien["power"]

        return total_power


def run_engine():
    engine = AlienEngine()
    print("Total Alien Power:", engine.calculate_total_power())


if __name__ == "__main__":
    run_engine()
