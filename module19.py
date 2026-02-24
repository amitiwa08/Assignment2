
# 1. Function to count words
def count_words(text):
    words = text.split()
    return len(words)


# 2. Function to count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for character in text:
        if character in vowels:
            vowel_count += 1
    return vowel_count


# 3. Function to count consonants
def count_consonants(text):
    vowels = "aeiouAEIOU"
    consonant_count = 0
    for character in text:
        if character.isalpha() and character not in vowels:
            consonant_count += 1
    return consonant_count


# 4. Function to reverse text
def reverse_text(text):
    return text[::-1]


# 5. Function to check palindrome
def is_palindrome(text):
    processed_text = text.lower().replace(" ", "")
    return processed_text == processed_text[::-1]


# 6. Function to remove vowels
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for character in text:
        if character not in vowels:
            result += character
    return result


# 7. Function to calculate word frequency
def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


# 8. Function to find longest word
def longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# 9. Main analysis function
def analyze_text(text):

    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    palindrome_result = "Yes" if is_palindrome(text) else "No"
    print("Palindrome:", palindrome_result)

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")

    frequency = word_frequency(text)
    print("Word Frequency:", end=" ")
    for word, count in frequency.items():
        print(f"{word}: {count}", end=", ")
    print()


user_text = input("Enter text: ")
analyze_text(user_text)
