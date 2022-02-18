## Question 1 : récupérer le corpus original et la référence à partir d'un fichier annoté tout en enlevant les mots composés  
```
python getOriginalCorpus.py ../data/pos_reference.txt.lima out/pos_test.txt
```

## Question 2 : Convertir un fichier tagger LIMA en un fichier tagger universel
```
python from_LIMA_to_universal.py ../data/pos_reference.txt.lima ../data/POSTags_LIMA_PTB_Linux.txt ../data/POSTags_PTB_Universal_Linux.txt
```

## Question 3 : Créer les fichiers tagger en Stanford et en NLTK

### Stanford
Etapes :
1. Ouvrir un terminal et se positionner dans le dossier Projet
2. Se placer dans le dossier TP/TP2/stanford-postagger-full-2018-10-16
```
cd stanford-postagger-full-2018-10-16/
./../TP/TP2/stanford-postagger.sh models/english-left3words-distsim.tagger ../pos_text.txt > ../out/wsj_0010_sample.txt.pos.stanford
```
3. Lancer la commande suivante :
```
python convert_format_stanford_two_columns.py ../data/pos_text.txt.pos.stanford
```

### NLTK

Tout refaire avec ce fichier la : out/pos_reference.txt.wc.lima

// python pos_test.txt.pos.stanford pos_test.txt.pos.nltk

```
python doPOStag.py out/pos_test.txt
```

### Faire en sorte que ce soit le bon format
