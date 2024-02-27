import random

"""
Write valid Python code to implement the design shown in the following flow chart. The problem is provided to help make the flow chart clearer, 
but you are not expected to use it in any way. In order to calculate 
the amount that the customer needs to pay, include the code import random as 
the first line of your file and then use amount = random.randint(0,20) + 
round( random.randint(0,100)/100, 2 ) to calculate the amount.

Completely test your code - there will be a major penalty if the code submitted cannot be run by your professor. In order to test your code, set amount to your test value after it is set by the random line. Create comments in your source code to state what values you used to test your program. A single test will not be sufficient to correctly test this program, so do not be concerned if you believe that you need to go through your program more than 1 time in order to completely test it.

Problem: A person is at a store and you have just processed their purchase. After you tell 
them the amount that they owe for their purchase they will hand you some money. 
If the amount given is the exact amount, then you should tell them that no 
change is owed. Otherwise, you should calculate the number of each denomination 
to give them back in their change. The denominations available are dollars 
(1.00), quarters (0.25), dimes (0.10), and nickels (0.05). Since Canada no 
longer has a penny the change should be rounded up to the nearest nickel. 
Once you have calculated the change you should tell the person how much change
 you have given them. In order to keep your customer happy, you should always 
 give them the fewest coins possible, do not simply give them back all their 
 change in nickels.

Note that some of the steps in the flow chart will require you to think about how to get Python to perform the calculation. There is no best way to do it that will earn more marks. Any valid, working Python code that correctly calculates the totals will be accepted. Do not, however, remove any of the conditional statements. There are two conditional blocks in the flow chart and there should be two in your solution since we are trying to practice writing them. You are expected to use meaningful variable names and comment any code you feel requires explanation.

"""

def calculateMoney(amount, payment):
    amount = random.randint(0, 20) + round(random.randint(0, 100) / 100, 2)
    print(amount)

    if payment >= amount:
        return change = payment - amount

    if change > 0:

    else:
        print("No change")



























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
            change = change - (q + i + n)  # calculate the owed money in changes

            n = n + round(change * 2, 1) * 10  # penny change should be rounded up to nickel
            return f"You got {d} dollars, {q} quarters + {i} dimes, and {n} nickels back in change"
        else:
            return f"You got {d} dollars, {q} quarters + {i} dimes, and {n} nickels back in change"
    else:
            return "There is no change owed"


print(calculateMoney(8, 10))