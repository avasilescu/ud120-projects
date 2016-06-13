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

print "Total Stock Value for James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"];

print "Emails from Wesley Colwell to POIs:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"];

print "Value of stock options exercised by Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"];

skilling_total = enron_data["SKILLING JEFFREY K"]["total_payments"];
lay_total = enron_data["LAY KENNETH L"]["total_payments"];
fastow_total = enron_data["FASTOW ANDREW S"]["total_payments"];

print "Skilling Total:", skilling_total;
print "Lay Total:", lay_total;
print "Fastow Total:", fastow_total;
