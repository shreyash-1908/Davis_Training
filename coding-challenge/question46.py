# Question 46: A shopkeeper wants to calculate total bill after discount.
# Input: Enter price and discount percentage
# Output: Final price after discount


while True:
    price = float(input())

    if price == 0:
        break

    d = float(input())
    print(price - (price * d / 100))