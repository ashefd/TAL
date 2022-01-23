import nltk
import sys

if __name__ == '__main__':
    f1 = open(sys.argv[1], "r") # Premier fichier donne
    f2 = open(sys.argv[2], "r") # ref
    lines1 = f1.read().split()
    lines2 = f2.read().split()
    f1.close()
    f2.close()

    f1 = open(sys.argv[1], "w") # Premier fichier donne
    f2 = open(sys.argv[2], "w") # ref

    text1 = []
    text2 = []

    for i in range(0,len(lines1),2):
        if(lines2[i] != lines1[i]):
            print(lines2[i])
            print(lines1[i])
        else : 
            text1.append((lines1[i], lines1[i+1]))
            text2.append((lines2[i], lines2[i+1]))
    
    for i in range(len(text1)):
        f1.write("\t".join(text1[i]))
        f1.write("\n")

        f2.write("\t".join(text2[i]))
        f2.write("\n")


    f1.close()
    f2.close()
