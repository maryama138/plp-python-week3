count = 1
total = 0

# BUG: The loop condition was count < 5, which stopped before adding 5. I changed it to count <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: The print statement was outside the correct indentation and total needed to be converted to a string.
print("Sum of 1 to 5 is: " + str(total))

# BUG: The original loop did not include 5, so the answer was 10 instead of 15.
