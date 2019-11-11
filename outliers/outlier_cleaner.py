#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    ### your code goes here
    i = 0
    for net_worth in net_worths:
        error = abs(net_worth - predictions[i])
        
        list_inner = [ages[i], net_worth, error]
        if error <50 :
            cleaned_data.append(list_inner)
        i += 1
        print error
        print ""
        print ""
        
    
    return cleaned_data

