import nltk
import sys
import re
from nltk import pos_tag
from nltk import RegexpParser

def convertTabToUnderscore(filename):
    f = open(filename, "r")
    lines = f.read().splitlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\t', '_')
    return lines


if __name__ == '__main__':
    lines = convertTabToUnderscore(sys.argv[1])
    f = open(sys.argv[2], 'w')
    f.write(' '.join(lines))