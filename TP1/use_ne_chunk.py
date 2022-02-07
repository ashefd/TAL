import nltk
import sys
import io
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def process_content(filename, tokenized):
    """ Recuperer les entites nommees d'un fichier pour le stocker dans un autre

    Cette fonction permet de recuperer les entites nommees d'un fichier pour le stocker dans un autre

    Parameters
    ----------
    filename : string
        Nom du fichier qui contient le texte duquel on souhaite extraire les "chunk" (groupes de mots)

    tokenized : Tokenizer choisi
        Tokenizer choisi dans le main

    Returns
    -------
    None
    """
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
    
    except Exception as e:
        print(str(e))

if __name__ == '__main__':

    f = open(sys.argv[1], 'r') # wsj_0010_sample.txt
    file = open(sys.argv[2], 'w') # wsj_0010_sample.txt.ne.nltk
    lignes = f.read()

    custom_sent_tokenizer = PunktSentenceTokenizer(lignes)

    tokenized = custom_sent_tokenizer.tokenize(lignes)

    process_content(sys.argv[2], tokenized) 


# python use_ne_chunk.py wsj_0010_sample.txt wsj_0010_sample.txt.ne.nltk