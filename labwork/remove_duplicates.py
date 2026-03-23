# create list of 15 numbers
nums = [10, 5, 7, 5, 3, 5, 8, 9, 5, 2, 6, 5, 1, 4, 5]

# take user input
x = int(input("Enter a number to remove duplicates: "))

count = 0
result = []

for num in nums:
    if num == x:
        count += 1
        if count == 1:
            result.append(num)   # keep first occurrence
    else:
        result.append(num)

print("Original List:", nums)
print("Updated List:", result)
