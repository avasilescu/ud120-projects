#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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


def DTAccuracy(features_train, features_test, labels_train, labels_test):
    
    #import sklearn modules for DecisionTree
    from sklearn import tree
    from sklearn.metrics import accuracy_score

    #Create classifier using min_sample_split of 40
    clf = tree.DecisionTreeClassifier(min_samples_split=40);
    
    #Fit classifier on the training data
    clf = clf.fit(features_train, labels_train);

    #Use classifier to predict labels for test features
    predication = clf.predict(features_test);
    
    #Calculate accuracy from test with labels_test
    accuracy = accuracy_score(predication, labels_test);

    return accuracy;

accuracy = DTAccuracy(features_train, features_test, labels_train, labels_test);
print accuracy;