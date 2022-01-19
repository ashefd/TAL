import nltk
import sys

if __name__ == '__main__':
    mydict = {}

    f1 = open(sys.argv[1], "r") # fichier a remplacer
    f2 = open(sys.argv[2], "r") # fichier a remplacer
    f3 = open(sys.argv[3], "r") # post-tag

    lines1 = f1.read().split()
    lines2 = f2.read().split()
    lines3 = f3.read().split()

    f1.close()
    f2.close()

    for i in range(0,len(lines3),2):
        mydict[lines3[i]] = lines3[i+1]
    print(mydict)

    f1 = open(sys.argv[1]+'.universal.nltk', "w") # fichier a remplacer
    f2 = open(sys.argv[2]+'.universal.ref', "w") # fichier a remplacer

    for i in range(0,len(lines1),2):
        f1.write("\t".join((lines1[i], mydict[lines1[i+1]])))
        f1.write("\n")

        f2.write("\t".join((lines2[i], mydict[lines2[i+1]])))
        f2.write("\n")

    f1.close()
    f2.close()

    f3.close()