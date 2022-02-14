import nltk
import sys
import re
from nltk import pos_tag
from nltk import RegexpParser

def convertTabToUnderscore(filename):
    """Cette fonction permet de convertir les tabulations d'un texte en underscore _

    Parameters
    ----------
    filename : string
        Nom du fichier a modifier

    Returns
    -------
    lines : list of string
        Liste de string provenant du fichier 'filename' mais avec les underscores
    """
    f = open(filename, "r")
    lines = f.read().splitlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\t', '_')
    return lines


if __name__ == '__main__':
    """Permet de convertir les tabulations d'un texte en underscore _ et l'enregistrer dans un autre fichier

    'Parameters'
    ----------
    sys.argv[1] : string
        Nom du fichier a modifier

    sys.argv[2] : string
        Nom du fichier, output

    Returns
    -------
    None
    """
    lines = convertTabToUnderscore(sys.argv[1])
    f = open(sys.argv[2], 'w')
    f.write(' '.join(lines))