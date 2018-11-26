# cz_corpus

The word embedding methods have been proven to be very
useful in many tasks of NLP (Natural Language Processing). Much has
been investigated about word embeddings of English words and phrases,
but only little attention has been dedicated to other languages.
Our goal in this paper is to explore the behavior of state-of-the-art
word embedding methods on Czech, the language that is characterized
by very rich morphology. We introduce new corpus for word analogy
task that inspects syntactic, morphosyntactic and semantic properties
of Czech words and phrases. We experiment with Word2Vec and GloVe
algorithms and discuss the results on this corpus. The corpus is available
for the research community.

### Note

Results in an article are lower due to the fact that we have used dataset trained with phrases and default W2V settings, that is not suited for less amount of data as the Czech Wikipedia has. Result was a dataset with lower single word performance, see our other publications that correct our results.

For testing the words analogies only, please use no_phrase dataset. 

### Cite
please cite this article: 
```
@inproceedings{svoboda:16,
author = {Svoboda, Lukáš and Brychcín, Tomáš},
year = {2016},
month = {04},
pages = {103–114},
booktitle = {Computational Linguistics and Intelligent Text Processing},
publisher={Springer},
doi= {10.1007/978-3-319-75477-2},
title = {New word analogy corpus for exploring embeddings of Czech words}
}
```


### Testing corpus with Python and Gensim

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



