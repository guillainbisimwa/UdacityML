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
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print len(enron_data)
print len(enron_data["DONAHUE JR JEFFREY M"])
# print "SKILLING JEFFREY K: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
# print "FASTOW ANDREW S: ", enron_data["FASTOW ANDREW S"]["total_payments"]
# print "LAY KENNETH L: ", enron_data["LAY KENNETH L"]["total_payments"]


#print enron_data["DONAHUE JR JEFFREY M"]["poi"]
poi_f = 0
with_mail = 0
with_salary = 0
total_payments = 0
total_pay_of_poi = 0
for features in enron_data.values():
    if features["poi"] == True:
        poi_f += 1
    
    if features["email_address"] != "NaN":
        with_mail += 1
    
    if features["salary"] != "NaN":
        with_salary += 1

    if features["total_payments"] == "NaN":
        total_payments += 1

    if features["poi"] == True and features["total_payments"] == "NaN":
        total_pay_of_poi += 1
    # print features
    # print ""
    # print ""
    
print "Number of False POI: ", poi_f
print "isna mail: ", with_mail
print "isna salary: ", with_salary
print "isna total_payments: ", total_payments

t = 0
for names in enron_data.keys():
   #print names
   t += 1
print "Total persons in the dataset: ", t
print "Total POIs of NaN pay in the dataset: ", total_pay_of_poi