import nltk
import sys
import io
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

def process_content(filename, tokenized):
    """ Recuperer l'ensemble des entites nommees identifiees contenu dans une liste de mot tokenisee.
    Cet ensemble est ensuite stocke dans un fichier

    Parameters
    ----------
    filename : string
        Nom du fichier dans lequel on stocke les entites nommees

    tokenized : list of string
        Liste des mots tokenisee contenus dans un fichier txt

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
    """ Recuperer l'ensemble des entites nommees identifiees contenu dans un fichier txt.
    Cet ensemble est ensuite stocke dans un autre fichier

    Parameters
    ----------
    sys.argv[1] : string
        Nom du fichier que l'on souhaite etudier. Le fichier contient un texte dont on souhaite extraire les "chunk" (groupes de mots)

    sys.argv[2] : string
        Nom du fichier output qui contiendra l'ensemble des entites nommees identifiees

    Returns
    -------
    None
    """
    nltk.download('words')
    nltk.download('maxent_ne_chunker')


    f = open(sys.argv[1], 'r') # wsj_0010_sample.txt
    file = open(sys.argv[2], 'w') # wsj_0010_sample.txt.ne.nltk
    lignes = f.read()

    custom_sent_tokenizer = PunktSentenceTokenizer(lignes)

    tokenized = custom_sent_tokenizer.tokenize(lignes)

    process_content(sys.argv[2], tokenized) 
    print("File with named entities written in " + sys.argv[2])

# python use_ne_chunk.py wsj_0010_sample.txt wsj_0010_sample.txt.ne.nltk