import  random
def calculateMoney(amount, payment):
    amount = random.randint(0, 20) + round(random.randint(0, 100) / 100, 2)
    print(amount)

    if payment >= amount:
        change = payment - amount

        if change > 0:
            d = 0
            d = int(change)
            change -= d

            if change > 0:
                q = 0
                i = 0
                n = 0

                q = q * 0.25  # quarter change calculation
                i = i * 0.10  # dimes change calculation
                n = n * 0.05  # nickel change calculation
                change -= (q + i + n)  # calculate the owed money in changes

                n = n + round(change * 2, 1) * 10  # penny change should be rounded up to nickel
                return f"You got {d} dollars, {q} quarters + {i} dimes, and {n} nickels back in change"
        else:
            return f"You got {d} dollars, {q} quarters + {i} dimes, and {n} nickels back in change"
    else:
        print("No change owed")


print(calculateMoney(amount, 18))
