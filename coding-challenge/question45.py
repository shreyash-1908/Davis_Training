# Question 45: Create a function to calculate simple interest.
# Input: Enter P, R, T
# Output: Simple Interest

def simple_interest(p, r, t):
    return (p * r * t) / 100    

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))            
t = float(input("Enter Time: "))

print(simple_interest(p, r, t))