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
                        for element in x[3:len(x)-1].splitlines():       
                            print(element)
                            line = element.translate({ ord(c): ' ' for c in "()/" })
                            print(line)
                            #print(line.split())
                            #print(x[3:len(x)-1].splitlines())
                            #print(x[2:len(x)-1] + '\n')
                            element_in_line = line.split()
                            fout.write(' '.join(element_in_line) + '\n')

                            print(element_in_line)
                            '''
                            if(len(element_in_line) > 1):
                                print('sup a 1')
                                fout.write(element_in_line[1] + '\t' + element_in_line[2] + '\n')
                            else:
                                fout.write(element_in_line[0] + '\t' + element_in_line[1] + '\n')
                            '''
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

    for line in lignes[:5]:
        custom_sent_tokenizer = PunktSentenceTokenizer(line)

        tokenized = custom_sent_tokenizer.tokenize(line)

        process_content(sys.argv[2], tokenized) 
        #print("File with named entities written in " + sys.argv[2])
