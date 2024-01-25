def fibonacci_series(n):
    fib_series = [0, 1]

    while fib_series[-1] + fib_series[-2] <= n:
        next_term = fib_series[-1] + fib_series[-2]
        fib_series.append(next_term)

    return fib_series

range_limit = int(input("Enter the range limit for Fibonacci series: "))

if range_limit < 0:
    print("Please enter a non-negative range limit.")
else:
    fib_result = fibonacci_series(range_limit)
    print(f"Fibonacci series within the range of {range_limit}: {fib_result}")
