
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

if num1 == num2 or num1 + num2 == 5 or abs(num1 - num2) == 5:
    result = True
else:
    result = False

print(result)
