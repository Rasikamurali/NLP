import pandas as pd 
import numpy as np 
import random 
from collections import Counter
import regex as re
#using pre-existing python libraries 

# import required module
from sklearn.feature_extraction.text import TfidfVectorizer
# create object
tfidf = TfidfVectorizer()

# assign documents
d0 = 'Geeks for geeks'
d1 = 'Geeks'
d2 = 'r2j'
 
# # merge documents into a single corpus
# string = [d0, d1, d2]

# # get tf-df values
# result = tfidf.fit_transform(string)
# print(result)
# # get idf values
# # print('\nidf values:')
# for ele1, ele2 in zip(tfidf.get_feature_names_out(), tfidf.idf_):
# 	print(ele1, ':', ele2)



#coding tfidf from scratch 

#coding tf which is count of term in document/ number of words in document 

#First combine all documents to create corpus and check for unique words 
# merge documents into a single corpus
string = [d0, d1, d2]
print(string)
strings = d0 + " " + d1 + " " + d2
print(strings)
unique_words = (set(str.split(strings.lower())))
# strings = str(string)
# unique_words = set(str.split(strings.lower()))
# print(unique_words)


def tf(doc): 
	#needs to be revise. It needs to check for each unique word, the frequency in that document 
	print(doc)
	terms = doc.split()
	# words in doc 
	word_in_doc = len(terms)
	print(word_in_doc)
	freq = (Counter(terms))
	values = freq.values() 
	for value in values: 
		final_tf = print(value/word_in_doc)
	return final_tf

def idf(t): 
	#First get df, i.e how many times does this word show up across the documents 
	count = 0 
	N = 0 
	for doc in string: 
		N +=1 
		print(doc)
		if t in doc: 
			print("yes!")
			count += 1
	print(count, N)
	idf = np.log(N/count)
	print(idf)
	return idf
	# counter = 0 
	# print(t)
	# print(re.findall(t, strings.lower()))
	
    # #Get number of documents 
	# N= 3
	# idf = np.log(N/N(t))

	 
		

tf_d0 = tf(d0)
idf_t1 = idf("Geeks")
print(tf_d0 * idf_t1)