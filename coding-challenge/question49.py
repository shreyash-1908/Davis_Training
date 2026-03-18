# Question 49: Print all even numbers between 1 to N.
# Input: Enter N
# Output: Even numbers list

n = int(input("Enter N: "))

if n>= 2:
    for i in range(2, n + 1, 2):
        print(i, end=" ")
else:
    print("No even numbers between 1 and", n)