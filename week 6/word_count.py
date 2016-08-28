"""
Program that counts the occurrences of words in a string

Created by simon richards on 29/8/16
"""

word_count = {}
LONGEST_WORD = 0

text = input("Text: ").lower().split()

for word in text:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
    if len(word) > LONGEST_WORD:
        LONGEST_WORD = len(word)

for word in sorted(word_count):
    print("{:{}} : {}".format(word, LONGEST_WORD, word_count[word]))
