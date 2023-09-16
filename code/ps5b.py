'''Problem #2
Implement the update_hand function. Make sure this function has no side effects; i.e., it cannot
mutate the hand passed in.
def update_hand(hand, word):
"""
Assumes that 'hand' has all the letters in word.
In other words, assumes that however many times
a letter appears in 'word', 'hand' has at least as
many instances of that letter in it.
Updates the hand: uses up the letters in the given word
and returns the new hand, without those letters in it.
Has no side effects: does not modify hand.
word: string
hand: dictionary (string -> int)
returns: dictionary (string -> int)'''

def update_hand(hand, word):
    
    for letter in word:
        
        if letter in hand:
            hand[letter] -= 1

            if hand[letter] == 0:
                del hand[letter] 
    
    print(hand)


hand = {'a': 2, 'b': 1, 'c': 1, 'd': 1}
word = "bad"
print(update_hand(hand, word))                