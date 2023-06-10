# Reverse words

# Testcases
# Input : str ="" geeks quiz practice code""
# Output : str = code practice quiz geeks  
# Input : str = ""my name is laxmi""
# output : str= laxmi is name my

def rev_sentence(sentence):
    words = sentence.split()
    reverse = words[::-1] 
    
    reverse_sentence = ''
    for i in reverse:
        reverse_sentence += i + " "

    #reverse_sentence = ' '.join(reverse)
    return reverse_sentence