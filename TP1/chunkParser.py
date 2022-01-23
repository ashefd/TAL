import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser

def chunk_parse(text, patterns):

    print(text)
    text = text.split()
    print("After Split:", text)
    tokens_tag = pos_tag(text)
    print("After Token:", tokens_tag)
    ##patterns = """COMPOUND:{<DT>?<JJ>*<NN>}""" # le pattern qui spécifie la structure syntaxique à extraire

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

def chunk_parse_file(text_to_chunk_file, dict_file, structure):

    f2 = open(dict_file, "r")
    lines = f2.read().split()
    patterns = ''
    for i in range(0, len(lines), 2):
        if(lines[i].lower() == structure):
            patterns = "COMPOUND:"+lines[i+1]

    f2.close()

    f1 = open(text_to_chunk_file, "r")
    lines = f1.read()
    compounds = chunk_parse(lines, patterns)
    f1.close()

    f3 = open(sys.argv[1] + '.chk.nltk', "w")
    f3.write(structure + ": \n")
    for i in range(len(compounds)):
        print("write compound : " + str(compounds[i]))
        f3.write(str(compounds[i]))
        f3.write("\n")

    f3.close()

if __name__ == '__main__':
    chunk_parse_file(sys.argv[1], sys.argv[2], sys.argv[3].lower())
