import nltk
import sys
import io
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Tsha 
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
    try:
        with io.open(filename, 'a', encoding='utf8') as fout: # rajouter dans le ficher filename
            for i in tokenized:
                words = nltk.word_tokenize(i)   # on obtient la liste des tokens
                tagged = nltk.pos_tag(words)    # on associe un tag pour chaque token
                namedEnt = nltk.ne_chunk(tagged, binary=False) # on regarde les liens (entites nommees) entre chaque token

                for subtree in namedEnt.subtrees(): # on regarde dans l'arbre des liens
                    if subtree.label() == 'S': # si c'est une phrase
                        x = str(subtree)

                        for element in x[3:len(x)-1].splitlines(): # pour chaque lien contenu dans la phrase
                            line = element.translate({ ord(c): ' ' for c in "()/" }) # on remplace les () et / par un espace
                            element_in_line = line.split()

                            if(len(element_in_line) == 2): # si on n'a pas d'entite nommee dans cette ligne
                                fout.write(element_in_line[0] + '\tO' + '\n') # on la reecrit directement en ajoutant une tabulation

                            elif('/' not in element.split()[0]): # s'il n'y a pas de tag dans le tout premier element, ie : si la ligne est une entite nommee (PERSON, ORGANISATION)
                                for w in range(1, len(element_in_line), 2):
                                    fout.write(element_in_line[w] + '\t' + element_in_line[0] + '\n')

                            else: # Sinon, on est bien dans une phrase
                                for w in range(0, len(element_in_line), 2):
                                    fout.write(element_in_line[w] + '\tO' + '\n') # on la reecrit directement en ajoutant une tabulation
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
        exemple : 
        Mary Barra appointed as General Motors chief 
        December 10 , 2013 
        The United States 's largest car manufacturer General Motors today named Mary Barra as its new chief executive . 

    sys.argv[2] : string
        Nom du fichier output qui contiendra l'ensemble des entites nommees identifiees

    Returns
    -------
    None

    contenu du fichier final sys.argv[2]
    exemple :
        Mary	PERSON
        Barra	PERSON
        appointed	O
        as	O
        General	ORGANIZATION
        Motors	ORGANIZATION
        chief	O
        December	O
        10	O
        ,	O
        2013	O
        The	O
        United	GPE
        States	GPE
        's	O
        largest	O
        car	O
        manufacturer	O
        General	ORGANIZATION
        Motors	ORGANIZATION
        today	O
        named	O
        Mary	PERSON
        Barra	PERSON
        as	O
        its	O
        new	O
        chief	O
        executive	O
        .	O
    """
    nltk.download('words')
    nltk.download('maxent_ne_chunker')


    f = open(sys.argv[1], 'r') 
    file = open(sys.argv[2], 'w') 

    lignes = f.read()

    custom_sent_tokenizer = PunktSentenceTokenizer(lignes)

    tokenized = custom_sent_tokenizer.tokenize(lignes)

    process_content(sys.argv[2], tokenized) 
    print("File with named entities written in " + sys.argv[2])
