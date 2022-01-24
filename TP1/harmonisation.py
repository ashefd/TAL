import nltk
import sys

def read_file(file_name1, file_name2):
    """Lecture de deux fichiers.

    Cette fonction permet de lire deux fichiers

    Parameters
    ----------
    file_name1 : string
        Le premier fichier a lire.
    file_name2 : string
        Le second fichier a lire.

    Returns
    -------
    lines1
        Le produit des deux nombres.
    lines2
        Le produit des deux nombres.
    """
    f1 = open(file_name1, "r") # Premier fichier donne
    f2 = open(file_name2, "r") # ref
    lines1 = f1.read().split()
    lines2 = f2.read().split()
    f1.close()
    f2.close()
    return lines1, lines2


def harmonise(lines1, lines2):
    """Lecture de deux fichiers.

    Cette fonction permet de lire deux fichiers

    Parameters
    ----------
    file_name1 : string
        Le premier fichier a lire.
    file_name2 : string
        Le second fichier a lire.

    Returns
    -------
    lines1
        Le produit des deux nombres.
    lines2
        Le produit des deux nombres.
    """

    text1 = []
    text2 = []


    for i in range(0,len(lines1),2):
        if(lines2[i] != lines1[i]):
            print(lines2[i])
            print(lines1[i])
        else : 
            text1.append((lines1[i], lines1[i+1]))
            text2.append((lines2[i], lines2[i+1]))
    return text1, text2
    

def write_text_in_file(file_name_out1,  file_name_out2, text1, text2):
    """Ecriture de deux fichiers.

    Cette fonction permet de lire deux fichiers

    Parameters
    ----------
    file_name1 : string
        Le premier fichier a lire.
    file_name2 : string
        Le second fichier a lire.

    Returns
    -------
    lines1
        Le produit des deux nombres.
    lines2
        Le produit des deux nombres.
    """
    f1 = open(file_name_out1, "w") # Premier fichier donne
    f2 = open(file_name_out2, "w") # ref

    for i in range(len(text1)):
        f1.write("\t".join(text1[i]))
        f1.write("\n")

        f2.write("\t".join(text2[i]))
        f2.write("\n")

    f1.close()
    f2.close()


if __name__ == '__main__':
    lines1, lines2 = read_file(sys.argv[1], sys.argv[2])

    text1, text2 = harmonise(lines1, lines2)

    #write_text_in_file(sys.argv[1],  sys.argv[2], text1, text2)