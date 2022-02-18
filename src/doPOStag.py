import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser

def nltk_parse(text_file_name):
    """ Extraction de chunk "matchant" un pattern.

    Cette fonction permet d'extraire  d'un texte des groupes de mots correspondants
    à un schema (structure) syntaxique donne.

    Parameters
    ----------
    text_file_name : string
        Nom du fichier qui contient le texte duquel on souhaite extraire les "chunk" (groupes de mots)

    pattern : RegexpChunkRule
        Une expression reguliere qui represente la structure syntaxique (pattern) des mots que l'on souhaite
        extraire

    Returns
    -------
    matched_compounds : list of string
        Liste de groupes de mots (chunks) qui ont concorde (matche) avec le pattern donne en entree
    """
    text  = open(text_file_name, 'r')
    print(text)
    line_tag = []
    lines = text.read().splitlines()
    for line in lines:
        line_tag.append(pos_tag(line.split()))
    print(line_tag)
    """
    #Separation des lignes du text
    text = text.read().split()
    #Etiquettage (Tag) des mots de la liste
    tokens_tag = pos_tag(text)
    """
    #print("After Token:", tokens_tag)
    ##patterns = """COMPOUND:{<DT>?<JJ>*<NN>}""" # le pattern qui specifie la structure syntaxique à extraire

    return line_tag

def write_compounds_in_file(list_of_tags, file_name):
    """
    Cette fonction permet d'ecrire dans un fichier les elements de la liste compound,
    en precisant au debut le nom de la structure syntaxique qui concerne ces elements

    Parameters
    ----------
    compounds : list of string
        Liste de mots composes qui match la syntaxe "structure"
    structure : string
        Nom de la structure syntaxique des mots à extraire
    file_name : string
        Nom du fichier dans lequel on souhaite ecrire
        
    Returns
    -------
    void
    """
    f3 = open(file_name, "w")
    for line_tag in list_of_tags:
        for i in range(len(line_tag)):
            print(str(i) + " : " + str(line_tag[i]))
            f3.write('\t'.join(line_tag[i]))
            f3.write("\n")
        f3.write('\n')
    f3.close()

if __name__ == '__main__':

    list_of_tags = nltk_parse(sys.argv[1])
    print(list_of_tags)
    write_compounds_in_file(list_of_tags, "out/pos_test.txt.pos.nltk")