# TP2

## Téléchargement de stanford-postagger-2018-10-16.zip
Disponible sur : https://nlp.stanford.edu/software/tagger.shtml


## Partie 2 : Evaluation
### Question a
```
./stanford-postagger.sh models/english-left3words-distsim.tagger wsj_0010_sample.txt > wsj_0010_sample.txt.pos.stanford
```

### Question b
```
python from_ref_to_stanford_pos_tagger.py wsj_0010_sample.pos.ref wsj_0010_sample.pos.stanford.ref
```

### Question c
```
python
evaluate.py wsj_0010_sample.txt.pos.stanford
wsj_0010_sample.pos.stanford.ref
```

### Question d
```
python from_PTB_to_universal.py wsj_0010_sample.txt.pos.stanford wsj_0010_sample.pos.stanford.ref POSTags_PTB_Universal.txt wsj_0010_sample.txt.pos.univ.stanford wsj_0010_sample.txt.pos.univ.ref. wsj_0010_sample.pos.ref
```
