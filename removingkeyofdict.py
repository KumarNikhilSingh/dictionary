def remove_key(my_dict):
    removed_value = my_dict.pop("teacher")
    return removed_value
my_dict = {'student': 40, 'teacher': 10, 'table':10, 'chair':40}
removed_value = remove_key(my_dict)
print(removed_value)