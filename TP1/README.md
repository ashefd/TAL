# Commandes pour le TP1

## Exercice 1 : Evaluation de l'analyse morpho-syntaxique de la plateforme NLTK

### Question 1 : Désambiguïser morpho syntaxiquement un text
```
python desambiguate.py wsj_0010_sample.txt out/wsj_0010_sample.txt.pos.nltk  
```
Avec  *wsj_0010_sample.txt*          : le fichier que l'on doit désambiguïser morpho syntaxiquement

Et    *wsj_0010_sample.txt.pos.nltk* : le fichier obtenu, enregistré dans le dossier "/out"

Résultat sauvegardé et disponible (sans exécution) sur : 
- 'results/EXO1_question_1_saving.txt'


### Question 2 : Evaluer à l'aide des étiquettes Penn TreeBank (PTB)
Avant d'évaluer le fichier *wsj_0010_sample.txt.pos.nltk*, il faut harmoniser ce fichier et sa référence.
```
 python harmonisation.py out/wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref  
```
Après exécutions, fichiers harmonisés enregistrés dans : 
- out/wsj_0010_sample.txt.pos.harm.nltk : fichier nltk harmonisé 
- out/wsj_0010_sample.pos.harm.ref  : fichier de référence harmonisé 

Résultats sauvegardés et disponibles sur : 
- 'output/EXO1_question_2_saving.txt' : fichier wsj_0010_sample.txt.pos.nltk harmonisé
- 'output/EXO1_question_2_saving_ref.txt' fichier wsj_0010_sample.pos.ref harmonisé


Par la suite, pour évaluer à l'aide des étiquettes Penn TreeBank, il faut entrer la commande :
```
python evaluate.py out/wsj_0010_sample.txt.pos.harm.nltk out/wsj_0010_sample.pos.harm.ref 
```

Résultats :
```
Word precision: 0.944954128440367
Word recall: 0.944954128440367
Tag precision: 0.944954128440367
Tag recall: 0.944954128440367
Word F-measure: 0.944954128440367
Tag F-measure: 0.944954128440367
```

Avec *wsj_0010_sample.txt.pos.harm.nltk* : le fichier à évaluer harmonisé

Et   *wsj_0010_sample.pos.harm.ref*      : le fichier de référence harmonisé


### Question 3 : Evaluser à l'aide des étiquettes universelles

#### A. Remplacement des étiquettes Penn TreeBank par des étiquettes universelles

On remplace dans la référence et dans le fichier à évaluer les étiquettes Penn TreeBank par des étiquettes universelles
```
python universal.py out/wsj_0010_sample.txt.pos.harm.nltk out/wsj_0010_sample.pos.harm.ref POSTags_PTB_Universal_Linux.txt 
```
Avec *wsj_0010_sample.txt.pos.harm.nltk*     : le fichier à évaluer

Et   *wsj_0010_sample.pos.harm.ref*          : le fichier de référence

Et   *POSTags_PTB_Universal_Linux.txt*  : le fichier "dictionnaire" qui contient la traduction des étiquettes Penn TreeBank par des étiquettes universelles

Après exécution, les fichiers en étiquette universelle seront enregistrés dans:

- *out/wsj_0010_sample.txt.pos.univ.nltk*

- *out/wsj_0010_sample.pos.txt.pos.univ.ref*

Output sauvegardé et disponible sur : 
- 'output/EXO1_question_3A_saving.txt' : fichier wsj_0010_sample.txt.pos.nltk avec etiquette universelle (wsj_0010_sample.txt.pos.univ.nltk)
- 'output/EXO1_question_3A_saving_ref.txt' fichier wsj_0010_sample.pos.ref avec etiquette universelle (wsj_0010_sample.pos.txt.pos.univ.ref))

#### B. Evaluer le texte à étiquette universelle

La commande est :
```
python evaluate.py out/wsj_0010_sample.txt.pos.univ.nltk out/wsj_0010_sample.pos.univ.ref   
```

Résultat :
```
Word precision: 0.963302752293578
Word recall: 0.963302752293578
Tag precision: 0.963302752293578
Tag recall: 0.963302752293578
Word F-measure: 0.963302752293578
Tag F-measure: 0.963302752293578
```

#### C. Conclusion
Utiliser les étiquettes universelles permettent d'avoir de meilleurs résultats : en effet, nous constatons une augmentation de la fiabilité de 2%.


## Exercice 2
Afin de pouvoir laisser a l'utilisateur le choix de trouver dans le texte, les structures qu'il souhaite, la commande est la suivante :  

```
python chunkParser.py wsj_0010_sample.txt structures_rules.txt Adjectif-Nom

```
- *wsj_0010_sample.txt* : le fichier que l'on veut chunker


- *structures_rules.txt* : le fichier qui contient les équivalences entre les structures syntaxiques et les expression régulières (regex) qui les modélise en python


- *Déterminant-Adjectif-Nom* : une string (insensible à la casse) qui indique la structure souhaitée. On peut indiquer les différentes structures qui suivent:
1. Adjectif-Nom 
2. Nom-Nom 
3. Adjectif-Nom-Nom 
4. Adjectif-Adjectif-Nom 

Après exécution, fichier de sortie sauvegardé dans :
out/wsj_0010_sample.txt.chk.nltk

Résultat sauvegardé et disponible sur : 
'output/EXO2_question_1_savings.txt'


## Exercice 3
### Question 1
Afin d'obtenir les entités nommées présentes dans le texte d'un fichier, on note la commande suivante :

```
 python use_ne_chunk.py wsj_0010_sample.txt out/wsj_0010_sample.txt.ne.nltk

```

Avec *wsj_0010_sample.txt*     : le fichier à évaluer

Et   *wsj_0010_sample.txt.ne.nltk*          : le fichier final qui contiendra un arbre syntaxique décrivant les entités nommées présentent dans le premier fichier

Après exécution, fichier de sortie sauvegardé dans :
out/wsj_0010_sample.txt.ne.nltk

Résultat sauvegardé et disponible sur : 
'output/EXO3_question_1_savings.txt'

### Question 2

```
python ne_standard_etiquettes.py out/wsj_0010_sample.txt.ne.nltk dict_ne_standard_etiquettes.txt out/wsj_0010_sample.txt.ne.univ.nltk
```

Avec   *wsj_0010_sample.txt.ne.nltk*          : le fichier à convertir 

Et *wsj_0010_sample.txt.ne.univ.nltk* : le fichier résultat contenant les entités nommées avec les étiquettes universelles (et sans les indicateurs)

Après exécution, fichier de sortie sauvegardé dans :
out/wsj_0010_sample.txt.ne.univ.nltk

Résultat sauvegardé et disponible sur : 
'output/EXO3_question_2_savings.txt'


### Question 3
Première commande : 
```
python use_ne_chunk.py formal-tst.NE.key.04oct95_sample.txt out/formal-tst.NE.key.04oct95_sample.txt.ne.nltk
```

Deuxième commande :

```
python ne_standard_etiquettes.py out/formal-tst.NE.key.04oct95_sample.txt.ne.nltk dict_ne_standard_etiquettes.txt out/formal-tst.NE.key.04oct95_sample.txt.ne.univ.nltk
```

