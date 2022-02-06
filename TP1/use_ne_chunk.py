import nltk
import sys
import io
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def process_content(filename, tokenized):
    file = open(filename, 'w')
    try:
        with io.open(filename, 'w', encoding='utf8') as fout:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                namedEnt = nltk.ne_chunk(tagged, binary=False)
                #namedEnt.draw()
                #fout.write(str(namedEnt)+'\n\n')
                for subtree in namedEnt.subtrees():
                    if subtree.label() != 'S':
                        x = str(subtree)
                        fout.write(x[1:len(x)-1]+'\n')
                """
                ## Partie qui extrait seulement les sous arbres qui ont la structure syntaxique souhaitée
                    print("Only Matched Coumpound : ")
                    matched_compounds = []
                    for subtree in tree.subtrees():
                        if subtree.label() == 'COMPOUND':
                            print(subtree)
                            matched_compounds.append(subtree)
                    return matched_compounds   # Si on veut tout écrire dans le fichier y compris
                    #les élements qui ne sont pas "matchés" par le regexParser, il suffit de retourner tout le tree

                """
    
    except Exception as e:
        print(str(e))

if __name__ == '__main__':

    f = open(sys.argv[1], 'r') # wsj_0010_sample.txt
    file = open(sys.argv[2], 'w') # wsj_0010_sample.txt.ne.nltk
    lignes = f.read()

    # lignes = state_union.raw("2006-GWBush.txt")

    custom_sent_tokenizer = PunktSentenceTokenizer(lignes)

    tokenized = custom_sent_tokenizer.tokenize(lignes)

    process_content(sys.argv[2], tokenized) 


# python use_ne_chunk.py wsj_0010_sample.txt wsj_0010_sample.txt.ne.nltk