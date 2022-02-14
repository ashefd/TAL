import sys

def extractSentences(file_name):
    line = ''
    file = open(file_name, 'r')

    lines = file.read().splitlines()

    for l in lines:
        x =  l.split()
        if(len(x) == 0):
            line += '\n'
        else:
            words = x[0:-1]
            line += ' '.join(words) + ' '
    return line

def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.write(lines)

if __name__ == '__main__':
    lines = extractSentences(sys.argv[1])
    writeLines(lines, sys.argv[2])
