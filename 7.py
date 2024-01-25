
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    result_sum = 0
    print("Two or more numbers are equal. Sum is set to zero.")
else:
    result_sum = num1 + num2 + num3
    print(f"The sum of the three integers is: {result_sum}")
