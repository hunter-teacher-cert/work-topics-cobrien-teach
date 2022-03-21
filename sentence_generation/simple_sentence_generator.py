import random

articles = ["a", "the", "one", "some"]
nouns = ["apple", "carrot", "rabbit", "banana", "basketball", "chess", "sun", "wind"]

#this list inlcudes both intransitive and transitive, should be decombosed
verbs = ["cooks", "blows", "bounces", "walks", "jumps", "calls", "stays", "runs", "abides"]
#NOTE modified list of conjunctions 'for' is a preposition not a conjunction! 'nor' is complicated because of it's semantics ( it must appear in
#the scope of a negation operator).
conjunctions = ["and", "or", "but", "yet", "so"]
dependent_clause_markers = ["although", "even if", "until", "when", "whether", "while", "in order to"]

"""
Simple context-free Phrase Structure grammar

simpleS -> NP VP
NP -> article noun
VP -> verb NP
S -> simpleS conjunction simpleS || simpleS dependent_clause_marker simpleS || simpleS




"""

def simple_S():
    return NP() + " " + VP()


def NP():
    return random.choice(articles) + " " + random.choice(nouns)

def VP():
    return random.choice(verbs) + " " + NP()
def S():
    my_choice = random.randrange(0,3)
    if my_choice == 0:
        return simple_S()() + " " + random.choice(conjunctions) + " " + simple_S()()
    elif my_choice == 1:
        return simple_S()() + " " + random.choice(dependent_clause_markers) + " " + simple_S()()
    else:
        return simple_S()



if __name__ == "__main__":
    #test print for simple sentence
    sentence = S()
    print(sentence)
    #complex_sentence = complex_S()
    #print(complex_sentence)
