import sys
import re

def create_dictionary(file_name):
    """Creation d'un dictionnaire.

    Cette fonction permet de creer un dictionnaire a partir d'une liste de mot

    Parameters
    ----------

    Returns
    -------
    mydict : dictionary
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_universelle'
    """
    f = open(file_name, "r")
    lines = f.read().split()
    mydict = {}
    for i in range(0,len(lines),2):
        mydict[lines[i]] = lines[i+1]
    return mydict

def replace_etiquettes(file_name, dict_etiquettes):
    f = open(file_name, "r")
    lines = f.read().splitlines()


    for j in range(len(lines)):
        line = lines[j]
        line = line.split()
        for i in range(len(line)):
            if(i == 0):
                line[i] = dict_etiquettes[line[i]]
            else :
                line[i] = re.sub("([^\/]+$)", "", line[i]).replace("/", "")
        lines[j] = line
    return lines

def write_lines_file(lines, file_name_out):
    f = open(file_name_out, "w")
    for line in lines :
        f.writelines(" ".join(line))
        f.writelines("\n")

    f.close()


if __name__ == '__main__':

    dict_etiquettes = create_dictionary(sys.argv[2])
    lines = replace_etiquettes(sys.argv[1], dict_etiquettes )
    write_lines_file(lines, sys.argv[3])
    print("File with named entities with universal etiquettes written in " + sys.argv[3])