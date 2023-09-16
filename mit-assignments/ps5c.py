'''Problem #3
Implement the is_valid_word function.
def is_valid_word(word, hand, word_list):
"""
Returns True if word is in the word_list and is entirely
composed of letters in the hand. Otherwise, returns False.
Does not mutate hand or word_list.
word: string
hand: dictionary (string -> int)
word_list: list of strings'''

import words
def is_valid_word(word, hand ,word_list):
    if word not in word_list:
        return False
    
    for letter in word:
        if hand[letter] == 0:
            return False
        else:
            hand[letter] -= 1

    return True      

hand = {'a': 2, 'b': 1, 'c': 1, 'd': 1}
word = "bad"
is_valid_word(word, hand, words)