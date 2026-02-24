user_sentence = input("Enter a sentence: ")

# Displaying the original sentence
print("\nOriginal:", user_sentence)

# 1. Total characters (including spaces)
total_characters_with_spaces = len(user_sentence)
print("Characters (with spaces):", total_characters_with_spaces)

# 2. Total characters (excluding spaces)
# We remove spaces using replace() before counting
total_characters_without_spaces = len(user_sentence.replace(" ", ""))
print("Characters (without spaces):", total_characters_without_spaces)

# 3. Total words
# split() separates the sentence into words based on spaces
word_list = user_sentence.split()
total_words = len(word_list)
print("Words:", total_words)

# 4. Convert to UPPERCASE
uppercase_sentence = user_sentence.upper()
print("UPPERCASE:", uppercase_sentence)

# 5. Convert to lowercase
lowercase_sentence = user_sentence.lower()
print("lowercase:", lowercase_sentence)

# 6. Convert to Title Case
title_case_sentence = user_sentence.title()
print("Title Case:", title_case_sentence)

# 7. First word
# Accessing the first element from the word list
print("First word:", word_list[0])

# 8. Last word
# Accessing the last element using negative indexing
print("Last word:", word_list[-1])

# 9. Reversed sentence (character-wise reverse)
reversed_sentence = user_sentence[::-1]
print("Reversed:", reversed_sentence)
