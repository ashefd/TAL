import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser

def chunk_parse(text_file_name, pattern):
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
    text  = read_file(text_file_name)
    print(text)
    #Separation des lignes du text
    text = text.split()
    #Etiquettage (Tag) des mots de la liste
    tokens_tag = pos_tag(text)
    print("After Token:", tokens_tag)
    ##patterns = """COMPOUND:{<DT>?<JJ>*<NN>}""" # le pattern qui specifie la structure syntaxique à extraire

    chunker = RegexpParser(pattern)
    print("After Regex:", chunker)
    tree = chunker.parse(tokens_tag) #creation de l'arbre qui parse les mots etiquettes
    print("After Chunking", tree)

## Partie qui extrait seulement les sous arbres qui ont la structure syntaxique souhaitee
    print("Only Matched Coumpound : ")
    matched_compounds = []
    for subtree in tree.subtrees():
        if subtree.label() == 'COMPOUND':
            print(subtree)
            matched_compounds.append(subtree)
    return matched_compounds   # Si on veut tout ecrire dans le fichier y compris
    #les elements qui ne sont pas "matches" par le regexParser, il suffit de retourner tout le tree

def find_regex_rule(dict_file, structure):
    """
    Cette fonction permet de retrouver l'expression reguliere python (regex) qui correspond à une
    structure syntaxique donnee

    Parameters
    ----------

    dict_file : string
        Nom du fichier qui associe des structures syntaxiques à des expression regulieres python (Regex)

    structure : 
        nom de la structure syntaxique des mots à extraire
    
    Returns
    -------
    pattern : RegexpChunkRule
        Expression reguliere qui correspond à la structure syntaxique donnee en entree
    """
    lines = read_file(dict_file).split()
    pattern = ''
    for i in range(0, len(lines), 2):
        if(lines[i].lower() == structure):
            pattern = "COMPOUND:"+lines[i+1]

    return pattern

def read_file(file_name):
    """
    Cette fonction permet de lire un fichier et retourne une chaine de caractere
    qui correspond au texte du fichier

    Parameters
    ----------

    file_name : string
        nom du fichier qui contient le texte à retourner
    
    Returns
    -------
    lines : string
        Chaine de caractere qui contient l'integralite du texte du fichier
    """
    f1 = open(file_name, "r")
    lines = f1.read()
    f1.close()

    return lines
def write_compounds_in_file(compounds, structure, file_name):
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
    f3.write(structure + ": \n")
    for i in range(len(compounds)):
        print("Compound " + str(i) + " : " + str(compounds[i]))
        f3.write(str(compounds[i]))
        f3.write("\n")

    f3.close()

if __name__ == '__main__':

    pattern = find_regex_rule(sys.argv[2], sys.argv[3].lower())
    compounds = chunk_parse(sys.argv[1],  pattern)
    write_compounds_in_file(compounds, sys.argv[3], sys.argv[1] + '.chk.nltk')