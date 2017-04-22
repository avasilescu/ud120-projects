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

    clean_percent = .1;
    print "Prediction Length: ", len(predictions);
    num_entries_to_remove = int((len(predictions) * clean_percent)); 


    for entry in range(len(predictions)):
        temp_ans = float(predictions[entry] - net_worths[entry]);
        resid_error.append(temp_ans);
    
    for i in range(num_entries_to_remove):
        max_val = max(resid_error);
        min_val = min(resid_error);
        max_idx = resid_error.index(max_val);
        min_idx = resid_error.index(min_val);
       
        if( max_val > abs(min_val)):
            resid_error.pop(max_idx);
            temp_predictions = np.delete(predictions, max_idx);
            temp_net_worths = np.delete(net_worths, max_idx);
            temp_ages = np.delete(ages, max_idx);

        else:
            resid_error.pop(min_idx);
            temp_predictions = np.delete(predictions, min_idx);
            temp_net_worths = np.delete(net_worths, min_idx);
            temp_ages = np.delete(ages, min_idx);
            
        predictions = temp_predictions;
        net_worths = temp_net_worths;
        ages = temp_ages;

    #cleaned_data = (ages, net_worths, resid_error);
    for i in range(len(ages)):
        cleaned_data.append((ages[i],net_worths[i],resid_error[i]));

    return cleaned_data;
    