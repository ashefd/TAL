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
    lines : list of string
        Liste a 1 dimension contenant 'une_categorie_grammaticale', 'la_categorie_grammaticale_universelle'


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
    f = open(file_in_name, "r")
    g = open(file_out_name, "w")

    lines = f.read().splitlines()
    print(lines)
    for i in range(len(lines)):
        m = re.findall(r"_[A-Z]*", lines[i])
        print(m)
        #lines[i] = re.sub(r"_[^_]+$", )
    return lines


if __name__ == '__main__':
    # sys.argv[1] : premier fichier a convertir
    # sys.argv[2] : deuxieme fichier a convertir
    # sys.argv[3] : dictionnaire a utiliser
    # sys.argv[4] : premier fichier a enregistrer
    # sys.argv[5] : deuxieme fichier a enregistrer
    mydict = create_dictionary(sys.argv[3])

    #convert_PTB_to_universal(sys.argv[1], sys.argv[4], mydict)
    convert_PTB_to_universal(sys.argv[2], sys.argv[5], mydict)

