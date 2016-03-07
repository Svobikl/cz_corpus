# cz_corpus

Prerequisites: 

- Python >2.7
- Gensim package for word2vec toolkit
- Numpy package

Clone repository and uncompress model: 

 - "git clone https://github.com/Svobikl/cz_corpus Evaluator"
 - Download model from following address: "https://github.com/Svobikl/cz_corpus/releases/tag/release1.0/vectors_cz_cbow_dim300uni400_w15n15_iter15.txt.tar.gz" and save it to
folder "models/no_phrase"
 - Alternatively you can download other models from "https://github.com/Svobikl/cz_corpus/releases/tag/release1.0" 
 - "tar -zxvf Evaluator/models/no_phrase/vectors_cz_cbow_dim300uni400_w15n15_iter15.tar.gz"

Running evaluator:

 - "cd Evaluator"
 - "python Evaluator.py -m ./models/no_phrase/vectors_cz_cbow_dim300uni400_w15n15_iter15.txt"


Settings: 
- "-m" : model path specification
- "-t" : top n similar words,  default is 1.
- "-c" : corpus path specification, default is "./corpus/czech_emb_corpus.txt",
- or you can use "help" command and see all possible argument settings.



