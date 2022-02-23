import nltk
import sys
# Alya
def read_file(file_name):
    f = open(file_name, "r") # fichier a remplacer

    lines = f.read().splitlines()
    f.close()
    return lines


def create_dictionary(lines):
    mydict = {}
    for line in lines:
        words = line.split()
        mydict[words[0]] = words[1]
    return mydict

def convert_CoNLL(lines, mydict):

    begin = False
    last_etiquette = ''
    lines_CoNLL = []
    for line in lines:
        print((line))
        if(len(line) != 0 and line.replace('\n', '') != ''):
            words = line.split('\t')
            if(words[1] != "O"):
                if(words[1] in mydict.keys() and last_etiquette != words[1]):
                    etiquette = "B-"+ mydict[words[1]]

                else:

                    etiquette = "I-" + mydict[words[1]]
                last_etiquette  =words[1]
            else:
                etiquette = "O"
                last_etiquette =  "O"
            lines_CoNLL.append(words[0] + '\t' + etiquette +"\n")

    return lines_CoNLL

def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.writelines(lines)

if __name__ == '__main__':

    lines = read_file(sys.argv[1])
    dict_lines = read_file(sys.argv[2])

    coNLL_dict = create_dictionary(dict_lines)
    lines_CoNLL = convert_CoNLL(lines, coNLL_dict)

    file_name = sys.argv[1] + '.conll'
    writeLines(lines_CoNLL,   file_name )

    print("Original file " + sys.argv[1]  + "  with conll tags written in " + file_name)
