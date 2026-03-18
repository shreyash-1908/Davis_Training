# Question 48: Calculate electricity bill based on units consumed.
# Input: Enter units
# Output: Total bill amount

def bill_calc(units):
    if units <= 100:
        return units * 5 + 50
    elif units <= 200:
        return units * 7 + 50
    else:
        return units * 10 + 50

units = int(input("Enter units consumed: "))
print("Total bill amount:", bill_calc(units))