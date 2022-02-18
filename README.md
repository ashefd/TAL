## Question 1 : récupérer le corpus original et la référence à partir d'un fichier annoté tout en enlevant les mots composés  
```
python getOriginalCorpus.py pos_reference.txt.lima out/pos_test.txt
```

## Question 2 : Convertir un fichier tagger LIMA en un fichier tagger universel
```
python from_LIMA_to_universal.py pos_reference.txt.lima POSTags_LIMA_PTB_Linux.txt POSTags_PTB_Universal_Linux.txt
```

## Question 3 : Créer les fichiers tagger en Stanford et en NLTK

### Stanford
Etapes :
1. Ouvrir un terminal et se positionner dans le dossier Projet
2. Copier le fichier out/pos_test.txt dans le dossier TP/TP2/stanford-postagger-2018-10-16
```
cd stanford-postagger-full-2018-10-16/
./../TP/TP2/stanford-postagger.sh models/english-left3words-distsim.tagger ../pos_text.txt > ../out/wsj_0010_sample.txt.pos.stanford
```




Tout refaire avec ce fichier la : out/pos_reference.txt.wc.lima

// python pos_test.txt.pos.stanford pos_test.txt.pos.nltk

```
python doPOStag.py out/pos_test.txt
```

### Faire en sorte que ce soit le bon format
