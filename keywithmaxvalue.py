def maximum_value(my_dict):
    key_with_max_value = max(my_dict, key=lambda k: my_dict[k])
    return key_with_max_value

my_dict = {'a': 10, 'b': 20, 'c': 30, 'c': 15} 
result = maximum_value(my_dict)   
print("key with maximum value:", result)
print("Maximum value:", my_dict[result])