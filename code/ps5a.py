'''The function get_word_score should accept a string of lowercase letters as input (a word) and
return the integer score for that word, using the game's scoring rules.
Fill in the code for get_word_score in ps5.py:
def get_word_score(word, n):
"""
Returns the score for a word. Assumes the word is a
valid word.
The score for a word is the sum of the points for letters
in the word, plus 50 points if all n letters are used on
the first go.
Letters are scored as in Scrabble; A is worth 1, B is
worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
word: string (lowercase letters)
n: integer (maximum hand size; i.e., hand size required for additional
points)
returns: int >= 0
"""
# TO DO ...
You may assume that the input word is always either a string of lowercase letters, or the empty
string "". You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of
ps5.py. You should not change its value.
Do not assume that there are always 7 letters in a hand! The parameter n is the number of
letters required for a bonus score (the maximum number of letters in the hand).'''


def get_word_score(word, n):

    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 
    'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]

    #score = sum(SCRABBLE_LETTER_VALUES[letter] for letter in word) 

    if len(word) == n:
        score += 50  

    return score


word = "hello"
n = 7 
print(get_word_score(word, n))