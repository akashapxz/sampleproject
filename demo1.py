num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# New feature added
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")