"""
Copied from the original Machine Learning in Action source code
and translated into Python 3

@author: Yi-Kun Yang
"""
from math import log
import operator

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
    """
    Extract rows that has 'value' at 'axis'

    :param data_set:
    :param axis:
    :param value:
    :return: rows from the original data set that has value at axis
    the column[axis] is removed
    """

    return_data_set = []
    for row in data_set:
        if row[axis] == value:
            # remove the axis used for splitting
            reduced_row = row[:axis]
            reduced_row.extend(row[axis+1:])
            return_data_set.append(reduced_row)

    return return_data_set


def choose_best_feature_to_split(data_set):
    """

    :param data_set:
    :return: index of the best feature to split
    """
    best_feature: int = -1
    best_info_gain: float = 0.0

    base_entropy = cal_shannon_entropy(data_set)

    # the last column is label not a feature
    feature_count = len(data_set[0]) - 1

    # data_set = [
    #     [1, 1, 'yes'],
    #     [1, 1, 'yes'],
    #     [1, 0, 'no'],
    #     [0, 1, 'no'],
    #     [0, 1, 'no']]

    # iterate over all features
    for i in range(feature_count):
        # put a column (a feature) into a list
        # such as [1, 1, 1, 0, 0]
        feature_list = [row[i] for row in data_set]
        unique_values = set(feature_list)
        new_entropy = 0.0
        for value in unique_values:
            sub_data_set = split_data_set(data_set, i, value)
            weight = len(sub_data_set)/float(len(data_set))
            new_entropy += weight * cal_shannon_entropy(sub_data_set)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i

    return best_feature


def majority_count(class_list):
    class_count = {}
    max_count_class = None

    # find the most popular clazz
    for clazz in class_list:
        # Add 1 to clazz
        if clazz not in class_count.keys():
            class_count[clazz] = 0
        class_count[clazz] += 1

        # initialize max count class
        if max_count_class is None:
            max_count_class = clazz

        # Update max_count_class
        if clazz != max_count_class:
            if class_count[clazz] > class_count[max_count_class]:
                max_count_class = clazz

    return max_count_class


def create_tree(data_set, labels):
    # the last column is the clazz
    class_list = [row[-1] for row in data_set]

    # check is class_list is homogeneous
    if len(class_list) == class_list.count(class_list[0]):
        # return the clazz
        return class_list[0]

    # stop when there no more features
    if len(data_set[0]) == 1:
        return majority_count(class_list)

    # so we need to split
    # find the best feature to split
    best_feature = choose_best_feature_to_split(data_set)
    best_feature_label = labels[best_feature]

    my_tree = {best_feature_label:{}}
    del(labels[best_feature])

    feature_values = [row[best_feature] for row in data_set]
    unique_values = set(feature_values)

    for value in unique_values:
        sub_labels = labels[:]
        my_tree[best_feature_label][value] = create_tree(
            split_data_set(data_set, best_feature, value),
            sub_labels
        )

    return my_tree

