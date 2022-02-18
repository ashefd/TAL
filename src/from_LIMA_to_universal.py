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

    lines1 = f1.read().splitlines()
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




def createDirectDictionary(dictionary_LIMA_PTB, dictionary_PTB_universal):
    direct = {}

    for key in dictionary_LIMA_PTB : 
        value = dictionary_LIMA_PTB[key]
        if(value in dictionary_PTB_universal):
            #print(key + " " + value + "\n")
            direct[key] = dictionary_PTB_universal[value]
    return direct


def write_with_uni_tag(lines, file_name_out, dictionary_LIMA_universal):
    """Reecriture des categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Cette fonction permet de remplacer les categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Parameters
    ----------
    lines : array of string
        Le premier fichier a reecrire
    file_name2 : string
        Le deuxieme fichier a reecrire

    Returns
    -------
    None
    """
    f = open(file_name_out, "w") # fichier resultat

    for i in range(0,len(lines)):
        x = lines[i].split('\t')
        if(len(x) >= 2):
            f.write("\t".join((x[0], dictionary_LIMA_universal[x[1]])))
        f.write("\n")
    f.close()



if __name__ == '__main__':
    # sys.argv[1] : lima file
    # sys.argv[2] : dictionary from lima to PTB
    # sys.argv[3] : dictionary from PTB to universal


    lines1, lines2, lines3 = read_file(sys.argv[1], sys.argv[2], sys.argv[3])

    #print(lines1)
    dictionary_LIMA_PTB = create_dictionary(lines2)
    #print(dictionary_LIMA_PTB)

    dictionary_PTB_universal = create_dictionary(lines3)
    #print(dictionary_PTB_universal)

    dictionary_LIMA_universal = createDirectDictionary(dictionary_LIMA_PTB, dictionary_PTB_universal)
    #print(dictionary_LIMA_universal)

    lima_out = "out/" + sys.argv[1][8:-5] + ".univ"+sys.argv[1][-5:]
    print(lima_out)

    write_with_uni_tag(lines1, lima_out, dictionary_LIMA_universal)

    #Si on veut donner des noms spécifiques '.harm' aux fichiers harmonisés :
    """
    nltk_out = sys.argv[1][:-9] + "univ"+sys.argv[1][-5:]
    ref_out =  sys.argv[2][:-8] + "univ"+sys.argv[2][-4:]

    write_with_uni_tag(nltk_out, ref_out, lines1, lines2, mydict)
    print("files with universal etiquettes written in file " + nltk_out + " and  " + ref_out)
    """