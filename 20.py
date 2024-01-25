def insert_string_in_middle(main_string, insert_string):
  
    middle_index = len(main_string) // 2

    result_string = main_string[:middle_index] + insert_string + main_string[middle_index:]

    return result_string

original_string = "abcdefgh"
string_to_insert = "XYZ"
result = insert_string_in_middle(original_string, string_to_insert)
print(f"The result is: '{result}'")
