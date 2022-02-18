import sys

def two_columns_without_underscore(file_name):

    f = open(file_name, 'r')
    lines = f.read().splitlines()
    f.close()
    out = open(file_name, 'w')

    for line in lines:
        for word_cat in line.split():
            out.write(word_cat.replace('_', '\t') + '\n')
        out.write('\n')

    out.close()

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie
    lines = two_columns_without_underscore(sys.argv[1])