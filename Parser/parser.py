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
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    np_chunks = []
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            np_chunks.append(subtree)         
    return np_chunks


if __name__ == "__main__":
    main()
