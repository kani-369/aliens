class AlienEngine:
    def __init__(self):
        self.aliens = [
            {"name": "Zorg", "power": 90},
            {"name": "Blip"},  # missing "power"
            {"name": "Xenon", "power": 70}
        ]
#hi
    #jacsiweubciwbviwbvi
##hdgfgfgfuhef
    def calculate_total_power(self):
        total_power = 0
        for alien in self.aliens:
            total_power += alien["power"]  # ← crash here
        return total_power
