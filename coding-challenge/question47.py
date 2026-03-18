# Question 47: Check whether a person is eligible to vote.
# Input: Enter age
# Output: Eligible / Not Eligible


n = int(input())
count = 0

for i in range(n):
    age = int(input())
    if age < 18:
        count += 1

print(count)