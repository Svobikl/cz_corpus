# cz_corpus

Prerequisites: 

Python >2.7\\
Gensim package for word2vec toolkit\\
Numpy package\\

Running evaluator: 

git clone https://github.com/Svobikl/cz_corpus Evaluator
tar -zxvf Evaluator/models/no_phrase/vectors_cz_cbow_dim300uni400_w15n15_iter15.tar.gz

cd Evaluator
python Evaluator.py -m ./models/no_phrase/vectors_cz_cbow_dim300uni400_w15n15_iter15.txt


- or you can use help command and see how to specify your own model



