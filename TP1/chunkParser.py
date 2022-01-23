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
    patterns = """COMPOUND:{<DT>?<JJ>*<NN>}""" # le pattern qui spécifie la structure syntaxique à extraire

    chunker = RegexpParser(patterns)
    print("After Regex:", chunker)
    tree = chunker.parse(tokens_tag)
    print("After Chunking", tree)

## Partie qui extrait seulement les sous arbres qui ont la structure syntaxique souhaitée
    print("Only Matched Coumpound : ")
    matched_compound = []
    for subtree in tree.subtrees():
        if subtree.label() == 'COMPOUND':
            print(subtree)
            matched_compound.append(subtree)
    return matched_compound   # Si on veut tout écrire dans le fichier y compris
    #les élements qui ne sont pas "matchés" par le regexParser, il suffit de retourner tout le tree

def chunk_parse_file(file_name_in):

    f1 = open(file_name_in, "r")
    lines = f1.read()
    compounds = chunk_parse(lines)
    f1.close()

    f2 = open(sys.argv[1] + '.chk.nltk', "w")
    for i in range(len(compounds)):
        print("write compound : " + str(compounds[i]))
        f2.write(str(compounds[i]))
        f2.write("\n")

    f2.close()

if __name__ == '__main__':
    chunk_parse_file(sys.argv[1])