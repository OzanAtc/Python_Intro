import random

def calculateMoney(amount, payment):
    change = payment - amount

    if change > 0:
        d = 0
        d = int(change)
        change -= d

        if change > 0:
            q = 0
            i = 0
            n = 0
            q = int(change // 0.25)
            change -= q * 0.25

            i = int(change // 0.10)
            change -= i * 0.10

            n = round(change / 0.05)
            return f"You got {d} dollars, {q} quarters, {i} dimes, and {n} nickels back in change"

        else:
            return f"You got {d} dollars and no coins back in change"
    else:
        return "There is no change owed"

# Test the function
print(calculateMoney(4.35, 10)) # Tested with $4.35 amount and payment of $10
print(calculateMoney(6, 9.75))  # Tested with $6 amount and payment of $9.75
print(calculateMoney(10, 10))   # Tested with $10 amount and payment of $10
print(calculateMoney(12, 8))    # Tested with $12 amount and payment of $8