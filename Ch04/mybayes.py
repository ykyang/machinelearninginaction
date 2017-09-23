"""
Copied from bayes.py
"""


def load_data_set():
    """
    :return: list of list of words, 
    vector of class labels, 0 for not abusive, 1 for abusive
    """
    posting_list = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    
    class_vec = [0, 1, 0, 1, 0, 1]
        
    return posting_list, class_vec


def create_vocabulary_list(data_set):
    """
    Find unique words in the input data set

    :param data_set: list of list of words
    :return: list of unique words
    """
    vocab_set = set([])
    for document in data_set:
        vocab_set = vocab_set | set(document)

    return list(vocab_set)


def set_of_words_to_vec(vocab_list, word_list):
    """
    Find if words in the vocabulary list show up in a list
    of words

    :param vocab_list: list of unique words
    :param word_list: list of words
    :return: list of 0 and 1 in the same length as the vocab_list,
    0 indicates the word in the vocabulary is not in the word_list, 1 indicates
    the word in the vocabulary is in the word_list
    """
    return_vec = [0]*len(vocab_list)
    for word in word_list:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] = 1
        else:
            print('The word: %s is not in my Vocabulary!' % word)

    return return_vec

        
