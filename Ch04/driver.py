"""
Driver
"""
import mybayes as bayes

# load data
post_list, class_list = bayes.load_data_set()
my_vocab_list = bayes.create_vocabulary_list(post_list)
print(my_vocab_list)

x = bayes.set_of_words_to_vec(my_vocab_list, post_list[0])
print(x)
x = bayes.set_of_words_to_vec(my_vocab_list, post_list[3])
print(x)