import nltk
import sys
# Tsha et Alya

def read_file(file_name):

    f = open(file_name, "r") # fichier a remplacer

    lines = f.read().splitlines()
    f.close()
    return lines


def create_dictionary(lines):
    """Creation d'un dictionnaire.

    Cette fonction permet de creer un dictionnaire a partir d'une liste de lignes

    Parameters
    ----------
    lines : list of string
        Liste a 2 dimensions contenant 'une_categorie_grammaticale', 'la_categorie_grammaticale_dans_un_autre_type'
        exemple :
            ["SCONJ CC", "SENT .", "COMMA ,"]

    Returns
    -------
    mydict : dictionary
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_dans_un_autre_type'
        exemple : 
            SCONJ CC
            SENT .
            COMMA ,
    """
    mydict = {}
    for line in lines:
        words = line.split()
        mydict[words[0]] = words[1]
    return mydict


def write_with_uni_tag(file_name, lines, mydict):
    """Reecrit un fichier en remplacant ses tag par d'autres tags

    Parameters
    ----------
    file_name : string
        Nom du fichier dans lequel on stocke le tout

    lines : list of string
        Liste des lignes dans lequel on doit remplacer les tag par d'autres tags

    mydict : dictionary
        Dictionnaire ressemblant a  'une_categorie_grammaticale' : 'la_categorie_grammaticale_dans_un_autre_type'
        exemple : 
            SCONJ CC
            SENT .
            COMMA ,

    Returns
    -------
    None



    content of lines :
    ,	,
    ,	,
    will	MD
    join	VB
    the	DT
    board	NN
    as	IN
    a	DT
    nonexecutive	JJ
    director	NN
    .	.

    content of file_name
    ,	.
    ,	.
    will	VERB
    join	VERB
    the	DET
    board	NOUN
    as	ADP
    a	DET
    nonexecutive	ADJ
    director	NOUN
    .	.
    """
    f = open(file_name, "w") # fichier 

    # print(mydict)
    for line in lines:
        # print((line))
        if(len(line) != 0):
            words = line.split('\t')

            f.write("\t".join((words[0], mydict[words[1]]))) # on reecrit la ligne en remplacant le tag par le tag associe d'apres le dictionnaire mydict

        f.write("\n")

    f.close()



if __name__ == '__main__':

    lines = read_file(sys.argv[1])
    dict_line = read_file(sys.argv[2])

    mydict = create_dictionary(dict_line)

    file_name = sys.argv[1] + '.univ'
    write_with_uni_tag(file_name ,lines, mydict)
    print("Original file " + sys.argv[1]  + "  with universal tags written in " + file_name)
