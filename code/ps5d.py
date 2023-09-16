'''4
Implement the play_hand function. This function allows the user to play out a single hand.
def play_hand(hand, word_list):
"""
Allows the user to play the given hand, as follows:
* The hand is displayed.
* The user may input a word. Alternatively, the user may end the
game by entering a period (.).
* An invalid word is rejected, and a message is displayed asking
the user to choose another word.
* When a valid word is entered, it uses up letters from the hand.
* After every valid word: the score for that word and the total
score so far are displayed, the remaining letters in the hand
are displayed, and the user is asked to input another word.
* The sum of the word scores is displayed when the hand finishes.
* The hand finishes when there are no more unused letters.
The user may choose to end the hand at any time by inputting
a single period (the string '.') instead of a word.
* The final score is displayed.
hand: dictionary (string -> int)
word_list: list of strings'''

def play_hand(hand, word_list):
    word = input("Enter any word : ")
    if input == ".":
        break

    if word not in word_list:
        print("Invalid word , Enter another word ")

    
    score_total = 0

    for letter in word :
        
        hand[letter] -= 1
        if hand[letter] == 0:
            del hand[letter]
        print(hand)

    for i in hand:
        score_word = 0
        score_word += hand[i]
        print(score_word)

    