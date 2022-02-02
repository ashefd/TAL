# Commandes pour le TP1

## Exercice 1 : Evaluation de l'analyse morpho-syntaxique de la plateforme NLTK

### Question 1 : Désambiguïser morpho syntaxiquement un text
```
python desambiguate.py wsj_0010_sample.txt wsj_0010_sample.txt.pos.nltk
```
Avec  *wsj_0010_sample.txt*          : le fichier que l'on doit désambiguïser morpho syntaxiquement

Et    *wsj_0010_sample.txt.pos.nltk* : le fichier obtenu

### Question 2 : Evaluer à l'aide des étiquettes Penn TreeBank (PTB)
Avant d'évaluer le fichier *wsj_0010_sample.txt.pos.nltk*, il faut harmoniser ce fichier et sa référence.
```
python harmonisation.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref
```

Par la suite, pour évaluer à l'aide des étiquettes Penn TreeBank, il faut entrer la commande :
```
python evaluate.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref 
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

Avec *wsj_0010_sample.txt.pos.nltk* : le fichier à évaluer

Et   *wsj_0010_sample.pos.ref*      : le fichier de référence


### Question 3 : Evaluser à l'aide des étiquettes universelles

#### A. Remplacement des étiquettes Penn TreeBank par des étiquettes universelles

On remplace dans la référence et dans le fichier à évaluer les étiquettes Penn TreeBank par des étiquettes universelles
```
python universal.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref POSTags_PTB_Universal_Linux.txt 
```
Avec *wsj_0010_sample.txt.pos.nltk*     : le fichier à évaluer

Et   *wsj_0010_sample.pos.ref*          : le fichier de référence

Et   *POSTags_PTB_Universal_Linux.txt*  : le fichier "dictionnaire" qui contient la traduction des étiquettes Penn TreeBank par des étiquettes universelles

A la fin, les fichiers en étiquette universelle seront :

*wsj_0010_sample.txt.pos.nltk* -> *wsj_0010_sample.txt.pos.univ.nltk*

*wsj_0010_sample.pos.ref* -> *wsj_0010_sample.pos.txt.pos.univ.ref*

#### B. Evaluer le texte à étiquette universelle

La commande est :
```
python evaluate.py wsj_0010_sample.txt.pos.univ.nltk wsj_0010_sample.pos.txt.pos.univ.ref 
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
python chunkParser.py .\wsj_0010_sample.txt .\structures_rules.txt Adjectif-Nom

```
- *wsj_0010_sample.txt* : le fichier que l'on veut chunker


- *structures_rules.txt* : le fichier qui contient les équivalences entre les structures syntaxiques et les expression régulières (regex) qui les modélise en python


- *Déterminant-Adjectif-Nom* : une string (insensible à la casse) qui indique la structure souhaitée. On peut indiquer les différentes structures qui suivent:
1. Adjectif-Nom 
2. Nom-Nom 
3. Adjectif-Nom-Nom 
4. Adjectif-Adjectif-Nom 

## Exercice 3
### Question 1
Afin d'obtenir les entités nommées présentes dans le texte d'un fichier, on note la commande suivante :

```
python use_ne_chunk.py wsj_0010_sample.txt wsj_0010_sample.txt.ne.nltk
```

Avec *wsj_0010_sample.txt*     : le fichier à évaluer

Et   *wsj_0010_sample.txt.ne.nltk*          : le fichier final qui contiendra un arbre syntaxique décrivant les entités nommées présentent dans le premier fichier


### Question 2

```
python from_nltk_to_standard.py wsj_0010_sample.txt.ne.nltk wsj_0010_sample.standard.txt.ne.nltk
```

Avec   *wsj_0010_sample.txt.ne.nltk*          : le fichier à convertir 

Et *res.txt* : le fichier résultat contenant un arbre syntaxique décrivant les entités nommées présentent dans le premier fichier mais avec uniquement les étiquettes nltk.


### Question 3
Première commande : 
```
python use_ne_chunk.py formal-tst.NE.key.04oct95_sample.txt formal-tst.NE.key.04oct95_sample.txt.ne.nltk
```

Deuxième commande :
```
python use_ne_chunk.py formal-tst.NE.key.04oct95_sample.txt.ne.nltk res.txt
```

