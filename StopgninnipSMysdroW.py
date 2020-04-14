
def spin_words(sentence):
    # Your code goes 
    words = sentence.split()
    new_sentence = ""
    #Welcome
    
    for word in range(0,len(words),1):
        if word >0:
            new_sentence += " "
        if len(words[word]) >= 5:
            new_sentence += (spin(words[word]))
        else:
            new_sentence += words[word]
    return new_sentence
def spin(word):
    letters = len(word)
    new_word =''
    for letter in range(len(word)-1,-1,-1):
        new_word += word[letter]
    
    return new_word
