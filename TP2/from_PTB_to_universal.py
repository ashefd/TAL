import nltk
import sys
import re
from nltk import pos_tag
from nltk import RegexpParser

def create_dictionary(dictionnaire_file):
    """Creation d'un dictionnaire.
    Cette fonction permet de creer un dictionnaire a partir d'une liste de mot

    Parameters
    ----------
    dictionnaire_file : string
        Nom du fichier contenant le dictionnaire a creer

    Returns
    -------
    mydict : dictionary
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_universelle'
    """
    f = open(dictionnaire_file, 'r')
    lines = f.read().split()

    mydict = {}
    for i in range(0,len(lines),2):
        mydict[lines[i]] = lines[i+1]

    return mydict

def convert_PTB_to_universal(file_in_name, file_out_name, dictionnaire):
    """Cette fonction permet de convertir les categories grammaticales Penn TreeBank en leur categorie grammaticale
    universelle a partir d'un dictionnaire

    Parameters
    ----------
    file_in_name : string
        Nom du fichier a modifier

    file_out_name : string
        Nom du fichier, output, contenant le texte du fichier 'file_in_name' mais avec les categories grammaticales universelles
    
    dictionnaire : dictionary
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_universelle'

    Returns
    -------
    lines : list of string
        Liste de string provenant du fichier 'file_in_name' mais avec les categories grammaticales universelles
    """
    f = open(file_in_name, "r")
    g = open(file_out_name, "w")
    lines = f.read().splitlines()

    for i in range(len(lines)):
        line = lines[i].split()
        for j in range(len(line)):
            m = re.findall(r"_[^_]+$", line[j])
            line[j] = line[j].replace(m[0][1:], dictionnaire[m[0][1:]])
        g.write(' '.join(line) + '\n')
    f.close()
    g.close()
    return lines


if __name__ == '__main__':
    # sys.argv[1] : premier fichier a convertir
    # sys.argv[2] : deuxieme fichier a convertir
    # sys.argv[3] : dictionnaire a utiliser
    # sys.argv[4] : premier fichier a enregistrer
    # sys.argv[5] : deuxieme fichier a enregistrer
    mydict = create_dictionary(sys.argv[3])

    convert_PTB_to_universal(sys.argv[1], sys.argv[4], mydict)
    convert_PTB_to_universal(sys.argv[2], sys.argv[5], mydict)

