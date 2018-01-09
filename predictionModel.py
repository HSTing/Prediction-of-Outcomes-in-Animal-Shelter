import csv
import os
import pydotplus
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


__author__ = 'Shih-Ting Huang', 'Wei-Yao Ku'

"""
CSCI-630: Final Project
Author: Shih-Ting Huang (sh3964), Wei-Yao Ku(wxk6489)

Build outcome prediction model of animal in shelter.
"""


def run_all(X_train, y_train, X_test, y_test):
    """
    Run the prediction model
    :param X_train: predictor of training data set
    :param y_train: target of training data set
    :param X_test: predictor of testing data set
    :param y_test: target of testing data set
    :return: running time list, accuracy list and model list
    """
    # Type of Classifiers
    Classifiers = [
        LogisticRegression(),
        DecisionTreeClassifier(criterion='entropy'),
        DecisionTreeClassifier(criterion='entropy', max_depth=5),
        RandomForestClassifier()]

    Accuracy = []
    Model = []
    Time = []
    # Run each classifier
    for classifier in Classifiers:
        start = time.time()
        fit = classifier.fit(X_train, y_train)
        end = time.time()
        pred = fit.predict(X_test)
        accuracy = accuracy_score(pred, y_test)
        Accuracy.append(accuracy)
        Model.append(classifier.__class__.__name__)
        Time.append(end-start)
    return Time, Accuracy, Model


def DTL(X_train, y_train):
    """
    Draw decision tree
    :param X_train: predictor of training data set
    :param y_train: target of training data set
    :return: None
    """
    clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=10)
    clf = clf.fit(X_train, y_train)
    with open(FILENAME + ".dot", 'w') as f:
        f = tree.export_graphviz(clf, out_file=f)
    os.unlink(FILENAME + '.dot')
    dot_data = tree.export_graphviz(clf, out_file=None, filled=True, rounded=True, special_characters=True)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf(FILENAME + "_tree.pdf")


def dummy(lst, lst_var):
    """
    Re-coding string variables into dummy variables
    :param lst: the data list
    :param lst_var: variable list
    :return: the data list with dummy variable coding
    """
    dummy_lst = []
    for i in range(len(lst)):
        example = lst[i]
        dummy_lst.append([])
        for j in range(len(lst_var)):
            idx = lst_var[j].index(example[j])
            for k in range(len(lst_var[j])):
                if k == idx:
                    dummy_lst[i].append(1)
                else:
                    dummy_lst[i].append(0)
    return dummy_lst


def main():
    """
    The main function.
    Run prediction mode & output the prediction result.
    :return: None
    """
    data = []
    data_var = []
    target = []

    # Read in csv file
    with open(FILENAME + '.csv', newline='') as f:
        title = f.readline().split(',')
        # extract variables types
        for _ in range(len(title)-1):
            data_var.append([])
        # extract the data
        line = f.readline().strip()
        while line != '':
            line = line.split(',')
            # extract all possible variables
            features = line[:len(line)-1]
            data.append(features)
            for i in range(len(features)):
                if features[i] not in data_var[i]:
                    data_var[i].append(features[i])
            outcome = line[len(line)-1]
            # extract the outcome(target)
            if outcome[0] is '0':
                outcome = 0
            else:
                outcome = 1
            target.append(outcome)
            line = f.readline()

    # output variable table
    with open(FILENAME + '_varTable.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        x_idx = 0
        for x in data_var:
            for y in x:
                writer.writerow(['x(' + str(x_idx) + ')', y])
                x_idx += 1
    # build dummy variables
    dum_data = dummy(data, data_var)

    # divide data into train & test set
    TRAIN_NUM = int(len(dum_data) * 0.7)
    TEST_NUM = int(len(dum_data) * 0.3)
    Time = []
    SetNum = []
    Acc = []
    '''
    # run with different data set number
    for factor in range(1, 21):
        train_num = int(TRAIN_NUM * 0.05 * factor)
        X_train = np.array(dum_data[:train_num])
        y_train = np.array(target[:train_num])
        X_test = np.array(dum_data[-TEST_NUM:])
        y_test = np.array(target[-TEST_NUM:])
        # run different method to build predict model
        this_time, acc, model = run_all(X_train, y_train, X_test, y_test)
        # store the result of prediction
        SetNum.append(train_num)
        Time.append(this_time)
        Acc.append(acc)

    # output the result
    with open(FILENAME +'_result_acc.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Data Size:'] + model)
        for i in range(len(SetNum)):
            writer.writerow([SetNum[i]] + Acc[i])

    with open(FILENAME + '_result_time.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Data Size:'] + model)
        for i in range(len(SetNum)):
            writer.writerow([SetNum[i]] + Time[i])
    '''
    # draw DTL
    DTL(np.array(dum_data[:TRAIN_NUM]), np.array(target[:TRAIN_NUM]))


if __name__ == '__main__':
    print("Please enter file name:")
    FILENAME = input()
    main()


