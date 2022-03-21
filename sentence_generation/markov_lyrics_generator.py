#SHOULD ACTUALLY BE MARKOV FANCY HIGHBROW LITERATURE GENERATOR
import random

# This function handles input by opening a file and returning it as a string
def input(text):
    with open(text) as f:
        corpus = f.read()
    return corpus



#This function creates a dictionary where each key represents a string consisting of len(state_size) and the values are all strings that follow it, each of length state size.
def build_markov_2(corpus, state_size):
    corpus = corpus.split()#split the string input into a list of words
    markov = {}#create an empty dictionary to hold the model - keys and values are words
    for i in range(state_size, len(corpus) - state_size):
        current_word = ' '.join(corpus[i:i+state_size])
        previous_words = ' '.join(corpus[i-state_size:i])
        if previous_words in markov:
            markov[previous_words].append(current_word)
        else:
            markov[previous_words] = [current_word]
    return markov



# This function takes a model and returns a sentence, ending with a period.
def gen_text_2(model):
    word = random.choice(list(model.keys()))
    while word[0] not in "ABCDEFGHIJKLMNOPQRSTUVQXYZ":
        word = random.choice(list(model.keys()))
    sentence = word + " "
    while word in model.keys() and word[-1] != "." and word[-2:] != ".\""  and word[-1] != "/" :

        word = random.choice(model[word])
        sentence += word + " "
    return sentence



# This is like "main" in java - here is where we run the program by calling the functions
if __name__ == "__main__":
    body = input('proust.txt')
    # print(body)
    model = build_markov_2(body,2)
    sentence = gen_text_2(model)
    print(sentence)
    #print(dict(itertools.islice(model.items(), 2)))
