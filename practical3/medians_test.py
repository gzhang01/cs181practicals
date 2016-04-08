import numpy as np
import csv
import sklearn
import math

# Predict via the user-specific median.
# If the user has no data, use the global median.

# Load the training data.
train_file = 'data/traindf.csv'
test_file  = 'data/valdf.csv'
# soln_file  = 'data/median_test.csv'

# Load the training data.
train_data = {}
with open(train_file, 'r') as train_fh:
    train_csv = csv.reader(train_fh, delimiter=',', quotechar='"')
    next(train_csv, None)
    for row in train_csv:
        user   = row[0]
        artist = row[1]
        plays  = row[2]

        if not user in train_data:
            train_data[user] = {}

        train_data[user][artist] = int(plays)



# Calculates the RMSE given a vector of predictions and a vector of observations
# pred and obs must be of same size
def calc_RMSE(pred, obs):
    assert (pred.shape[0] == obs.shape[0])
    return math.sqrt(sum((pred - obs) ** 2) / obs.shape[0])

def get_medians():
    # Compute the global median and per-user median.
    plays_array  = []
    user_medians = {}
    for user, user_data in train_data.iteritems():
        user_plays = []
        for artist, plays in user_data.iteritems():
            plays_array.append(plays)
            user_plays.append(plays)

        median_plays = np.median(np.array(user_plays))
        cutoff = 10000
        if median_plays > cutoff:
            median_plays = cutoff
            # median_plays = median_plays * 0.9
        user_medians[user] = median_plays
    global_median = np.median(np.array(plays_array))

    # Write out test solutions.
    # with open(test_file, 'r') as test_fh:
    #     test_csv = csv.reader(test_fh, delimiter=',', quotechar='"')
    #     next(test_csv, None)

    #     with open(soln_file, 'w') as soln_fh:
    #         soln_csv = csv.writer(soln_fh,
    #                               delimiter=',',
    #                               quotechar='"',
    #                               quoting=csv.QUOTE_MINIMAL)
    #         soln_csv.writerow(['Id', 'plays'])

    return_predictions = []
    test_plays = []
    # Load the testing data
    test_data = {}
    with open(test_file, 'r') as test_fh:
        test_csv = csv.reader(test_fh, delimiter=',', quotechar='"')
        next(test_csv, None)
        for row in test_csv:
            user   = row[0]
            artist = row[1]
            plays  = row[2]

            if not user in test_data:
                test_data[user] = {}

            test_data[user][artist] = int(plays)

    # for row in test_csv:
    #     user   = row[0]
    #     artist = row[1]

            if user in user_medians:
                return_predictions.append(user_medians[user])
            else:
                # print "User", id, "not in training data."
                return_predictions.append(global_median)

            test_plays.append(int(plays))

    print return_predictions[:5]
    print len(return_predictions)
    print test_plays[:5]
    print len(test_plays)

    RMSEs = []
    # Append RMSE
    RMSEs.append(calc_RMSE(np.array(return_predictions), np.array(test_plays)))

    # print RMSEs
    print "Mean: " + str(np.mean(RMSEs))
    # print "Variance: " + str(np.var(RMSEs))
    # print "Std Dev: " + str(np.std(RMSEs))


    return return_predictions



# Perform cross validation with n blocks
# def cross_validation(n):
#     print "Starting"
#     # Determines size of blocks and indices to start
#     dataSize = train_data.shape[0]
#     blockSize = dataSize / n

#     # RMSE values for each test
#     RMSEs = []

#     for i in xrange(n):
#         print i
#         # Determine start and end values for test data
#         start = i * blockSize
#         end = start + blockSize

#         # Training data
#         X_train = pd.concat((data.iloc[0:start], data.iloc[end:dataSize]), axis=0)
#         # Testing data
#         X_test = data.iloc[start:end]
#         print X_train.shape[0], X_test.shape[0]

#         # Store plays values
#         Y_train = X_train.plays.values
#         X_train = X_train.drop(['plays'], axis=1)
#         Y_test = X_test.plays.values
#         X_test = X_test.drop(['plays'], axis=1)

#         # Training / testing values
#         vals_train = X_train.values
#         vals_test = X_test.values

#         print vals_train

#         # Training: EDIT THIS FOR NEW MODELS
#         # LR = LinearRegression()
#         # LR.fit(vals_train, Y_train)

#         # # Predict based on test data
#         predictions = get_medians(vals_test, vals_test)

#         # Append RMSE
#         RMSEs.append(calc_RMSE(predictions, Y_test))

# #     print RMSEs
#     print "Mean: " + str(np.mean(RMSEs))
#     print "Variance: " + str(np.var(RMSEs))
#     print "Std Dev: " + str(np.std(RMSEs))

# cross_validation(2)

predictions = get_medians()
