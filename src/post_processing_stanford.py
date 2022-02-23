import sys

# Tsha 
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

def two_columns_without_LRB_RRB(file_name, file_name_out):

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
        if(len(word_cat) > 0 and word_cat[0] in dict.keys()):
            
            out.write(dict[word_cat[0]] + '\t' +  word_cat[1])
        elif(len(word_cat) > 0):
            out.write('\t'.join(word_cat))
        out.write('\n')
        
    out.close()

if __name__ == '__main__':
    #sys.argv[1] # le fichier stanford a convertir pour qu'il y ait :
    # mot\tcategorie


    dict = {
        'pos_tag': '_',
        'ne': '/',
    }
    if(sys.argv[2] == 'pos_tag') :
        file_name_out = "out/" + sys.argv[1][8:]
        lines = two_columns_without_underscore(sys.argv[1], file_name_out)
        print("Stanford file with post-processing written in " +file_name_out)

    elif(sys.argv[2] == 'ne'):
        file_name_out = sys.argv[1] + 'c'
        lines = two_columns_without_LRB_RRB(sys.argv[1], file_name_out)
        print("Stanford file with post-processing written in " +file_name_out)