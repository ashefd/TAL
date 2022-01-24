import nltk
import sys

def read_file(file_name1, file_name2, file_name3):
    f1 = open(file_name1, "r") # fichier a remplacer
    f2 = open(file_name2, "r") # fichier a remplacer
    f3 = open(file_name3, "r") # post-tag

    lines1 = f1.read().split()
    lines2 = f2.read().split()
    lines3 = f3.read().split()

    f1.close()
    f2.close()
    f3.close()

    return lines1, lines2, lines3


def create_dictionary(lines):
    mydict = {}
    for i in range(0,len(lines),2):
        mydict[lines[i]] = lines[i+1]
    return mydict


def write_with_uni_tag(file_name1, file_name2, lines1, lines2, mydict):
    f1 = open(file_name1, "w") # fichier a remplacer
    f2 = open(file_name2, "w") # fichier a remplacer

    for i in range(0,len(lines1),2):
        f1.write("\t".join((lines1[i], mydict[lines1[i+1]])))
        f1.write("\n")

        f2.write("\t".join((lines2[i], mydict[lines2[i+1]])))
        f2.write("\n")

    f1.close()
    f2.close()



if __name__ == '__main__':

    lines1, lines2, lines3 = read_file(sys.argv[1], sys.argv[2], sys.argv[3])

    mydict = create_dictionary(lines3)

    write_with_uni_tag('wsj_0010_sample.txt.pos.univ.nltk', 'wsj_0010_sample.pos.txt.pos.univ.ref', lines1, lines2, mydict)
    