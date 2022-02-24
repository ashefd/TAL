import nltk
import sys
# Tsha et Alya

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


def write_with_uni_tag(file_name, lines, mydict):
    """
    From
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

    To : 
    ,	.
    ,	.
    will	VERB
    join	VERB
    the	DET
    board	NOUN
    as	ADP
    a	DET
    nonexecutive	ADJ
    director	NOUN
    .	.
    """
    f = open(file_name, "w") # fichier a remplacer

    print(mydict)
    for line in lines:
        print((line))
        if(len(line) != 0):
            words = line.split('\t')

            f.write("\t".join((words[0], mydict[words[1]])))

        f.write("\n")

    f.close()



if __name__ == '__main__':

    lines = read_file(sys.argv[1])
    dict_line = read_file(sys.argv[2])

    mydict = create_dictionary(dict_line)

    file_name = sys.argv[1] + '.univ'
    write_with_uni_tag(file_name ,lines, mydict)
    print("Original file " + sys.argv[1]  + "  with universal tags written in " + file_name)
