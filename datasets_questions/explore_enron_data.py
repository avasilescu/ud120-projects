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

data_points = len(enron_data);

print "No. of Data Points: ", data_points;

enron_features = sum(len(v) for v in enron_data.itervalues());

print "No. of Features ", enron_features;  

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

salaried = 0;
known_email = 0;
total_paid = 0;

for person in enron_data.itervalues():
    if person["salary"] != "NaN":
        salaried += 1;
    if person["email_address"] != "NaN":
        known_email += 1;
    if person["total_payments"] != "NaN":
        total_paid += 1;

total_paid_NaN = data_points - total_paid;
percentage_total_paid_NaN = (total_paid_NaN/float(data_points))*100;

print "No. of Salaries:", salaried;
print "No. of Known Email Address:", known_email;
print "No. of Total Paid NaN:", total_paid_NaN;
print "Percentage of Total Paid NaN:", percentage_total_paid_NaN;