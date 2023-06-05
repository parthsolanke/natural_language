import nltk
import sys
import os
import string
import math

FILE_MATCHES = 2
SENTENCE_MATCHES = 1


def main():
    
    try:
        while True:
            # Check command-line arguments
            if len(sys.argv) != 2:
                sys.exit("Usage: python questions.py corpus")

            # Calculate IDF values across files
            files = load_files(sys.argv[1])
            file_words = {
                filename: tokenize(files[filename])
                for filename in files
            }
            file_idfs = compute_idfs(file_words)

            # Prompt user for query
            query = set(tokenize(input("Query: ")))

            # Determine top file matches according to TF-IDF
            filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

            # Extract sentences from top files
            sentences = dict()
            for filename in filenames:
                for passage in files[filename].split("\n"):
                    for sentence in nltk.sent_tokenize(passage):
                        tokens = tokenize(sentence)
                        if tokens:
                            sentences[sentence] = tokens

            # Compute IDF values across sentences
            idfs = compute_idfs(sentences)

            # Determine top sentence matches
            matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
            for match in matches:
                print(match)
    except KeyboardInterrupt:
        sys.exit(0)


def load_files(directory):
    # loading files into dictionary
    file_names = {}
    
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), "r", encoding="utf8") as f:
                file_names[file] = f.read()
                f.close()
                
    return file_names


def tokenize(document):
    # removing stopwords and punctuation
    tokens = []
    
    for word in nltk.word_tokenize(document):
        if word not in nltk.corpus.stopwords.words("english"):
            if not all([char in string.punctuation for char in word]):
                tokens.append(word.lower())
            
    return tokens


def compute_idfs(documents):
    # calculating number of documents containing word
    word_and_count = {}
    
    for file in documents:
        for word in documents[file]:
            if word not in word_and_count:
                word_and_count[word] = 1
            word_and_count[word] += 1
            
    # calculating idfs for words
    idf = {}        
    for word in word_and_count:
        idf[word] = math.log(len(documents) / word_and_count[word])
        
    return idf


def top_files(query, files, idfs, n):  
    # calculating tf-idf for each file
    tf_idf = {}
        
    for file in files:
        tf_idf[file] = 0
        for word in query:
            tf_idf[file] += files[file].count(word) * idfs[word]
                
    # sorting the files according to tf-idf
    sorted_files = sorted(tf_idf, key=tf_idf.get, reverse=True)
        
    return sorted_files[:n]


def top_sentences(query, sentences, idfs, n):
    # calculating idf for each sentence
    idf = {}
    
    # calculating tf-idf for each sentence
    for sentence in sentences:
        idf[sentence] = 0
        for word in query:
            if word in sentences[sentence]:
                idf[sentence] += idfs[word]
        query_term_density = sum([1 for word in query if word in sentences[sentence]]) / len(sentences[sentence])
        idf[sentence] = (idf[sentence], query_term_density)
        
    # sorting the sentences according to idf
    sorted_sentences = sorted(idf, key=lambda x: (idf[x][0], idf[x][1]), reverse=True)
    
    return sorted_sentences[:n]


if __name__ == "__main__":
    main()
