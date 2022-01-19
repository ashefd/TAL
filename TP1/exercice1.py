import nltk
import sys
from nltk import word_tokenize
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')

if __name__ == '__main__':
    print(sys.argv[1]) # Premier fichier donne
    print(sys.argv[2]) # Deuxieme fichier donne
    print("\n\n\n")

    f = open(sys.argv[1], "r")
    s = open(sys.argv[2], "w")

    text = []

    lines = f.read().splitlines()
    for line in lines:
        listing = nltk.word_tokenize(line)

        tag = nltk.pos_tag(listing)
        for t in tag:
            text.append(t)
        
    for i in range(len(text)):
        s.write('\t'.join(text[i]))
        s.write("\n")

    s.close()
