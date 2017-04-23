#!/usr/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, datasets

train_data  = sys.argv[1]
train_label = sys.argv[2]
test_data   = sys.argv[3]
output_txt  = sys.argv[4]

X = np.loadtxt(train_data)
Y = np.loadtxt(train_label)


logreg = linear_model.LogisticRegression(C=1e5)
#logreg = linear_model.LogisticRegression(C=1e5)

logreg.fit(X, Y)

Y2 = logreg.predict(X)

num_errors = sum((Y - Y2) * (Y - Y2))
error = num_errors / Y.shape[0]

#print logreg.coef_
print "Error rate on train is", error

devX = np.loadtxt(test_data)
#devY = np.loadtxt(test_label)
Z = logreg.decision_function(devX)
np.savetxt(output_txt, Z, "%s")
