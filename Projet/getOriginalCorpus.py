import sys

def extractSentences(file_name):
    line = ''
    line_without_compounds = ''

    file = open(file_name, 'r')

    lines = file.read().splitlines()

    for l in lines:
        x =  l.split()
        if(len(x) == 0):
            line += '\n'
            line_without_compounds += '\n'
        # ajouter un elif(len(x) > 2): ajoute pas ds le talzau a ecrire 
        else:
            words = x[0:-1]
            line += ' '.join(words) + ' '
            if(len(x) == 2):
                line_without_compounds += ' '.join(words) + ' '

    return line, line_without_compounds

def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.write(lines)

if __name__ == '__main__':
    lines, line_without_compounds = extractSentences(sys.argv[1])
    writeLines(lines, sys.argv[2])
    without_compound = "out/" + sys.argv[1][:-5] + ".wc"+sys.argv[1][-5:]
    print(without_compound)
    writeLines(line_without_compounds, without_compound)

