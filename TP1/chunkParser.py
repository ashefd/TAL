import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser

def chunk_parse(text_file_name, pattern):
    """ Extraction de chunk "matchant" un pattern.

    Cette fonction permet d'extraire  d'un texte des groupes de mots correspondants
    à un schéma (structure) syntaxique donné.

    Parameters
    ----------
    text_file_name : string
        Nom du fichier qui contient le texte duquel on souhaite extraire les "chunk" (groupes de mots)

    pattern : RegexpChunkRule
             Une expression régulière qui représente la structure syntaxique (pattern) des mots que l'on souhaite
             extraire
    Returns
    -------
    matched_compounds : list of string
        Liste de groupes de mots (chunks) qui ont concordé (matché) avec le pattern donné en entrée
    """
    text  = read_file(text_file_name)
    print(text)
    #Séparation des lignes du text
    text = text.split()
    #Etiquettage (Tag) des mots de la liste
    tokens_tag = pos_tag(text)
    print("After Token:", tokens_tag)
    ##patterns = """COMPOUND:{<DT>?<JJ>*<NN>}""" # le pattern qui spécifie la structure syntaxique à extraire

    chunker = RegexpParser(pattern)
    print("After Regex:", chunker)
    tree = chunker.parse(tokens_tag) #création de l'arbre qui parse les mots étiquettés
    print("After Chunking", tree)

## Partie qui extrait seulement les sous arbres qui ont la structure syntaxique souhaitée
    print("Only Matched Coumpound : ")
    matched_compounds = []
    for subtree in tree.subtrees():
        if subtree.label() == 'COMPOUND':
            print(subtree)
            matched_compounds.append(subtree)
    return matched_compounds   # Si on veut tout écrire dans le fichier y compris
    #les élements qui ne sont pas "matchés" par le regexParser, il suffit de retourner tout le tree

def find_regex_rule(dict_file, structure):
    """

       Cette fonction permet de retrouver l'expression régulière python (regex) qui correspond à une
       structure syntaxique donnée

       Parameters
       ----------

       dict_file : string
       nom du fichier qui associe des structures syntaxiques à des expression régulières python (Regex)

       structure : nom de la structure syntaxique des mots à extraire
       Returns
       -------
       pattern : RegexpChunkRule
           Expression régulière qui correspond à la structure syntaxique donnée en entrée
       """
    lines = read_file(dict_file).split()
    pattern = ''
    for i in range(0, len(lines), 2):
        if(lines[i].lower() == structure):
            pattern = "COMPOUND:"+lines[i+1]

    return pattern

def read_file(file_name):
    """

            Cette fonction permet de lire un fichier et retourne une chaine de caractère
            qui correspond au texte du fichier

            Parameters
            ----------

            file_name : string
            nom du fichier qui contient le texte à retourner
            Returns
            -------
           lines : string
                Chaine de caractère qui contient l'intégralité du texte du fichier
            """
    f1 = open(file_name, "r")
    lines = f1.read()
    f1.close()

    return lines
def write_compounds_in_file(compounds, structure, file_name):
    """

          Cette fonction permet d'écrire dans un fichier les éléments de la liste compound,
          en précisant au début le nom de la structure syntaxique qui concerne ces éléments

          Parameters
          ----------
          compounds : list of string
          Liste de mots composés qui match la syntaxe "structure"
          structure : string
          nom de la structure syntaxique des mots à extraire
          file_name : string
          nom du fichier dans lequel on souhaite ecrire


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