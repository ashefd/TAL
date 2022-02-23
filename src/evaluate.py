import sys
# Tsha et Alya


def number_nonempty_lines(array):
    empty = 0
    for line in array:
        if (line.replace('\n', '') == '' or line == ''):
            empty += 1
    return len(array) -empty

def harmonize_by_concatenation(file_name_ref, file_to_change):
    """
    Le but de la fonction est d'harmoniser le fichier file_to_change en fonction de file_name_ref
    et de calculer les différentes métriques d'évaluation : TP, FP, FN,
    """
    ref_file = open(file_name_ref, 'r')
    to_change_file = open(file_to_change, 'r')

    lines_ref_file = ref_file.read().splitlines()
    lines_to_change_file = to_change_file.read().splitlines()

    ref_file.close()
    to_change_file.close()

    final_ref = []
    final_to_change_file = []

    line_index_ref = 0
    line_index_change = 0

    window = 3
    found = False

    nb_FN = 0
    nb_TP = number_nonempty_lines(lines_ref_file)
    nb_FP = 0
    nCandidateWords = number_nonempty_lines(lines_to_change_file)
    nTotalCorrectWords = 0



    while ((line_index_ref < len(lines_ref_file)) and line_index_change < len(lines_to_change_file)) :

        words_ref = lines_ref_file[line_index_ref].split('\t')
        words_to_change_file = lines_to_change_file[line_index_change].split('\t')

        # on trouve bien le même mot
        if(words_ref[0] == words_to_change_file[0]):

            final_ref.append(lines_ref_file[line_index_ref])
            final_to_change_file.append(lines_to_change_file[line_index_change])
            line_index_ref += 1 
            line_index_change += 1

            #si ce n'est pas un saut de ligne :
            if(len(words_ref) > 1 and len(words_to_change_file) > 1):
                nTotalCorrectWords += 1  # le mot est juste et bien tokenizé

                if(words_ref[1] != words_to_change_file[1]):# si le mot n'a pas la bonne etiquette
                    nb_FP += 1

        #Les mots n'ont pas été tokenisés de la bonne manière :
        else:
            if(line_index_change+ 1 < len(lines_to_change_file) and line_index_ref + 1 < len(lines_ref_file)):
                words2_ref = lines_ref_file[line_index_ref+1].split('\t')
                words2_to_change_file = lines_to_change_file[line_index_change+1].split('\t')

            #On regarde la ligne d'en dessous pour le fichier à évaluer en concaténant
            if(words_ref[0] == words_to_change_file[0] + words2_to_change_file[0]):
                line_index_ref += 1 
                line_index_change += 2
                nb_FN += 1
                print(words_ref[0] + " VS " + words_to_change_file[0] +"    "+ words2_to_change_file[0])

            #On regarde la ligne d'en dessous pour la référence en concaténant
            elif(words_ref[0] + words2_ref[0] == words_to_change_file[0]):
                line_index_ref += 2
                line_index_change += 1
                nb_FN += 2
                print(words_ref[0] + " " + words2_ref[0] + " VS " + words_to_change_file[0] )

            else :
                #Si la concaténation a échoué, on itère sur un certains nombre de mots pour voir si
                #le mot de la référence s'y trouve
                found = False
                for i in range(window):
                    if(line_index_change + i < len(lines_to_change_file)):
                        words_to_change_file_i = lines_to_change_file[line_index_change + i].split('\t')
                        if(words_ref[0] == words_to_change_file_i[0]):
                            #On retrouve bien le mot de la référence sur le fichier évalué
                            found = True
                            line_index_change += i
                            final_ref.append(lines_ref_file[line_index_ref])
                            final_to_change_file.append(lines_to_change_file[line_index_change])
                            nTotalCorrectWords+=1
                            break

                #Affichage des lignes problématiques
                print(line_index_ref)
                print(line_index_change)
                print(words_ref[0])
                print(words2_ref[0])
                print(words_to_change_file[0])
                print(words2_to_change_file[0])
                print('\n')

                if(not found):
                    #Le fichier n'a pas été trouvé donc on passe à la ligne suivante et on retire ce mot
                    #non étiqueté
                    nb_FN += 1
                line_index_ref += 1 
                line_index_change += 1


    return final_ref, final_to_change_file, nb_TP, nb_FN, nb_FP, nCandidateWords, nTotalCorrectWords


