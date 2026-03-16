"""
Alien Navigation System
Intentional bugs for testing the Self-Healing SRE Agent
"""

def calculate_route(distance, speed):
    # BUG 1: Division by zero possible
    time_required = distance / speed
    return time_required

#
def get_alien_rank(alien):
    # BUG 2: Missing dictionary key
    return alien["rank"]


def print_navigation_status(alien):
    # BUG 3: Variable not defined
    print(f"Navigation ready for {alien_name}")


def main():
    alien = {
        "name": "Zorg"
        # BUG 4: missing comma above will cause syntax error
        "power": 900
    }

    route_time = calculate_route(100, 0)  # BUG 5: speed = 0
    rank = get_alien_rank(alien)

    print_navigation_status(alien)

    print("Route time:", route_time)
    print("Rank:", rank)


if __name__ == "__main__":
    main()
