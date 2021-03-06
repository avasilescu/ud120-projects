#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#Imports for Accuracy Score
import sys
from time import time
from sklearn.metrics import accuracy_score
import numpy

#Imports for KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier

#Imports for Adaboost
from sklearn.ensemble import AdaBoostClassifier

#Imports for Random Forest
from sklearn.ensemble import RandomForestClassifier

#Variable to switch between classifiers to run
#Options:
# "knn" = K Nearest Neighbors
# "ada" = Adaboost
# "rforest" = Random Forest
selectedClassifier = "knn";

#K Nearest Neighbors Classifier
def kNearestNeighbors(features_test, features_train,labels_test,labels_train):    
    print "Using K Nearest Neighbors"
    #Setup classifier
    clf = KNeighborsClassifier(algorithm='ball_tree',n_jobs=-1,weights='distance');
    
    #Timing fit algorithm
    t0 = time();
    
    #Fitting data
    clf = clf.fit(features_train,labels_train);
    
    print "Training Time: ", round(time() - t0, 3), "s";
    
    #Reset timer for prediction;
    t0 = time();
    
    #Predicting using test data
    nbrs_predict = clf.predict(features_test);
    
    print "Prediction Time: ", round(time() - t0, 3), "s";
    
    nbrs_acc = accuracy_score(nbrs_predict,labels_test);
    
    print "Accuracy: ", nbrs_acc;
    return clf;

def adaboost(features_test, features_train, labels_test, labels_train):
    print "Using Adaboost"
    #Setup Classifier
    clf = AdaBoostClassifier(n_estimators=100, learning_rate=.125)
    
    #Timing Fit Algorithm
    t0 = time();
    
    #Fitting data
    clf = clf.fit(features_train,labels_train);
    
    print "Training Time: ", round(time() - t0, 3), "s";
    
    #Reset timer for prediction
    t0=time();
    
    #Predicting using test data
    ada_predict = clf.predict(features_test);
    print "Prediction Time: ", round(time() - t0, 3), "s";
    
    ada_acc = accuracy_score(ada_predict,labels_test);
    
    print "Accuracy: ", ada_acc;
    return clf;

def rforest(features_test, features_train, labels_test, labels_train):
    print "Using Random Forest"
    #Setup Classifier
    clf = RandomForestClassifier(n_estimators=10,n_jobs=-1, min_samples_split=7);
    
    #Timing Fit Algorithm
    t0 = time();
    
    #Fitting data
    clf = clf.fit(features_train,labels_train);
    
    print "Training Time: ", round(time() - t0, 3), "s";
    
    #Reset timer for prediction
    t0=time();
    
    #Predicting using test data
    rforest_predict = clf.predict(features_test);
    print "Prediction Time: ", round(time() - t0, 3), "s";
    
    rforest_acc = accuracy_score(rforest_predict,labels_test);
    
    print "Accuracy: ", rforest_acc;
    return clf;

if selectedClassifier == "knn":
    clf = kNearestNeighbors(features_test, features_train, labels_test, labels_train);
if selectedClassifier == "ada":
    clf = adaboost(features_test, features_train, labels_test, labels_train);
if selectedClassifier == "rforest":
    clf = rforest(features_test, features_train, labels_test, labels_train);

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
