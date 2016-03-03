import os
from collections import Counter
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import numpy as np
from scipy import sparse

import util

TRAIN_DIR = "train"

call_set = set([])

# CHANGE IF NEED DIFFERENT FEATURES
good_calls = ['dump_line', 'download_file', 'open_file', 'connect_socket', 'impersonate_user']

def add_to_set(tree):
    for el in tree.iter():
        call = el.tag
        call_set.add(call)

def create_data_matrix(start_index, end_index, direc="train"):
    X = None
    classes = []
    ids = [] 
    i = -1
    for datafile in os.listdir(direc):
        if datafile == '.DS_Store':
            continue

        i += 1
        if i < start_index:
            continue 
        if i >= end_index:
            break

        # extract id and true class (if available) from filename
        id_str, clazz = datafile.split('.')[:2]
        ids.append(id_str)
        # add target class if this is training data
        try:
            classes.append(util.malware_classes.index(clazz))

        except ValueError:
            # we should only fail to find the label in our list of malware classes
            # if this is test data, which always has an "X" label
            assert clazz == "X"
            classes.append(-1)

        # parse file as an xml document
        tree = ET.parse(os.path.join(direc,datafile))
        add_to_set(tree)
        this_row = call_feats(tree)
        if X is None:
            X = this_row 
        else:
            X = np.vstack((X, this_row))

    return X, np.array(classes), ids

def call_feats(tree):
    

    call_counter = {}
    for el in tree.iter():
        call = el.tag
        if call not in call_counter:
            call_counter[call] = 1
        else:
            call_counter[call] += 1

    call_feat_array = np.zeros(len(good_calls))
    for i in range(len(good_calls)):
        call = good_calls[i]
        call_feat_array[i] = 0
        if call in call_counter:
            call_feat_array[i] = call_counter[call]

    return call_feat_array

def write_feats_to_file(filename, ids, feat_counts, classes):
    with open(filename, "w") as f:
        csfeats = ",".join(good_calls)
        f.write("id," + csfeats + ",classnum\n")
        for i in range(len(ids)):
            csfeatcounts = ",".join(map(str, feat_counts[i]))
            f.write(str(ids[i]) + "," + str(csfeatcounts) + "," + str(classes[i]) + "\n")

## Feature extraction
def main():
    X_train, t_train, train_ids = create_data_matrix(0, 3086, TRAIN_DIR)

    print 'Data matrix (training set):'
    # print X_train
    print X_train.shape[0]
    print 'Classes (training set):'
    print t_train

    write_feats_to_file("data/features.csv", train_ids, X_train, t_train)

    # From here, you can train models (eg by importing sklearn and inputting X_train, t_train).

    # X = X_train
    # Y = t_train

    # nb1 = GaussianGenerativeModel(isSharedCovariance=False)
    # nb1.fit(X,Y)
    # nb1.visualize("generative_result_separate_covariances.png")

if __name__ == "__main__":
    main()
    