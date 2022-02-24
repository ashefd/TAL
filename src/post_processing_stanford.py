import sys

# Tsha 
def two_columns_without_underscore(file_name, file_name_out):
    """Reecriture d'un fichier en changeant les underscore en /t et en creant les deux colonnes

    Parameters
    ----------
    file_name : string
        Nom du fichier a modfier. Format :
        ,_, ,_, will_MD join_VB the_DT board_NN as_IN a_DT nonexecutive_JJ director_NN ._.

    file_name_out : string
        Nom du fichier a retourner

    Returns
    -------
    None 

    content of file_name_out. Format :
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

    """
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    out = open(file_name_out, 'w')

    dict = {
        '\'\'_\'\'': '\"\t\"',
        '-LCB-_-LRB-': '{\t(',
        '-RCB-_-RRB-': '}\t)',
        '-LRB-_-LRB-': '(\t(',
        '-RRB-_-RRB-': ')\t)',
    }

    for line in lines:
        for word_cat in line.split():
            if(word_cat in dict.keys()): # quand on rencontre une ligne dans laquelle on trouve un LCB, RCB, LRB ou RRB
                out.write(dict[word_cat] + '\n') # on remplace ca par le bon caractere correspondant et son tag
            else:
                out.write(word_cat.replace('_', '\t') + '\n') # on reecrit sans le underscore
        out.write('\n')

    out.close()

def two_columns_without_slash(file_name, file_name_out):
    """Reecriture d'un fichier en changeant les slash (/) en /t et en creant les deux colonnes

    Parameters
    ----------
    file_name : string
        Nom du fichier a modfier. Format :
        Mary/PERSON Barra/PERSON appointed/O as/O General/ORGANIZATION Motors/ORGANIZATION chief/O December/O 10/O ,/O 2013/O The/O United/LOCATION States/LOCATION 's/O largest/O car/O manufacturer/O General/ORGANIZATION Motors/ORGANIZATION today/O named/O Mary/PERSON Barra/PERSON as/O its/O new/O chief/O executive/O ./O 
        

    file_name_out : string
        Nom du fichier a retourner

    Returns
    -------
    None 

    content of file_name_out. Format :
    Mary	PERSON
    Barra	PERSON
    appointed	O
    as	O
    General	ORGANIZATION
    Motors	ORGANIZATION
    chief	O
    December	O
    10	O
    ,	O
    2013	O
    The	O
    United	LOCATION
    States	LOCATION
    's	O
    largest	O
    car	O
    manufacturer	O
    General	ORGANIZATION
    Motors	ORGANIZATION
    today	O
    named	O
    Mary	PERSON
    Barra	PERSON
    as	O
    its	O
    new	O
    chief	O
    executive	O
    .	O
    """
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    out = open(file_name_out, 'w')

    for line in lines: # pour chaque ligne du fichier
        for word_chunk in line.split(): 
                out.write(word_chunk.replace('/', '\t') + '\n') # on remplace les / par une tabulation
        out.write('\n')

    out.close()

def two_columns_without_LRB_RRB(file_name, file_name_out):
    """Reecriture d'un fichier en changeant les LRB, RRB, LCB et RCB en leur caractere asscoié
    LRB = (
    RCB = )
    LRB = (
    RRB = )

    Parameters
    ----------
    file_name : string
        Nom du fichier a modfier. Format :
        Mary/PERSON Barra/PERSON appointed/O as/O General/ORGANIZATION Motors/ORGANIZATION chief/O December/O 10/O ,/O 2013/O The/O United/LOCATION States/LOCATION 's/O largest/O car/O manufacturer/O General/ORGANIZATION Motors/ORGANIZATION today/O named/O Mary/PERSON Barra/PERSON as/O its/O new/O chief/O executive/O ./O 
        

    file_name_out : string
        Nom du fichier a retourner

    Returns
    -------
    None 

    Exemple :
    -------
    // Before //
    United	ORGANIZATION
    Auto	ORGANIZATION
    Workers	ORGANIZATION
    -LRB-	O
    UAW	ORGANIZATION
    -RRB-	O
    union	O
    agree	O

    // After //
    United	ORGANIZATION
    Auto	ORGANIZATION
    Workers	ORGANIZATION
    (	O
    UAW	ORGANIZATION
    )	O
    union	O
    agree	O

    """
    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    out = open(file_name_out, 'w')

    dict = {
        '\'\'_\'\'': '\"\t\"',
        '-LCB-' : '(',
        '-RCB-' : ')',
        '-LRB-' : '(',
        '-RRB-' : ')',
    }

    for line in lines:
        word_cat = line.split()
        if(len(word_cat) > 0 and word_cat[0] in dict.keys()): # si ce n'est pas un saut de ligne et que le mot (surement une parenthese ou une accolade)
            
            out.write(dict[word_cat[0]] + '\t' +  word_cat[1])  # on reecrit le token par le caractere associe. Par exemple, les -LRB- seront remplaces par un (
        elif(len(word_cat) > 0):
            out.write('\t'.join(word_cat)) # sinon, on reecrit directement la ligne en ajoutant une tabulation
        out.write('\n')
        
    out.close()

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie


    dict = {
        'pos_tag': '_',
        'ne': '/',
    }
    if(sys.argv[2] == 'pos_tag') : # pour faire du post processing avec le post_tag
        file_name_out = "out/" + sys.argv[1][8:]
        lines = two_columns_without_underscore(sys.argv[1], file_name_out)
        print("Stanford file with post-processing written in " +file_name_out)

    elif(sys.argv[2] == 'ne'): # pour faire du post processing avec le ne_chunk
        file_name_out = sys.argv[1] + 'c'
        lines = two_columns_without_LRB_RRB(sys.argv[1], file_name_out)
        print("Stanford file with post-processing written in " +file_name_out)

    elif(sys.argv[2] == 'slash'): # pour faire du post processing pour enlever les /
        file_name_out = sys.argv[1][:-2]
        lines = two_columns_without_slash(sys.argv[1], file_name_out)
        print("Stanford file with post-processing written in " +file_name_out)
