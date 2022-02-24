import sys
# Tsha et Alya


def extractSentences(file_name):
    line = ''
    line_without_compounds = ''
    ref_without_compounds = ''

    file = open(file_name, 'r')

    lines = file.read().splitlines()

    for l in lines:
        x =  l.split()
        if(len(x) == 0):
            line += '\n'
            line_without_compounds += '\n'
            ref_without_compounds += '\n'
        # ajouter un elif(len(x) > 2): ajoute pas ds le talzau a ecrire 
        else:

            words = x[0:-1]
            line += ' '.join(words) + ' '
            if(len(x) == 2):
                line_without_compounds += ' '.join(words) + ' '
                ref_without_compounds += '\t'.join(x) + '\n'

    return line, line_without_compounds, ref_without_compounds

def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.write(lines)

if __name__ == '__main__':
    #1er arg : ref lima
    #2eme : nom du file out pour le corpus (complet)

    lines, line_without_compounds, ref_without_compounds = extractSentences(sys.argv[1])
    writeLines(lines, sys.argv[2])
    print("Corpus written in "+ sys.argv[2])

    corpus_without_comp_out = sys.argv[2][:-4] + ".wc"+sys.argv[2][-4:]
    ref_without_comp_out = "out/" + sys.argv[1][8:-5] + ".wc" + sys.argv[1][-5:]

    writeLines(line_without_compounds, corpus_without_comp_out)
    print("Corpus without compounds written in " + corpus_without_comp_out)
    writeLines(ref_without_compounds, ref_without_comp_out)
    print("Ref lima without compounds written in " + ref_without_comp_out)
