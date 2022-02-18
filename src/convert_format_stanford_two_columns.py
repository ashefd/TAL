import sys

def two_columns_without_underscore(file_name, file_name_out):

    f = open(file_name, 'r')
    out = open(file_name_out, 'w')
    lines = f.read().splitlines()
    for line in lines:
        for word_cat in line.split():
            out.write(word_cat.replace('_', '\t') + '\n')
        out.write('\n')

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie
    lines = two_columns_without_underscore(sys.argv[1], "xxxx.txt")

    # python convert_format_stanford_two_columns.py pos_text.txt.pos.stanford