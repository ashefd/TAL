## Question 1 : récupérer le corpus original et la référence à partir d'un fichier annoté tout en enlevant les mots composés  
```
python getOriginalCorpus.py ../data/pos_reference.txt.lima out/pos_test.txt
```

Trois fichiers de sortie : 

- Le corpus original : sauvegardé dans out/pos_test.txt
- Le corpus sans les mots composés: sauvegardé dans out/pos_test.wc.txt
- La référence lima sans les mots composés: sauvegardée dans  out/pos_reference.txt.wc.lima


## Question 2 : Convertir un fichier tagger LIMA en un fichier tagger universel
```
python from_LIMA_to_universal.py ../data/pos_reference.txt.lima ../data/POSTags_LIMA_PTB_Linux.txt ../data/POSTags_PTB_Universal_Linux.txt
```

Résultat stocké dans :
- out/pos_reference.txt.univ.lima 

Conversion du fichier lima sans les mots composés :

```
python from_LIMA_to_universal.py  out/pos_reference.txt.wc.lima ../data/POSTags_LIMA_PTB_Linux.txt ../data/POSTags_PTB_Universal_Linux.txt
```


Résultat stocké dans :
- out/reference.txt.wc.univ.lima

## Question 3 : Créer les fichiers tagger en Stanford et en NLTK

### Stanford
Etapes :
1. Ouvrir un terminal
2. Se placer dans le dossier stanford-postagger-full-2018-10-16 et lancer stanford-postagger.sh
```
cd ../stanford-postagger-full-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../src/out/pos_test.wc.txt > ../data/pos_test.txt.pos.stanford
cd ../src
```

Résultat du fichier taggé par stanford disponible dans :

 - data/pos_test.txt.pos.stanford : fichier taggé au format stanford 

3. Lancer la commande suivante :
```
python post_processing_stanford.py ../data/pos_test.txt.pos.stanford pos_tag
```

Résultat du fichier stanford au format modifié : 

 - out/pos_test.txt.pos.stanford 

### NLTK

```
python doPOStag.py out/pos_test.wc.txt
```

Résultat du fichier taggé par nltk disponible dans :

 - out/pos_test.txt.pos.nltk : fichier taggé au format nltk

## Question 4 : Traduire les tag PTB en tag universel
### Stanford
```
python universal.py out/pos_test.txt.pos.stanford ../data/POSTags_PTB_Universal_Linux.txt
```
Résultat sauvegardé et disponible sur :

- out/pos_test.txt.pos.stanford.univ

### NLTK
```
python universal.py out/pos_test.txt.pos.nltk ../data/POSTags_PTB_Universal_Linux.txt
```
Résultat sauvegardé et disponible sur :

- out/pos_test.txt.pos.nltk.univ

## Question 5

Analyse faite dans le Rapport : Partie "Evaluation de lanalyse morpho-syntaxique (POStagging)
" et Partie "Analyse de chaque Plateforme"


### Stanford
```
python evaluate.py out/reference.txt.wc.univ.lima out/pos_test.txt.pos.stanford.univ
```
Résultats obtenus : 

Word precision: 0.979500052295785
Word recall: 0.987660831048302
Tag precision: 0.9545957918050941
Tag recall: 0.9854500103928497
Word F-measure: 0.9835635141521819
Tag F-measure: 0.9697775504985937

### NLTK
```
python evaluate.py out/reference.txt.wc.univ.lima out/pos_test.txt.pos.nltk.univ
```

Word precision: 1.0
Word recall: 1.0
Tag precision: 0.9364013430772269
Tag recall: 1.0
Word F-measure: 1.0
Tag F-measure: 0.967156262749898


# Partie 2
## Question 1
```
python getOriginalCorpus.py ../data/ne_reference.txt.conll out/ne_test.txt
```

Résultat sauvegardé et disponible sur :

- out/ne_test.txt


## Question 2
Execution des NE recognizers et conversion des fichiers de sortie au bon format :

### Stanford
```
cd ../stanford-ner-2018-10-16
java -mx600m -cp stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier classifiers/english.all.3class.distsim.crf.ser.gz -textFile ../src/out/ne_test.txt > ../src/out/ne_test.txt.ne.stanfordbf
cd ../src
python post_processing_stanford.py out/ne_test.txt.ne.stanfordbf slash
```

Résultat sauvegardé et disponible sur :

- out/ne_test.txt.ne.stanford

### NLTK

```
python use_ne_chunk.py out/ne_test.txt out/ne_test.txt.ne.nltk
```
Résultat sauvegardé et disponible sur :

- out/ne_test.txt.ne.nltk

## Question 3

Conversion des fichiers en étiquettes coNLL-2003 : 

### Stanford

```
python post_processing_stanford.py out/ne_test.txt.ne.stanford ne
python convertToCoNLL.py out/ne_test.txt.ne.stanfordc ../data/dict_ne_standard_etiquettes.txt
```

Résultat sauvegardé dans :
- out/ne_test.txt.ne.stanfordc.conll


### NLTK

```
python convertToCoNLL.py out/ne_test.txt.ne.nltk ../data/dict_ne_standard_etiquettes.txt
```

Résultat sauvegardé dans : 
- out/ne_test.txt.ne.nltk.conll


## Question 4

### Stanford

```
python evaluate.py out/ne_test.txt.ne.stanfordc.conll ../data/ne_reference.txt.conll 
```
Résultats obtenus :
Word precision: 0.8314756597122988
Word recall: 0.8661307928947107
Tag precision: 0.9277296998711103
Tag recall: 0.8819359355855068
Word F-measure: 0.8484494993681345
Tag F-measure: 0.9042534099066762

### NLTK
```
python evaluate.py out/ne_test.txt.ne.nltk.conll ../data/ne_reference.txt.conll 
```
Résultats obtenus :
Word precision: 0.8114699437934648
Word recall: 0.8461309228171252
Tag precision: 0.9229006233956729
Tag recall: 0.8666494490358126
Word F-measure: 0.8284380470725541
Tag F-measure: 0.8938909607529747

#Question 5 

Analyse faite dans le Rapport : Partie "Evaluation de la reconnaissance dentités nommées (NE recognition)" et "Analyse de chaque Plateforme"
