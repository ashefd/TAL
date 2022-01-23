import nltk
import sys

from nltk import pos_tag
from nltk import word_tokenize

def tokenize_tag(file_name_in):
    f = open(file_name_in, "r")

    text = []

    lines = f.read().splitlines()
    for line in lines:
        listing = nltk.word_tokenize(line)

        tag = nltk.pos_tag(listing)
        for t in tag:
            text.append(t)

    return text

def write_text_in_file(tokenized_tagged_text,  file_name_out):
    s = open(file_name_out, "w")
    for i in tokenized_tagged_text:
        s.write('\t'.join(i))
        s.write("\n")

    s.close()
    return tokenized_tagged_text

if __name__ == '__main__':
    tokenized_tagged_text = tokenize_tag(sys.argv[1])
    print(tokenized_tagged_text)

    write_text_in_file(tokenized_tagged_text, sys.argv[2])  # Deuxieme fichier donne
    print("tagged written in file" + sys.argv[2])


