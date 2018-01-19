# -*- coding: utf-8 -*-

import pytest
import numpy as np
from hypertools.tools import text2mat
from sklearn.decomposition import LatentDirichletAllocation

data = [['i like cats alot', 'cats r pretty cool', 'cats are better than dogs'],
        ['dogs rule the haus', 'dogs are my jam', 'dogs are a mans best friend']]

def test_transform_text():
    assert isinstance(text2mat(data)[0], np.ndarray)

def test_count_LDA():
    isinstance(text2mat(data, vectorizer='CountVectorizer',
                        text='LatentDirichletAllocation')[0], np.ndarray)

def test_tfidf_LDA():
    isinstance(text2mat(data, vectorizer='TfidfVectorizer',
                        text='LatentDirichletAllocation')[0], np.ndarray)

def test_count_NMF():
    isinstance(text2mat(data, vectorizer='CountVectorizer', text='NMF')[0], np.ndarray)

def test_tfidf_NMF():
    isinstance(text2mat(data, vectorizer='TfidfVectorizer', text='NMF')[0], np.ndarray)

def test_transform_ndims():
    assert text2mat(data, n_components=10)[0].shape[1]==10

def test_transform_no_text_model():
    assert isinstance(text2mat(data, text=None)[0], np.ndarray)

def test_text_model_params():
    assert isinstance(text2mat(data, text_params={'learning_method' : 'batch'})[0], np.ndarray)

def test_vectorizer_params():
    assert text2mat(data, vectorizer_params={'max_features' : 2}, text=None)[0].shape[1]==2

def test_LDA_class():
    assert text2mat(data, text=LatentDirichletAllocation)[0].shape[1]==20

def test_LDA_class_instance():
    user_model = LatentDirichletAllocation(n_components=10)
    assert text2mat(data, text=user_model)[0].shape[1]==10
