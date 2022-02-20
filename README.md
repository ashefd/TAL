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
1. Ouvrir un terminal
2. Se placer dans le dossier stanford-postagger-full-2018-10-16 et lancer stanford-postagger.sh
```
cd stanford-postagger-full-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../src/out/pos_test.wc.txt > ../data/pos_test.txt.pos.stanford
```
3. Lancer la commande suivante :
```
python post_processing_stanford.py ../data/pos_test.txt.pos.stanford
```

### NLTK

```
python doPOStag.py out/pos_test.wc.txt
```

## Question 4 : Traduire les tag PTB en tag universel
### Stanford


### NLTK


## Faire en sorte que ce soit le bon format
python harmonisation.py out/pos_reference.txt.wc.lima out/pos_test.txt.pos.nltk

python harmonisation.py out/pos_reference.txt.wc.lima out/pos_test.txt.pos.stanford

