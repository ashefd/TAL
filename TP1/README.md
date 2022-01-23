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
```

#### C. Conclusion
Utiliser les étiquettes universelles permettent d'avoir de meilleurs résultats.


## Exercice 2
```
python chunkParser.py wsj_0010_sample.txt wsj_0010_sample.txt.chk.nltk
```
Avec *wsj_0010_sample.txt* : le fichier que l'on veut chunker
Et *wsj_0010_sample.txt.chk.nltk* : le fichier résultat contenant les mots composés

