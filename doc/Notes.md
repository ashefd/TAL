# Prise de notes

## Comment évaluer un POStagger ou un NE recognizer ?

TP : Le nombre de mot étiquetté correctement par les experts
FN : Le nombre de mot qui n'est étiquetté par aucune étiquette
FP : Le nombre de mot qui n'a pas été étiquetté correctement
TN : Les occurences ont été catégorisées comme des instances normales

Précision : Le ration entre les étiquettes correctement étiquettés et l'ensemble des mots étiquetés 
Précision = TP / (TP + FP)

Rappel: Le ratio entre tous les exemples (mots) correctement étiquettés avec tous les exemples (mots) étiquettés par les experts
Rappel = TP / (TP + FN)

## Exemple 1 : 
référence des experts   |   Prédication
            Phrase : I've a car
I   PRON                |   PRON
've VERB                |   VERB
a   DET                 |   DET
car NOUN                |   NOUN

TP = 4
FN = 0
FP = 0
Précision = 4 / (4+0) = 100%
Rappel = 100% aussi


## Exemple 2
référence des experts   |   Prédication
            Phrase : I've a car
I   PRON                |   *ADJ*
've VERB                |   VERB
a   DET                 |   DET
car NOUN                |   NOUN

TP = 4
FN = 0
FP = 1
Précision = 4 / (4+1) = 80%
Rappel = 100%


## Exemple 3
référence des experts   |   Prédication
            Phrase : I've a car
I   PRON                |   
've VERB                |   I've    VERB
a   DET                 |   a       DET
car NOUN                |   car     NOUN

TP = 4
FN = 2
FP = 0      // nb : on compare les étiquettes d'un même mot 
Précision = 4 / (4+0) = 100%
Rappel = 4 / (4+2) = 66%


## Exemple 4
référence des experts   |   Prédication
            Phrase : I've a car
I've   VERB             |   I   
                        |   've     VERB
a   DET                 |   a       DET
car NOUN                |   car     NOUN

TP = 3
FN = 1
FP = 0      // nb : on compare les étiquettes d'un même mot 
Précision = 3 / (3+0) = 100%
Rappel = 3 / (3+1) = 75%