import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import math

# Import data and drop smiles column
data = pd.read_csv("train.csv")
data = data.drop(['smiles'], axis=1)

# Calculates the RMSE given a vector of predictions and a vector of observations
# pred and obs must be of same size
def calc_RMSE(pred, obs):
    assert (pred.shape[0] == obs.shape[0])
    return math.sqrt(sum((pred - obs) ** 2) / obs.shape[0])

# Perform cross validation with n blocks
def cross_validation(n):
    print "Starting"
    # Determines size of blocks and indices to start
    dataSize = data.shape[0]
    blockSize = dataSize / n
    
    # RMSE values for each test
    RMSEs = []
    
    for i in xrange(n):
        print i
        # Determine start and end values for test data
        start = i * blockSize
        end = start + blockSize
        
        # Training data
        X_train = pd.concat((data.iloc[0:start], data.iloc[end:dataSize]), axis=0)
        # Testing data
        X_test = data.iloc[start:end]
#         print X_train.shape[0], X_test.shape[0]
        
        # Store gap values
        Y_train = X_train.gap.values
        X_train = X_train.drop(['gap'], axis=1)
        Y_test = X_test.gap.values
        X_test = X_test.drop(['gap'], axis=1)

        # Training / testing values
        vals_train = X_train.values
        vals_test = X_test.values
        
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

cross_validation(2)