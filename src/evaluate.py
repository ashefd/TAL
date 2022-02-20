import sys

def harmonize_by_concatenation(file_name_ref, file_to_change):
    """
    Le but de la fonction est d'harmoniser le fichier file_to_change en fonction de file_name_ref
    """
    ref_file = open(file_name_ref, 'r')
    to_change_file = open(file_to_change, 'r')

    lines_ref_file = ref_file.read().splitlines()
    lines_to_change_file = to_change_file.read().splitlines()

    ref_file.close()
    to_change_file.close()

    #min_range = min(len(lines_ref_file), len(lines_to_change_file))
    window = 3

    final_ref = []
    final_to_change_file = []

    nb_FN = 0
    found = False

    # for line_index in range(min_range):
    line_index_ref = 0
    line_index_change = 0
    while ((line_index_ref < len(lines_ref_file)) and line_index_change < len(lines_to_change_file)) :
        words_ref = lines_ref_file[line_index_ref].split('\t')
        words_to_change_file = lines_to_change_file[line_index_change].split('\t')

        # on trouve 
        if(words_ref[0] == words_to_change_file[0]):
            final_ref.append(lines_ref_file[line_index_ref])
            final_to_change_file.append(lines_to_change_file[line_index_change])
            line_index_ref += 1 
            line_index_change += 1  
        else:
            words2_ref = lines_ref_file[line_index_ref+1].split('\t')
            words2_to_change_file = lines_to_change_file[line_index_change+1].split('\t')

            if(words_ref[0] == words_to_change_file[0] + words2_to_change_file[0]):
                line_index_ref += 1 
                line_index_change += 2
                nb_FN += 1

            elif(words_ref[0] + words2_ref[0] == words_to_change_file[0]):
                line_index_ref += 2 
                line_index_change += 1
                nb_FN += 1

            else : 
                found = False
                for i in range(window):
                    words_to_change_file_i = lines_to_change_file[line_index_change + i].split('\t')
                    if(words_ref[0] == words_to_change_file_i[0]):
                        found = True
                        line_index_change += i
                        final_ref.append(lines_ref_file[line_index_ref])
                        final_to_change_file.append(lines_to_change_file[line_index_change])

                print(line_index_ref)
                print(line_index_change)
                print(words_ref[0])
                print(words2_ref[0])
                print(words_to_change_file[0])
                print(words2_to_change_file[0])
                print('\n')
                #break
                if(not found):
                    nb_FN += 1
                line_index_ref += 1 
                line_index_change += 1
                
                #print("aucun des cas")

    return final_ref, final_to_change_file, len(lines_ref_file), nb_FN

def harmonize_by_jump(file_name_ref, file_to_change):
    """
    Le but de la fonction est d'harmoniser le fichier file_to_change en fonction de file_name_ref
    """
    ref_file = open(file_name_ref, 'r')
    to_change_file = open(file_to_change, 'r')

    lines_ref_file = ref_file.read().splitlines()
    lines_to_change_file = to_change_file.read().splitlines()

    ref_file.close()
    to_change_file.close()

    window = 3 # nombre de mots que l'on verifie en dessous s'il y a une erreur

    final_ref = []
    final_to_change_file = []

    line_index_ref = 0
    line_index_change = 0
    while ((line_index_ref < len(lines_ref_file)-1) and line_index_change < len(lines_to_change_file)-1) :
        words_ref = lines_ref_file[line_index_ref].split('\t')
        words_to_change_file = lines_to_change_file[line_index_change].split('\t')

        if(words_ref[0] == words_to_change_file[0]):
            final_ref.append(lines_ref_file[line_index_ref])
            final_to_change_file.append(lines_to_change_file[line_index_change])
            line_index_ref += 1 
            line_index_change += 1  
        else:
            
            for i in range(window):
                words_to_change_file_i = lines_to_change_file[line_index_change + i].split('\t')
                if(words_ref[0] == words_to_change_file_i[0]):
                    line_index_change += i
                    final_ref.append(lines_ref_file[line_index_ref])
                    final_to_change_file.append(lines_to_change_file[line_index_change])
                    window = 3
                    break
                elif(i == window - 1):
                    window += 1
#                    if(window == 6):
#                        print(words_ref[0])
#                        print(line_index_ref)
#                        print(line_index_change)
#                        for x in range(window):
#                            print(lines_to_change_file[line_index_change + x])
#                        print('\n')
#                        return
            line_index_ref += 1 
    return final_ref, final_to_change_file


def evaluate(reference_file, to_evaluate_file, nb_TP, nb_FN):
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
    ################################################## TODO ###################################################
    #
    #                               Calculer la precision de tout ca
    #
    ###########################################################################################################

    rappel = nb_TP / (nb_TP + nb_FN)

    return rappel


def writeLines(lines, file_out):
    file = open(file_out, 'w')
    file.writelines("%s\n" % l for l in lines)


if __name__ == '__main__':
    # sys.argv[1] : le fichier qui ressemble à la reference (en terme de nombre de mots) / La reference
    # sys.argv[2] : le fichier que l'on va transformer au fur et a mesure

    final_ref, final_to_change_file, nb_TP, nb_FN = harmonize_by_concatenation(sys.argv[1], sys.argv[2])

    # Pour evaluer
    evaluate(final_ref, final_to_change_file, nb_TP, nb_FN)

    #final_ref, final_to_change_file = harmonize_by_jump(sys.argv[1], sys.argv[2])



    # Cette partie ne sert a rien
    final_ref_name_file = sys.argv[1][:-5] + ".harmonised." + sys.argv[2][-4:] + sys.argv[1][-5:]
    final_to_change_file_name_file = sys.argv[2] + ".harmonised"

    #print(final_ref_name_file)
    #print(final_to_change_file_name_file)
    writeLines(final_ref, final_ref_name_file)
    writeLines(final_to_change_file, final_to_change_file_name_file)





