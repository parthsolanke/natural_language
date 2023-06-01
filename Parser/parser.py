import nltk
import sys
import grammar as g

# creating a grammer object to read from the string of grammer rules 
grammar = nltk.CFG.fromstring(g.NONTERMINALS + g.TERMINALS)

# creating a parser variable to save and parse the grammer
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    words = []
    for word in sentence.split():
        # isalpha() checks if the word contains alphabets
        if word.isalpha():
            words.append(word.lower())
    return words


def np_chunk(tree):
    # creating a list to store the noun phrases
    np_chunks = []
    
    # iterating through the subtrees of the tree
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            if not list(subtree.subtrees(lambda t: t.label() == "NP" and t != subtree)):
                np_chunks.append(subtree)         
    return np_chunks


if __name__ == "__main__":
    main()
