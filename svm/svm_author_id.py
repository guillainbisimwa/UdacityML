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
from sklearn.svm import SVC
clf = SVC(C=1.0, kernel='rbf', gamma='auto')
t = time()

#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

clf.fit(features_train, labels_train)
print "Trainning time: ", round(time()-t,3), "s"
tt = time()
pred = clf.predict(features_test)
print "Predicting time: ", round(time()-tt,3), "s"
accuracy = clf.score(features_test, labels_test)
print accuracy
print "Predict the element [10]: ", pred[10]
print "Predict the element [25]: ", pred[26]
print "Predict the element [50]: ", pred[50]
#########################################################
print pred.size
chris = 0
for row in pred:
    if row == 0:
        chris += 1 
print chris

