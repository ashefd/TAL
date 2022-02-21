## Question 1 : récupérer le corpus original et la référence à partir d'un fichier annoté tout en enlevant les mots composés  
```
python getOriginalCorpus.py ../data/pos_reference.txt.lima out/pos_test.txt
```

Trois fichiers de sortie : 

- Le corpus original : sauvegardé dans out/pos_test.txt
- Le coprus sans les mots composés: sauvegardé dans out/pos_test.wc.txt
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
cd stanford-postagger-full-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../src/out/pos_test.wc.txt > ../data/pos_test.txt.pos.stanford
```

Résultat du fichier taggé par stanford disponible dans :

 - data/pos_test.txt.pos.stanford : fichier taggé au format stanford 

3. Lancer la commande suivante :
```
python post_processing_stanford.py ../data/pos_test.txt.pos.stanford
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
Le fichier evaluate permet l'harmonisation ainsi que l'évaluation des fichiers de Stanford et NLTK

### Stanford
```
python evaluate.py out/reference.txt.wc.univ.lima out/pos_test.txt.pos.stanford.univ
```

### NLTK
```
python evaluate.py out/reference.txt.wc.univ.lima out/pos_test.txt.pos.nltk.univ
```
Il faut aussi rendre lima universel pour pouvoir evaluer 

Attention : cette commande a été modifié pour ce qui a été écrit dans la question 5
python harmonisation.py out/pos_reference.txt.wc.lima out/pos_test.txt.pos.nltk

python harmonisation.py out/pos_reference.txt.wc.lima out/pos_test.txt.pos.stanford

