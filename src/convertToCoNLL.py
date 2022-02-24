import nltk
import sys
# Alya
def read_file(file_name):
    """lecture d'un fichier .

     Cette fonction permet de lire un fichier et retourner ses lignes dans un tableau

     Parameters
     ----------
     file_name : string
     Correspond au nom du fichier
     Returns
     -------
     lines : array of string
         tableau avec chaque élément étant une ligne du fichier d'entrée
     """
    f = open(file_name, "r") # fichier a remplacer

    lines = f.read().splitlines()
    f.close()
    return lines


def create_dictionary(lines):
    """Creation d'un dictionnaire.

     Cette fonction permet de creer un dictionnaire a partir d'une liste de mot

     Parameters
     ----------
    lines : array of string
    tableau qui contient les clés suivies de leur valeur
     Returns
     -------
     mydict : dictionary
         Dictionnaire ressemblant a  'étiquette NE recognizer' : 'etiquette coNLL'
     """
    mydict = {}
    for line in lines:
        words = line.split()
        mydict[words[0]] = words[1]
    return mydict

def convert_CoNLL(lines, mydict):
    """Conversion des étiquettes des NE recognizer en étiquette coNLL

        Cette fonction permet de convertir certaines étiquettes en étiquettes coNLL du dictionnaire en entrée

        Parameters
        ----------
       lines : array of string
       tableau qui contient les lignes pour lesquelles il faut convertir les étiquettes

           mydict : dictionary
            Dictionnaire ressemblant a  'étiquette NE recognizer' : 'etiquette coNLL'
        Returns
        -------
        lines_CoNLL : array of string
            le tableau d'entrée avec les étiquettes converties avec celle du dictionnaire  mydict
        """

    last_etiquette = ''
    lines_CoNLL = []
    for line in lines:
        if(len(line) != 0 and line.replace('\n', '') != ''): # si la ligne n'est pas vide
            words = line.split('\t')  #on sépare le mot de son tag
            if(words[1] != "O"): # si c'est une ne
                if(words[1] in mydict.keys() and last_etiquette != words[1]): #si l'étiquette est différente de celle d'avant
                    etiquette = "B-"+ mydict[words[1]] #alors c'est un B : debut de la ne

                else:

                    etiquette = "I-" + mydict[words[1]] #inside ne
                last_etiquette  =words[1] #l'étiquette a comparer est le dernier tag rencontré
            else:
                etiquette = "O"
                last_etiquette =  "O"
            lines_CoNLL.append(words[0] + '\t' + etiquette +"\n") #on ajoute la ligne avec le bon tag converti

    return lines_CoNLL

def writeLines(lines, file_out):
    """écriture dans un fichier .

       Cette fonction permet d'écrire des lignes dans un fichier

       Parameters
       ----------
       file_out : string
       Correspond au nom du fichier de sortie

       lines: array of string
       le tableau des lignes à écrire
       Returns
       -------
        void
       """
    file = open(file_out, 'w')
    file.writelines(lines)

if __name__ == '__main__':

    lines = read_file(sys.argv[1])
    dict_lines = read_file(sys.argv[2])

    coNLL_dict = create_dictionary(dict_lines)
    lines_CoNLL = convert_CoNLL(lines, coNLL_dict)

    file_name = sys.argv[1] + '.conll'
    writeLines(lines_CoNLL,   file_name )

    print("Original file " + sys.argv[1]  + "  with conll tags written in " + file_name)
