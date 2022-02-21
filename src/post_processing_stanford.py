import sys

def two_columns_without_underscore(file_name, file_name_out):

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
            if(word_cat in dict.keys()):
                out.write(dict[word_cat] + '\n')
            else:
                out.write(word_cat.replace('_', '\t') + '\n')
        out.write('\n')

    out.close()

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie
    file_name_out = "out/" + sys.argv[1][8:]

    lines = two_columns_without_underscore(sys.argv[1], file_name_out)
    print("Stanford file with post-processing written in " +file_name_out)