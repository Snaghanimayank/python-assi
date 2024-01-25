
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result_with_temp = swap_with_temp(num1, num2)
print(f"Swapping with temp variable: {result_with_temp}")

result_without_temp = swap_without_temp(num1, num2)
print(f"Swapping without temp variable: {result_without_temp}")
