import mytrees as my

# driver for Listing 3.1
data, labels = my.create_data_set()
print(data)

entropy = my.cal_shannon_entropy(data)
print('entropy = %.17g' % entropy)

# driver for Listing 3.2
data, labels = my.create_data_set()
d = my.split_data_set(data, 0, 1)
print(d)
d = my.split_data_set(data, 0, 0)
print(d)

# driver for Listing 3.3
data, labels = my.create_data_set()
feature = my.choose_best_feature_to_split(data)
print('best feature to split: %d' % feature)

# driver for Listing 3.4
data, labels = my.create_data_set()
my_tree = my.create_tree(data, labels)
print(my_tree)