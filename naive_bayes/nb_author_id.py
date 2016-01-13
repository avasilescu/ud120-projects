#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
#########################################################

def NBAccuracy(features_train, labels_train, features_test, labels_test):
	#Import sklearn modules for GaussianNB
	from sklearn.naive_bayes import GaussianNB
	from sklearn.metrics import accuracy_score
	
	#Create classifer
	classifer = GaussianNB();
	
	#Timing fit algorithm
	t0 = time();
	
	#Fit classier on the training features
	classifer.fit(features_train, labels_train);
	
	print "Training Time: ", round(time() - t0, 3), "s";
	
	GaussianNB();
	
	#Timing prediction algorithm
	t0=time();
	
	#Use trained classifer to predict labels for test features
	pred = classifer.predict(features_test);
	
	print "Prediction Time: ", round(time() - t0, 3), "s";
	
	#Calculate accuracy from features_test with answer in labels_test
	
	accuracy = accuracy_score(pred, labels_test);
	
	return accuracy;

accuracy = NBAccuracy(features_train, labels_train, features_test, labels_test);
print accuracy;