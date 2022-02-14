import nltk
import sys

def read_file(file_name1, file_name2, file_name3):
    """Lecture de trois fichiers.

    Cette fonction permet de lire trois fichiers et de renvoyer chacun leur contenu "mot par mot" dans une liste de string

    Parameters
    ----------
    file_name1 : string
        Le premier fichier a lire.
    file_name2 : string
        Le deuxieme fichier a lire.
    file_name3 : string
        Le troisieme fichier a lire.

    Returns
    -------
    lines1
        liste contenant les mots de file_name1
    lines2
        liste contenant les mots de file_name2
    lines3
        liste contenant les mots de file_name3
    """
    f1 = open(file_name1, "r") # fichier a remplacer
    f2 = open(file_name2, "r") # fichier a remplacer
    f3 = open(file_name3, "r") # post-tag

    lines1 = f1.read().split()
    lines2 = f2.read().split()
    lines3 = f3.read().split()

    f1.close()
    f2.close()
    f3.close()

    return lines1, lines2, lines3


def create_dictionary(lines):
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
    mydict = {}
    for i in range(0,len(lines),2):
        mydict[lines[i]] = lines[i+1]
    return mydict


def write_with_uni_tag(file_name1, file_name2, lines1, lines2, mydict):
    """Reecriture des categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Cette fonction permet de remplacer les categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Parameters
    ----------
    file_name1 : string
        Le premier fichier a reecrire
    file_name2 : string
        Le deuxieme fichier a reecrire
    lines1 : 
        liste contenant les mots de file_name1 et leur categorie grammaticale
    lines2 :
        liste contenant les mots de file_name2 et leur categorie grammaticale
    mydict : 
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_universelle'
    Returns
    -------
    None
    """
    f1 = open(file_name1, "w") # fichier a remplacer
    f2 = open(file_name2, "w") # fichier a remplacer

    for i in range(0,len(lines1),2):
        f1.write("\t".join((lines1[i], mydict[lines1[i+1]])))
        f1.write("\n")

        f2.write("\t".join((lines2[i], mydict[lines2[i+1]])))
        f2.write("\n")

    f1.close()
    f2.close()



if __name__ == '__main__':

    lines1, lines2, lines3 = read_file(sys.argv[1], sys.argv[2], sys.argv[3])

    mydict = create_dictionary(lines3)


    #Si on veut donner des noms spécifiques '.harm' aux fichiers harmonisés :
    nltk_out = sys.argv[1][:-9] + "univ"+sys.argv[1][-5:]
    ref_out =  sys.argv[2][:-8] + "univ"+sys.argv[2][-4:]

    write_with_uni_tag(nltk_out, ref_out, lines1, lines2, mydict)
    print("files with universal etiquettes written in file " + nltk_out + " and  " + ref_out)
    