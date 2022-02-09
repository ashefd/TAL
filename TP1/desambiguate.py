import nltk
import sys

from nltk import pos_tag
from nltk import word_tokenize

def tokenize_tag(file_name_in):
    """Tokeniser un fichier txt

    Cette fonction permet de lire un fichier texte pour ensuite obtenir dans une liste
    les mots qu'il contient.

    Parameters
    ----------
    file_name_in : string
        Nom du fichier a tokeniser
  
    Returns
    -------
    text
        Liste des mots qui composent le fichier file_name_in
    """
    f = open(file_name_in, "r")

    text = []

    lines = f.read().splitlines()
    for line in lines:
        listing = nltk.word_tokenize(line)

        tag = nltk.pos_tag(listing)
        for t in tag:
            text.append(t)

    return text

def write_text_in_file(tokenized_tagged_text,  file_name_out):
    """Ecriture d'une liste de mots dans un fichier.

    Cette fonction permet d'écrire le contenu d'une liste dans un fichier pour obtenir 
    dans une premiere colonne un mot et dans la deuxieme colonne sa categorie grammaticale


    Parameters
    ----------
    tokenized_tagged_text : string
        La liste de mots et leur categorie grammaticale (le tout a la suite)
    file_name_out : string
        Le nom du fichier contenant des mots et leur categorie grammaticale

    Returns
    -------
    tokenized_tagged_text
        La liste de mots et leur categorie grammaticale 
    """
    s = open(file_name_out, "w")
    for i in tokenized_tagged_text:
        s.write('\t'.join(i))
        s.write("\n")

    s.close()
    return tokenized_tagged_text

if __name__ == '__main__':
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

    tokenized_tagged_text = tokenize_tag(sys.argv[1])
    print(tokenized_tagged_text)

    write_text_in_file(tokenized_tagged_text, sys.argv[2])  # Deuxieme fichier donne
    print("tagged written in file " + sys.argv[2])


