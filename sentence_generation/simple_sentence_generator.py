import random

articles = ["a", "the", "one", "some"]
#removed Chess, this is a proper noun (note: cant say "I saw a chesss")
nouns = ["apple", "carrot", "rabbit", "banana", "basketball", "sun", "wind"]
#this list inlcudes both intransitive and transitive, should be decombosed
#removed stays, all other verbs in list are ambiguous between transitive and intransitive
verbs = ["cooks", "blows", "bounces", "walks", "jumps", "calls", "runs", "abides"]
#NOTE modified list of conjunctions 'for' is a preposition not a conjunction! 'nor' is complicated because of it's semantics ( it must appear in
#the scope of a negation operator).
conjunctions = ["and", "or", "but", "yet", "so"]
#"in order to" removed (applies to VPs not sentences). changed "whether" to "whenver" since former only goes with certain verbs.
dependent_clause_markers = ["although", "even if", "until", "when", "whenever", "while"]

"""
Simple context-free  grammar for a fragment of English. "||" represents disjunction. NP = Noun Phrase, VP = Verb Phrases

simpleS -> NP VP
NP -> article noun
simpleVP -> verb NP || verb
VP -> simpleVP + dependent_clause_marker + S || simpleVP
S -> simpleS conjunction simpleS || simpleS



"""

def simpleS():
    return NP() + " " + VP()


def NP():
    return random.choice(articles) + " " + random.choice(nouns)

def simpleVP():
    my_choice = random.randrange(0,2)
    if my_choice ==0:
        return random.choice(verbs) + " "+  NP()
    else :
        return random.choice(verbs)

def VP():
    my_choice = random.randrange(0,2)
    if my_choice == 0:
        return simpleVP() + " " + random.choice(dependent_clause_markers) + " " + simpleS();
    else:
        return simpleVP()
def S():
    my_choice = random.randrange(0,2)
    if my_choice == 0:
        return simpleS() + " " + random.choice(conjunctions) + " " + simpleS()
    else:
        return simpleS()



if __name__ == "__main__":
    #test print for simple sentence
    sentence = S()
    print(sentence)
    #complex_sentence = complex_S()
    #print(complex_sentence)
