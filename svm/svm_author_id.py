#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

def SVMAccuracy (features_train, features_test, labels_train, labels_test):
	from sklearn import svm
	from sklearn.metrics import accuracy_score
	
	#clf = svm.SVC(kernel = "linear");
	clf = svm.SVC(C=10000, kernel = "rbf");
	
	#1% of the data is used for training
	#features_train = features_train[:len(features_train)/100]; 
	#labels_train = labels_train[:len(labels_train)/100]; 
	
	#Timing fit algorithm
	t0 = time();
	
	clf.fit(features_train, labels_train);
	
	print "Training Time: ", round(time() - t0, 3), "s";
	
	t0=time();
	
	pred = clf.predict(features_test);
	
	print "Prediction Time: ", round(time() - t0, 3), "s";
	
	print "Predicted in Chris (1) class: "
	print (pred == 1).sum()
	
	acc = accuracy_score(pred, labels_test);
	
	
	#Specific Data Points
	# answer10=pred[10];
	# print "Answer 10: " + str(answer10);
	
	# answer26=pred[26];
	# print "Answer 26: " + str(answer26);
	
	# answer50=pred[50];
	# print "Answer 50: " + str(answer50);
	# */
	
	return acc;

accuracy = SVMAccuracy(features_train, features_test, labels_train, labels_test);
print accuracy