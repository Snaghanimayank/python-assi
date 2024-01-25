
n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_integers = n * (n + 1) // 2

    print(f"The sum of the first {n} positive integers is: {sum_of_integers}")
