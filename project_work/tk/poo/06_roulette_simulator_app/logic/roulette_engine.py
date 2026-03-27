class RouletteGame:
    def __init__(self):
        self.wheel_numbers = list(range(0, 37))  # European roulette
        self.bets = []

    def spin_wheel(self):
        import random
        return random.choice(self.wheel_numbers)

    def place_bet(self, number, amount):
        self.bets.append({'number': number, 'amount': amount})
