#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:33:51 2019

@author: sizhenhan
"""
import numpy as np
from spelling_check import spell_check
from tqdm import tqdm
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.stem.lancaster import LancasterStemmer
lc = LancasterStemmer()
from nltk.stem import SnowballStemmer
sb = SnowballStemmer("english")

def load_pretrain(file,word_dict, lemma_dict,pre_type,check_dict):
    check = spell_check(check_dict)
    EMBEDDING_FILE = file
    embeddings_index = {}
    if pre_type == 'Glove':
        for i in open(EMBEDDING_FILE):
            tmp = i.split(" ")
            word, arr = tmp[0], np.asarray(tmp[1:], dtype='float32')
            embeddings_index[word] = arr
    elif pre_type == 'word2vec':
        for i in open(EMBEDDING_FILE):
            if len(i) > 100:
                tmp = i.split(" ")
                word, arr = tmp[0], np.asarray(tmp[1:], dtype='float32')
                embeddings_index[word] = arr
    else:
        for i in open(EMBEDDING_FILE, encoding="utf8", errors='ignore'):
            if len(i) > 100:
                tmp = i.split(" ")
                word, arr = tmp[0], np.asarray(tmp[1:], dtype='float32')
                embeddings_index[word] = arr
    embed_size = 300
    nb_words = len(word_dict)+1
    embedding_matrix = np.zeros((nb_words, embed_size), dtype=np.float32)
    unknown_vector = np.zeros((embed_size,), dtype=np.float32) - 1.
    for key in tqdm(word_dict):
        word = key
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = key.lower()
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = key.upper()
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = key.capitalize()
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = ps.stem(key)
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = lc.stem(key)
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = sb.stem(key)
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        word = lemma_dict[key]
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            embedding_matrix[word_dict[key]] = embedding_vector
            continue
        if len(key) > 1:
            word = check.correction(key)
            embedding_vector = embeddings_index.get(word)
            if embedding_vector is not None:
                embedding_matrix[word_dict[key]] = embedding_vector
                continue
        embedding_matrix[word_dict[key]] = unknown_vector                    
    return embedding_matrix
