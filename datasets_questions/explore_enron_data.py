#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "No. of Data Points: ", len(enron_data);

enron_features = sum(len(v) for v in enron_data.itervalues());

print "No. of Features ", enron_features;  

#Counting POIs
#POIs = sum(PPOI[poi] == "True" for PPOI in enron_data.itervalues());
POI_Count = 0;
for PPOI in enron_data.itervalues():
    if PPOI["poi"] is True:
        POI_Count += 1;
    
print "No. of POIs ", POI_Count;