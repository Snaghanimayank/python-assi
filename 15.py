input_string = input("Enter a string: ")

if len(input_string) >= 3:
    if input_string.endswith('ing'):
        result_string = input_string + 'ly'
    else:
        result_string = input_string + 'ing'
else:
    result_string = input_string

print(f"The modified string is: {result_string}")
