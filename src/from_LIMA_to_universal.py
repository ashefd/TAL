import nltk
import sys
# Tsha et Alya


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
    f1 = open(file_name1, "r") 
    f2 = open(file_name2, "r") 
    f3 = open(file_name3, "r") 

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
        Liste a 1 dimension contenant 'une_categorie_grammaticale', 'la_categorie_grammaticale_dans_un_autre_type'
        exemple :
            ["SCONJ", "CC", "SENT", ".", "COMMA", ","]

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
    for i in range(0,len(lines),2): # un mot sur deux est un mot. 
        # i*n       :  une categorie grammaticale
        # **n + 1   :  la categorie grammaticale universelle associee
        mydict[lines[i]] = lines[i+1]
    return mydict




def createDirectDictionary(dictionary_LIMA_PTB, dictionary_PTB_universal):
    """Creation d'un dictionnaire à partir de deux dictionnaires
    Cela nous permettra de passer de LIMA vers universal plutot que de lima vers ptb puis ptb vers universal

    Parameters
    ----------
    dictionary_LIMA_PTB : dictionary
        key : categorie grammaticale en LIMA
        value : categorie grammaticale en PTB
        dictionnaire (key,value)
        exemple : 
            SCONJ CC
            SENT .
            COMMA ,
    dictionary_PTB_universal : dictionary 
        key : categorie grammaticale en PTB
        value : categorie grammaticale en universal
        dictionnaire (key,value)
        exemple :
            CC CONJ
            . .
            , .

    Returns
    -------
    direct : dictionary
        key : categorie grammaticale en LIMA
        value : categorie grammaticale en universal
        dictionnaire (key,value)
        exemple :
            SCONJ CONJ
            SENT .
            COMMA .
    """
    direct = {} 

    # on parcourt les cles du dictionnaire LIMA_PTB
    for key in dictionary_LIMA_PTB : 
        value = dictionary_LIMA_PTB[key] # on obtient la valeur associee de key

        if(value in dictionary_PTB_universal): # si la value (en ptb) existe dans le dictionnaire PTB -> universal
            #print(key + " " + value + "\n")
            direct[key] = dictionary_PTB_universal[value] # on ajoute dans le dictionnaire final la traduction de key (en LIMA) vers sa categorie grammaticale en universal
    return direct


def write_with_uni_tag(lines, file_name_out, dictionary_LIMA_universal):
    """Reecriture des categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Cette fonction permet de remplacer les categories grammaticales de deux fichiers avec des categories grammaticales universelles.

    Parameters
    ----------
    lines : array of string
        Lignes du fichier a reecrire
        Pierre Vinken	PROPN
        ,	COMMA
        61 years old	ADJ
        ,	COMMA

    file_name_out : string
        nom du fichier final

    dictionary_LIMA_universal : dictionary 
        key : categorie grammaticale en LIMA
        value : categorie grammaticale en universal
        dictionnaire (key,value)
        exemple :
            SCONJ CONJ
            SENT .
            COMMA .

    Returns
    -------
    None


    Content of file_name_out :
    exemple :
        Pierre Vinken	NOUN
        ,	.
        61 years old	ADJ
        ,	.
    """
    f = open(file_name_out, "w") # fichier resultat

    for i in range(0,len(lines)): # on parcourt les lignes du fichier file_name_out
        x = lines[i].split('\t')
        if(len(x) >= 2): # si ce n'est pas un retour chariot

            # on ajoute dans le fichier final :
            # le mot initial (contenu dans la premiere colonne) \t sa categorie grammaticale en universal
            f.write("\t".join((x[0], dictionary_LIMA_universal[x[1]]))) 
        f.write("\n")
    f.close()



if __name__ == '__main__':
    # sys.argv[1] : lima file
    # sys.argv[2] : dictionary from lima to PTB
    # sys.argv[3] : dictionary from PTB to universal

    # on obtient les lignes de chaque fichier
    lines1, lines2, lines3 = read_file(sys.argv[1], sys.argv[2], sys.argv[3])

    # on cree le dictionnaire de LIMA -> PTB
    dictionary_LIMA_PTB = create_dictionary(lines2)
    #print(dictionary_LIMA_PTB)

    # on cree le dictionnaire de PTB -> universal
    dictionary_PTB_universal = create_dictionary(lines3)
    #print(dictionary_PTB_universal)

    # on cree le dictionnaire de LIMA -> universal
    dictionary_LIMA_universal = createDirectDictionary(dictionary_LIMA_PTB, dictionary_PTB_universal)
    #print(dictionary_LIMA_universal)

    # nom du fichier final
    lima_out = "out/" + sys.argv[1][8:-5] + ".univ"+sys.argv[1][-5:]

    # on reecrit le fichier avec ses tag en unversal dans le fichier "lima_out"
    write_with_uni_tag(lines1, lima_out, dictionary_LIMA_universal)
    print("Reference Lima with universal tags written in " + lima_out)