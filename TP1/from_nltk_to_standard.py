import nltk
import sys


if __name__ == '__main__':

    f = open(sys.argv[1], 'r') # wsj_0010_sample.txt.ne.nltk : le fichier a convertir
    file = open(sys.argv[2], 'w') # res.txt : fichier resultat
    lignes = f.read()
