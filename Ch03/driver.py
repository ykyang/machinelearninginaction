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
