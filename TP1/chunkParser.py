import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser

def chunk_parse(text):
    print(text)
    text = text.split()
    print("After Split:", text)
    tokens_tag = pos_tag(text)
    print("After Token:", tokens_tag)
    patterns = """Compound:{<DT>?<JJ>*<NN>}"""
    chunker = RegexpParser(patterns)
    print("After Regex:", chunker)
    output = chunker.parse(tokens_tag)
    print("After Chunking", output)

def chunk_parse_file(file_name_in):

    f1 = open(file_name_in, "r")  # Premier fichier donne
    lines = f1.read()
    print(chunk_parse(lines))

    f1.close()

if __name__ == '__main__':
    chunk_parse_file(sys.argv[1])