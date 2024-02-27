import random

def calculateMoney(amount, payment):
    amount = random.randint(0, 20) + round(random.randint(0, 100) / 100, 2)
    change = payment - amount

    if change > 0:
        d = int(change)
        change -= d

        q = int(change / 0.25)  # Quarter change calculation
        change -= q * 0.25

        i = int(change / 0.10)  # Dimes change calculation
        change -= i * 0.10

        n = int(change / 0.05)  # Nickel change calculation
        change -= n * 0.05

        n = n + round(change * 2, 1) * 10  # penny change should be rounded up to nickel

        return f"You got {d} dollars, {q} quarters, {i} dimes, and {n} nickels back in change"
    else:
        return "There is no change owed"

print(calculateMoney(20, 30))
