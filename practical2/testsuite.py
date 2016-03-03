import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import math
import tony_test

# Calculates the RMSE given a vector of predictions and a vector of observations
# pred and obs must be of same size
def calc_RMSE(pred, obs):
    assert (pred.shape[0] == obs.shape[0])
    return math.sqrt(sum((pred - obs) ** 2) / obs.shape[0])

# Perform cross validation with n blocks
def cross_validation(n):
    print "Starting"

    # Training data
    TRAIN_DIR = "train"
    # adjust this to change size
    X_train, Y_train, train_ids = tony_test.create_data_matrix(0, 100, TRAIN_DIR)

    # Determines size of blocks and indices to start
    dataSize = X_train.shape[0]
    blockSize = dataSize / n
    
    # RMSE values for each test
    RMSEs = []
    
    for i in xrange(n):
        print i
        # Determine start and end values for test data
        start = i * blockSize
        end = start + blockSize
        
        # Testing data
        X_test = X_train[start:end]
        Y_test = Y_train[start:end]

        # Training / testing values
        vals_train = X_train
        vals_test = X_test
        
        # Training: EDIT THIS FOR NEW MODELS
        LR = LinearRegression()
        LR.fit(vals_train, Y_train)
        
        # Predict based on test data
        LR_pred = LR.predict(vals_test)
        
        # Append RMSE
        RMSEs.append(calc_RMSE(LR_pred, Y_test))
        
#     print RMSEs
    print "Mean: " + str(np.mean(RMSEs))
    print "Variance: " + str(np.var(RMSEs))
    print "Std Dev: " + str(np.std(RMSEs))

print 'testsuite shiyay'
cross_validation(2)