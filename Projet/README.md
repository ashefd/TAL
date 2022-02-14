## Question 1 : extraire 
```
python getOriginalCorpus.py pos_reference.txt.lima out/pos_test.txt
```

## Question 2 : 
```
python from_LIMA_to_universal.py pos_reference.txt.lima POSTags_LIMA_PTB_Linux.txt POSTags_PTB_Universal_Linux.txt
```

## Question 3 : 
Tout refaire avec ce fichier la : out/pos_reference.txt.wc.lima

```
python pos_test.txt.pos.stanford pos_test.txt.pos.nltk
python doPOStag.py out/pos_test.txt
```
Pb : dans le fichier NLTK, tous les mots sont tagges. 
exemple : 
red car 
->
red / noun
car / noun
Donc : il faut supprimer tous les mots composés. Donc problème pour les comparer
doPOStag.py doit pouvoir supprimer les mots composés (harmonisation)



