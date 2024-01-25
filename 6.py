
letter = input("Enter a letter: ")

letter = letter.lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is not a vowel.")
