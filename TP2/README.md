# TP2

## Téléchargement de stanford-postagger-2018-10-16.zip
Disponible sur : https://nlp.stanford.edu/software/tagger.shtml


## Partie 2 : Evaluation
### Question a
```
cd stanford-postagger-full-2018-10-16/
./stanford-postagger.sh models/english-left3words-distsim.tagger ../wsj_0010_sample.txt > ../wsj_0010_sample.txt.pos.stanford
```

### Question b
```
python from_ref_to_stanford_pos_tagger.py wsj_0010_sample.pos.ref wsj_0010_sample.pos.stanford.ref
```
### Question c
```
python evaluate.py wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref
```

Résultats obtenus : 

```
Word precision: 0.9636363636363636
Word recall: 0.9464285714285714
Tag precision: 0.9454545454545454
Tag recall: 0.9285714285714286
Word F-measure: 0.9549549549549549
Tag F-measure: 0.9369369369369368
```

### Question d
```
python from_PTB_to_universal.py wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref POSTags_PTB_Universal.txt wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.txt.pos.univ.ref. wsj_0010_sample.pos.ref
```
