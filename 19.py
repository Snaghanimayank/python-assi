def get_first_and_last_two_chars(input_str):
   
    if len(input_str) >= 2:
        result_str = input_str[:2] + input_str[-2:]
        return result_str
    else:
        return ""

input_string = input("Enter a string: ")
result = get_first_and_last_two_chars(input_string)
print(f"The result is: '{result}'")
