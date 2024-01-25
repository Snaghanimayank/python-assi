string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) >= 2 and len(string2) >= 2:
    
    new_string = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]
    print(f"The result after swapping is: {new_string}")
else:
    print("Please enter two strings with at least two characters each.")
