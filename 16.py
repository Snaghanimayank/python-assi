input_string = input("Enter a string: ")

index_not = input_string.find('not')
index_poor = input_string.find('poor')

if index_not != -1 and index_poor != -1 and index_not < index_poor:
    result_string = input_string[:index_not] + 'good' + input_string[index_poor + 4:]
else:
    result_string = input_string

print(f"The resulting string is: {result_string}")