def evaluate(nb_TP, nb_FN, nb_FP, nCandidateWords, nTotalCorrectWords):
    """
    nb_TP : Le nombre de mot étiquetté correctement par les experts
    nb_FN : Le nombre de mot qui n'est étiquetté par aucune étiquette
    nb_FP : Le nombre de mot qui n'a pas été étiquetté correctement
    TN : Les occurences ont été catégorisées comme des instances normales

    Précision : Le ration entre les étiquettes correctement étiquettés et l'ensemble des mots étiquetés 
    Précision = nb_TP / (nb_TP + nb_FP)

    Rappel: Le ratio entre tous les exemples (mots) correctement étiquettés avec tous les exemples (mots) étiquettés par les experts
    Rappel = nb_TP / (nb_TP + nb_FN)
    """

    """"
       word_precision = float(nTotalCorrectWords) / float(nCandidateWords)
       word_recall = float(nTotalCorrectWords) / float(nReferenceWords)
       tag_precision = float(nTotalCorrectTags) / float(nCandidateWords)
       tag_recall = float(nTotalCorrectTags) / float(nReferenceWords)
       word_fmeasure = (2*word_precision*word_recall)/(word_precision+word_recall)
       if tag_precision+tag_recall==0:
             tag_fmeasure = 0.0
        else:
            tag_fmeasure = (2*tag_precision*tag_recall)/(tag_precision+tag_recall)
      """

    tag_recall = nb_TP / (nb_TP + nb_FN)
    tag_precision = nb_TP / (nb_TP + nb_FP)
    if tag_precision + tag_recall == 0:
        tag_fmeasure = 0.0
    else:
        tag_fmeasure = (2 * tag_precision * tag_recall) / (tag_precision + tag_recall)

    word_precision = float(nTotalCorrectWords) / float( nCandidateWords)
    word_recall = float(nTotalCorrectWords) / float(nb_TP)
    word_fmeasure = (2 * word_precision * word_recall) / (word_precision + word_recall)

    return tag_recall, tag_precision, tag_fmeasure, word_precision,  word_recall ,  word_fmeasure


def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.writelines("%s\n" % l for l in lines)


if __name__ == '__main__':
    # sys.argv[1] : le fichier qui ressemble à la reference (en terme de nombre de mots) / La reference
    # sys.argv[2] : le fichier que l'on va transformer au fur et a mesure

    final_ref, final_to_change_file, nb_TP, nb_FN, nb_FP, nCandidateWords, nTotalCorrectWords = harmonize_by_concatenation(sys.argv[1], sys.argv[2])

    print("Nombre de mot total pour la référence : " , nb_TP)
    print("Nombre de mot total pour le candidat : " , nCandidateWords)
    print("Nombre de mots mal étiquettés : " , nb_FP)
    print("Nombre de mots non étiquettés : " , nb_FN)
    print("Nombre de mots bien tokenizés: " , nTotalCorrectWords)

    # Pour evaluer
    tag_recall, tag_precision, tag_fmeasure, word_precision,  word_recall ,  word_fmeasure = evaluate(nb_TP, nb_FN, nb_FP, nCandidateWords, nTotalCorrectWords)

    print("Word precision:", word_precision)
    print("Word recall:", word_recall)

    print("Tag precision:", tag_precision)
    print("Tag recall:", tag_recall)

    print("Word F-measure:", word_fmeasure)
    print("Tag F-measure:", tag_fmeasure)


    # Nommage des fichiers
    final_ref_name_file = sys.argv[1][:-5] + ".harmonised." + sys.argv[2][-4:] + sys.argv[1][-5:]
    final_to_change_name_file = sys.argv[2] + ".harmonised"

    #ecriture des fichiers harmonisés
    writeLines(final_ref, final_ref_name_file)
    writeLines(final_to_change_file, final_to_change_name_file)

    print("Reference harmonized with candidate file " + sys.argv[2] + " written in " +  final_ref_name_file )
    print("Candidate file " + sys.argv[2] + " harmonized with reference written in " + final_to_change_name_file)



