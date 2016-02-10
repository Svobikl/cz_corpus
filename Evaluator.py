# -*- coding: utf-8 -*-
__author__ = 'svobik'

from gensim.models.word2vec import Word2Vec
from gensim import corpora, models, similarities, matutils
import re
import os
import logging
import optparse
import numpy as np
import operator
import codecs
from fnmatch import fnmatch


word2vecmodel_EN= '/media/data/korpusy/Trained/EN-vectors-cbow.txt'
amazonWord2Vec = '/media/data/korpusy/Trained/Amazon-vectors-cbow.txt'
word2vecmodel_CZ = [
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim50cbow3vocab1m.txt',
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim100cbow3vocab1m.txt',
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim300cbow3vocab1m.txt',
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim500cbow3vocab1m.txt',
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim50skip3vocab1m.txt',
                    '/media/data/korpusy/Trained/CZvec/vectors_cz_dim100skip3vocab1m.txt'
                    ]


corpusPath_EN = '/home/svobik/Workspace/Python/Svobik_corpus/English(byMikolov)/questions-words.txt'
corpusPath_CZ = '/home/svobik/Workspace/Python/Svobik_corpus/Czech/czech_emb_corpus.txt'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def cosine_vector_similarity(vec_a, vec_b):

   sim = np.dot(vec_a, vec_b)/(np.linalg.norm(vec_a)* np.linalg.norm(vec_b))
   return sim

def result_vector(st1,st2,st3, model):
    vec1 = model.syn0norm[model.vocab[st1].index]
    vec2 = model.syn0norm[model.vocab[st2].index]
    vec3 = model.syn0norm[model.vocab[st3].index]

    sub_vec = map(operator.sub, vec2,vec1)
    result_vec = map(operator.add, sub_vec, vec3)

    return result_vec
def most_similar_to_vec(vector,model,topn, list_words):
    dists = np.dot(model.syn0norm, vector)

    best = matutils.argsort(dists, topn=topn + len(list_words), reverse=True)
    # ignore (don't return) words from the input
    result = [(model.index2word[sim], float(dists[sim])) for sim in best if model.index2word[sim] not in list_words]

    return result[:topn]
def evaluate_file(filePath, topN, outputFile):

    accuracy = 0.0
    accuracyCosMul = 0.0
    accuracyAll = 0.0
    accuracyAllCosMul = 0.0
    classItemsCount = 0
    notSeenCounter = 0
    questionsCount =0
    fw = codecs.open(outputFile[:-4]+".res.txt", 'w','utf-8' )
    prevCategory = "Antonyms-nouns"
    fwerr = open(outputFile[:-4]+"err.log", 'w')
    with codecs.open(filePath, 'r','utf-8') as f:
        for line in f:
            if (line.strip()[0]==':'):
                if classItemsCount!=0:
                    currAcc= (accuracy/classItemsCount)*100.0
                    currAccCosMul= (accuracyCosMul/classItemsCount)*100.0
                    print(prevCategory)
                    print "Accuracy TOP%d = %f (%d/%d)\n" % (topN,currAcc, accuracy,classItemsCount)
                    fw.write(prevCategory.encode('utf-8'))
                    fw.write("Accuracy TOP%d = %f (%d/%d)" % (topN,currAcc, accuracy,classItemsCount))
                    prevCategory = line
                print line
                accuracy = 0.0
                accuracyCosMul = 0.0
                classItemsCount = 0
            else:
                tokens = line.lower().strip().split(" ")
                questionsCount = questionsCount + 1
                #print tokens[0]
                classItemsCount = classItemsCount + 1
                try:

                    #list = model.most_similar(positive=[tokens[0], tokens[2]], negative=[tokens[1]], topn=topN)
                    list = most_similar_to_vec(result_vector(tokens[0], tokens[1], tokens[2], model),model,topN,tokens[:-1])
                    for item in list:
                        #print item[0]
                        #print "Pos=%s,Neg=%s,item found=%s", (tokens[0]+","+tokens[2], tokens[1], str(item[0]))
                        match = item[0]
                        #match = match.encode('utf-8')
                        if match == tokens[3]:
                            #print "Correct item=%s" % (item[0])
                            accuracy =accuracy + 1.0
                            accuracyAll =accuracyAll + 1.0
                    #list = model.most_similar_cosmul(positive=[tokens[0], tokens[2]], negative=[tokens[1]], topn=topN)
                    #for item in list:
                        #print item[0]
                        #print "Pos=%s,Neg=%s,item found=%s", (tokens[0]+","+tokens[2], tokens[1], str(item[0]))
                    #    match = item[0]
                    #    match = match.encode('utf-8')
                    #    if match in tokens[3]:
                    #        print "Correct cosmul item=%s" % (item[0])
                    #        accuracyCosMul =accuracyCosMul + 1.0
                    #        accuracyAllCosMul =accuracyAllCosMul + 1.0
                except KeyError,e:
                    logging.error(e)
                    notSeenCounter +=1
                    fwerr.write(str(e))

    print "Total accuracy TOP%d = %d" % (topN,(accuracyAll/questionsCount)*100.0)
    fw.write("Total accuracy TOP%d = %d" % (topN,(accuracyAll/questionsCount)*100.0))
    print "Total accuracy CosMul TOP%d = %d" % (topN,(accuracyAllCosMul/questionsCount)*100.0)
    #fw.write("Total accuracy CosMul TOP%d = %d", (topN,(accuracyAllCosMul/questionsCount)*100.0))
    print "Seen= %f" % ((questionsCount-notSeenCounter)/questionsCount * 100.0)
    fw.write("Seen= %f"% ((questionsCount-notSeenCounter)/questionsCount * 100.0))

    fw.close()
    fwerr.close()

    return 0


if __name__ == '__main__':

    parser = optparse.OptionParser(usage="%prog [OPTIONS]")
    parser.add_option('-m', '--model', default='vector.txt',
                      help='Give a path with the name of a model to load (default name= vector.txt)')
    parser.add_option('-c', '--corpus', default='cz_emb.txt',
                      help='Give a name of corpus to analyze  (default: cz_emb.txt)')
    options, args = parser.parse_args()

    for name in word2vecmodel_CZ:
        model = Word2Vec.load_word2vec_format(name,binary=False)
        evaluate_file(corpusPath_CZ,1, name)
    #readfile(corpusPath_CZ)



