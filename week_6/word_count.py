"""
Program that counts the occurrences of words in a string

Created by simon richards on 29/8/16
"""

word_count = {}

text = input("Text: ").lower().split()

for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

longest_word_length = max(len(word) for word in word_count)
for word in sorted(word_count):
    print("{:{}} : {}".format(word, longest_word_length, word_count[word]))
