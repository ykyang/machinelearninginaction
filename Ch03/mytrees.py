"""
Copied from the original Machine Learning in Action source code
and translated into Python 3

@author: Yi-Kun Yang
"""
from math import log


def create_data_set():
    data_set = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']

    return data_set, labels


def cal_shannon_entropy(data_set):
    """

    :param data_set:
            [
            [1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]
    :return:
    """
    entry_count = len(data_set)
    label_count = {}

    # - Count the number of occurrence - #
    for row in data_set:
        label = row[-1]
        if label not in label_count.keys():
            label_count[label] = 0
        label_count[label] += 1

    entropy = 0.0
    for key in label_count:
        prob = float(label_count[key])/ entry_count
        entropy -= prob * log(prob, 2)

    return entropy


def split_data_set(data_set, axis, value):
    return_data_set = []
    for row in data_set:
        if row[axis] == value:
            # remove the axis used for splitting
            reduced_row = row[:axis]
            reduced_row.extend(row[axis+1:])
            return_data_set.append(reduced_row)

    return return_data_set


#def choose_best_feature
