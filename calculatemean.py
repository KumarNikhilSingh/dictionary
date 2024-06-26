def calculate_mean(my_dict):
    return sum(my_dict.values()) / len(my_dict)
my_dict = {'a': 10, 'b': 20, 'c': 30}
mean_value = calculate_mean(my_dict)
print(mean_value)