import numpy as np
import operator as op

def create_dataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    #group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']

    return group, labels


'''

Input:      inx: vector to compare to existing dataset (1xN)
            dataSet: size m data set of known vectors (NxM)
            labels: data set labels (1xM vector)
            k: number of neighbors to use for comparison (should be an odd number)

Output:     the most popular class label

@author: pbharrin
'''
def classify0(inx, dataset, labels, k):
    dataset_size = dataset.shape[0]
    diff_mat = np.tile(inx, (dataset_size, 1)) - dataset
    sq_diff_mat = diff_mat**2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances**0.5
    sorted_distance_indices = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_distance_indices[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label,0) + 1
    sorted_class_count = sorted(class_count.items(),
                                key=op.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]

if __name__ == "__main__":
    inx = [0,0]
    group, labels = create_dataset()
    val = classify0(inx, group, labels, 3)
    print(val)

