import sys
# Tsha et Alya


def extractSentences(file_name):
    """

    Cette fonction permet de recomposer un corpus complet à partir d'un fichier reference tagué
    Et de retirer les mots composer du fichier tagué et du corpus

    Parameters
    ----------
    file_name : string
        Nom du fichier de reference qui contient les mots tagués

    Returns
    -------
    line: string
    chaine de caractère du corpus complet recomposé

    line_without_compounds: string
    chaine de caractère du corpus sans mots composés

    ref_without_compounds: string
    chaine de caractère du fichier de reference tagué sans les mots composés

    """
    line = ''
    line_without_compounds = ''
    ref_without_compounds = ''

    file = open(file_name, 'r')

    lines = file.read().splitlines()

    for l in lines:
        x =  l.split()
        if(len(x) == 0): #ligne vide
            line += '\n'
            line_without_compounds += '\n'
            ref_without_compounds += '\n'

        else:

            words = x[0:-1] #on ne recupère que les mots sans le tag (dernier elem)
            line += ' '.join(words) + ' '
            if(len(x) == 2):
                line_without_compounds += ' '.join(words) + ' '  # s'il y a plus de deux mots on ne les ecrit pas dans
                #les chaines sans compound (mots composés)
                ref_without_compounds += '\t'.join(x) + '\n'

    return line, line_without_compounds, ref_without_compounds

def writeLines(lines, file_out):
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
    file = open(file_out, 'w')
    file.write(lines)

if __name__ == '__main__':
    #1er arg : ref lima
    #2eme : nom du file out pour le corpus (complet)

    lines, line_without_compounds, ref_without_compounds = extractSentences(sys.argv[1])
    writeLines(lines, sys.argv[2])
    print("Corpus written in "+ sys.argv[2])

    corpus_without_comp_out = sys.argv[2][:-4] + ".wc"+sys.argv[2][-4:]
    ref_without_comp_out = "out/" + sys.argv[1][8:-5] + ".wc" + sys.argv[1][-5:]

    writeLines(line_without_compounds, corpus_without_comp_out)
    print("Corpus without compounds written in " + corpus_without_comp_out)
    writeLines(ref_without_compounds, ref_without_comp_out)
    print("Ref lima without compounds written in " + ref_without_comp_out)
