"""
Copied from bayes.py
"""


def load_data_set():
    """
    :return: list of list of words, class vector
    """
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    
    class_vec = [0, 1, 0, 1, 0, 1]
        
    return posting_list, class_vec


def create_vocal_list(data_set):
    """

    :param data_set: list of list of words
    :return:
    """
    vocab_set = set([])
    for document in data_set:
        vocab_set = vocab_set | set(document)
        
    return list(vocab_set)


