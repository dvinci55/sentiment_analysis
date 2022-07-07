#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Written as part of https://www.scrapehero.com/how-to-scrape-amazon-product-reviews-using-python/		
from lxml import html  
import json
import requests
import csv
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import numpy as np # linear algebra
import pandas as pd
import pandas as pd
import csv
import itertools
import pandas as pd
import json,re
from dateutil import parser as dateparser
from time import sleep
import matplotlib as plt

def word_feats(words):

#	print(words)
    	return dict([(word, True) for word in words])
def word_feats1(words):

	#print(words)
    	return dict([(word, True) for word in words])


def ReadSenti():

				neutral_vocab = ['sound','worth','nice','good','like','love','LOVE IT','Best','Smart','Fantastic','Five stars','Excellent Phone','very good']
				neutral_vocab1 = ['bad','CUT','did','not','battery sucks','heating','Pathetic','One star']
	 
				positive_features = [(word_feats1(pos), 'pos') for pos in neutral_vocab]
				negative_features = [(word_feats1(neg), 'neg') for neg in neutral_vocab1]
				#neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

				train_set = negative_features + positive_features 
				#print(train_set)
				classifier = NaiveBayesClassifier.train(train_set) 
				#print(classifier)
				# Predict
				neg = 0
				pos = 0

				with open('output.txt', 'r') as my_file:
				    text = my_file.read()
				#print(text)
				
				
			    	for line in open('output.txt'):
    					for word in line.splitlines():
 					    #print(word)
				
					    classResult = classifier.classify( word_feats(word))
					    #print(word+","+classResult)
					    if classResult == 'neg':
						negtv=word
						with open('neg.txt', 'a') as my_file:
	    						my_file.write(negtv+ '\n')
						neg = neg + 1
					    if classResult == 'pos':
						postv=word
						with open('pos.txt', 'a') as my_file:
	    						my_file.write(postv+ '\n')
						pos = pos + 1
			
				poss= (float(pos)/len(text))
				negg= (float(neg)/len(text))
				n1=str(float(pos)/len(text))
				n2=str(float(neg)/len(text))
				cnt=n1+","+n2

				print('Positive: ' + str(float(pos)/len(text)))

				print('Negative: ' + str(float(neg)/len(text)))
				with open('count.txt', 'w') as my_filee:
	    				my_filee.write(cnt)
			
				

if __name__ == '__main__':
	ReadSenti()
