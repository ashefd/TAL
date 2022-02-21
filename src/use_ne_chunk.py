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
    #file = open(filename, 'w')
    try:
        with io.open(filename, 'a', encoding='utf8') as fout:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                namedEnt = nltk.ne_chunk(tagged, binary=False)
                #namedEnt.draw()
                #fout.write(str(namedEnt)+'\n\n')
                for subtree in namedEnt.subtrees():
                    if subtree.label() == 'S':
                        x = str(subtree)
                        #print(x)
                        inside = []
                        for element in x[3:len(x)-1].splitlines():
                            if element[0] == ' ':
                                inside.append(element[2:])
                            else:
                                single = element.split()
                                for s in single:
                                    inside.append(s)
                        #print(inside)
                        for element in inside:
                            line = element.translate({ ord(c): ' ' for c in "()/" })
                            element_in_line = line.split()
                            if(len(element_in_line) == 2):
                                fout.write(element_in_line[0] + '\tO' + '\n')
                            elif(len(element_in_line) > 2):
                                for w in range(1, len(element_in_line), 2):
                                    fout.write(element_in_line[w] + '\t' + element_in_line[0] + '\n')
                        
                        fout.write('\n')

                

    
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


    f = open(sys.argv[1], 'r') 
    file = open(sys.argv[2], 'w') 
    lignes = f.read().splitlines()

    for line in lignes:
        custom_sent_tokenizer = PunktSentenceTokenizer(line)

        tokenized = custom_sent_tokenizer.tokenize(line)

        process_content(sys.argv[2], tokenized) 
        #print("File with named entities written in " + sys.argv[2])
