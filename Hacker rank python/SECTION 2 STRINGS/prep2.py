# Reverse a String
# Input: "hello" → Output: "olleh"
# a = ('Hello')
# print(a[::-1])
# print(reversed(a))

# Check Palindrome String
# Input: "madam" → Output: Palindrome

# b= 'madam'
# if b == b [::-1]:
#     print('The string is palindrome')
# else:
#     print('The string is not palindrome')

# Count Vowels and Consonants Output both counts.
# a = 'hello'
# vowels= 'aeiouAEIOU'

# vowel_count = sum(1 for ch in a if ch in vowels)

# consonant_count = sum(1 for ch in a if ch.isalpha() and ch not in vowels)

# print('Vowels:', vowel_count)

# print('Consonants:', consonant_count)

# Count Words in a Sentence
# Input: "I love Python" → Output: 3

# def count_words(sentence):
#     words = sentence.split()
#     print(len(words))


# sentence = input().strip()
# count_words(sentence)

# Remove Duplicates from String

# def remove_duplicates(s):
#     result= " "
#     for ch in s:
#         if ch not in result:
#             result += ch

#     print(result)
# s = input().strip()
# remove_duplicates(s)

# Find the Frequency of each character

def frequency_character(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1
    print(freq)

s = input().strip()
frequency_character(s)