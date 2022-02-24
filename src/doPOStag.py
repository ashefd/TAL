import nltk
import sys
from nltk import pos_tag
from nltk import RegexpParser
# Tsha 
def nltk_parse(text_file_name):
    """

    Cette fonction permet d'appliquer le pos tagging de nltk sur un fichier de mots

    Parameters
    ----------
    text_file_name : string
        Nom du fichier qui contient le texte pour lequel on souhaite appliquer les tags

    Returns
    -------
    line_tag : list of tuples
        Liste de tuples (mot, tag) qui correpondent à chaque mot avec son tag associé
    """
    text  = open(text_file_name, 'r')
    print(text)
    line_tag = []
    lines = text.read().splitlines()
    for line in lines:
        line_tag.append(pos_tag(line.split()))
    print(line_tag)


    return line_tag

def write_tags_in_file(list_of_tags, file_name):
    """
    Cette fonction permet d'ecriredans un fichier (avec le bon format) les elements d'une liste dans un fichier

    Parameters
    ----------
    list_of_tags: list of tuples
       Liste de tuples (mot, tag) qui correpondent à chaque mot avec son tag associé
    file_name : string
        Nom du fichier dans lequel on souhaite ecrire
        
    Returns
    -------
    void
    """
    f3 = open(file_name, "w")
    for line_tag in list_of_tags:
        for i in range(len(line_tag)):
            print(str(i) + " : " + str(line_tag[i]))
            f3.write('\t'.join(line_tag[i]))
            f3.write("\n")
        f3.write('\n')
    f3.close()

if __name__ == '__main__':

    list_of_tags = nltk_parse(sys.argv[1])
    print(list_of_tags)
    write_tags_in_file(list_of_tags, "out/pos_test.txt.pos.nltk")

    print("File tagged by nltk written in " + "out/pos_test.txt.pos.nltk")