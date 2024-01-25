def find_longest_word(word_list):
   
    if not word_list:
        return 0  

    longest_word = max(word_list, key=len)

    return len(longest_word)

words = ["apple", "banana", "kiwi", "strawberry", "orange"]
result = find_longest_word(words)
print(f"The length of the longest word is: {result}")
