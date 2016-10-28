#!/usr/bin/python
import numpy as np; 

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = [];
    resid_error = [];

    temp_list = [predictions, net_worths, resid_error];

    clean_percent = .1;
    print "Prediction Length: ", len(predictions);
    num_entries_to_remove = int((len(predictions) * clean_percent)); 


    for entry in range(len(predictions)):
        #print "Entry: ", entry;
        #print "Prediction: ", predictions[entry], " Net Worth: " , net_worths[entry];
        temp_ans = predictions[entry] - net_worths[entry];
        resid_error.append(temp_ans);
        #print "Residue Error: " , resid_error[entry];
    
    

    return cleaned_data

