class AlienEngine:
    def __init__(self):
        self.aliens = [
            {"name": "Zorg", "power": 90},
            {"name": "Blip"},   # missing power
            {"name": "Xenon", "power": 70}
        ]

    def calculate_total_power(self):
        total = 0
        for alien in self.aliens:
            total += alien["power"]   # this will crash
        return total


engine = AlienEngine()
print(engine.calculate_total_power())
