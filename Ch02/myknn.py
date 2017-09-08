import numpy as np
import operator as op
import builtins

def create_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    #group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']

    return group, labels


def classify0(inx, dataset, labels, k):
    """
    Classifier

    :param inx: vector to compare to existing data set (1xN)
    :param dataset: MxN data set
    :param labels: data set label vector size M
    :param k: number of neighbors to use for comparison
    :return: the most popular class label
    """
    dataset_size = dataset.shape[0]
    diff_mat = np.tile(inx, (dataset_size, 1)) - dataset
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sorted_distance_indices = distances.argsort()
    class_count = {}
    for i in builtins.range(k):
        vote_i_label = labels[sorted_distance_indices[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label,0) + 1
    sorted_class_count = sorted(class_count.items(),
                                key=op.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]


def file2matrix(filename):
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}

    fr = open(filename)
    line_count = len(fr.readlines())

    return_matrix = np.zeros((line_count, 3))
    class_label_vector = []

    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        tokens = line.split('\t')
        return_matrix[index,:] = tokens[0:3]
        label = tokens[-1]
        if label.isdigit():
            class_label_vector.append(int(label))
        else:
            class_label_vector.append(love_dictionary.get(label))

        index += 1

    return return_matrix, class_label_vector


def auto_norm(dataset):
    '''

    :param dataset: MxN array
    :return:
    '''
    min_val = dataset.min(0)
    max_val = dataset.max(0)

    frange = max_val - min_val

    norm_dataset = np.zeros(np.shape(dataset))
    row_count = dataset.shape[0]
    norm_dataset = dataset - np.tile(min_val, (row_count, 1))
    norm_dataset = norm_dataset/np.tile(frange, (row_count, 1))

    return norm_dataset, frange, min_val


def dating_class_test():
    hold_out_ratio = 0.05
    dating_data_mat, dating_label = file2matrix('datingTestSet2.txt')
    norm_mat, fucking_range, min_val = auto_norm(dating_data_mat)
    row_count = norm_mat.shape[0]
    test_count = int(row_count * hold_out_ratio)
    error_count = 0.0

    # What the hell is wrong with Python
    # because I used a variable named "range" in __main__
    # now it overtakes the "range" builtin function
    for i in builtins.range(test_count):
        classifier_result = classify0(norm_mat[i,:],
                                      norm_mat[test_count:row_count,:],
                                      dating_label[test_count:row_count],
                                      3)
        print("The classifier came back with: %d, the real answer is: %d" % (classifier_result,
                                                                             dating_label[i]))
        if classifier_result != dating_label[i]:
            error_count += 1

    print("The total error rate is: %f" % (error_count/float(test_count)))
    print("Error count: %d" % (error_count))


def classify_person():
    result_list = ['not at all', 'in small doses', 'in large doses']
    percent_time_video = float(input(
        'percentage of time spent playing video games? ')
    )
    frequent_miles = float(input(
        'frequent flier miles earned per year? '
    ))
    ice_cream = float(input(
        'liters of ice cream consumed per year? '
    ))

    dating_data_mat, dating_label = file2matrix('datingTestSet2.txt')
    norm_mat, range, min_val = auto_norm(dating_data_mat)
    input_array = np.array([frequent_miles, percent_time_video, ice_cream])

    classifier_result = classify0(
        (input_array - min_val)/range, norm_mat, dating_label, 3
    )

    print("You will probably like this person: %s"
          % (result_list[classifier_result - 1]))


def get_label(i):
    labels = ['Number of frequent flyer miles earned per year',
              'Percentage of time spent playing video games',
              'Liters of ice cream consumed per week']

    return labels[i]


import matplotlib.pyplot as plt


if __name__ == "__main__":
    inx = [0,0]
    group, labels = create_dataset()
    val = classify0(inx, group, labels, 3)
    print(val)

    dating_data_matrix, dating_label = file2matrix('datingTestSet.txt')
    # print(dating_data_matrix)
    # print(dating_label)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.scatter(dating_data_matrix[:,1], dating_data_matrix[:,2])
    ax.scatter(dating_data_matrix[:,1], dating_data_matrix[:,0],
               15.0*np.array(dating_label), 15.0*np.array(dating_label))

    plt.xlabel(get_label(1))
    plt.ylabel(get_label(0))

    # plt.show()

    #print(range(10))

    # norm_mat, range, min_val = auto_norm(dating_data_matrix)
    # print(norm_mat)
    # print(norm_mat.shape)
    # print(min_val)

    #dating_class_test()

    classify_person()
