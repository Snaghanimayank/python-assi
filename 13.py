sentence = input("Enter a sentence: ")

sentence = sentence.lower()

words = sentence.split()

word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("Word frequencies in the sentence:")
for word, frequency in word_frequency.items():
    print(f"'{word}': {frequency}")
