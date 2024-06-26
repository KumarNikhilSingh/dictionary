#Write a function to remove keys from a dictionary based on a list of words
def remove_keys_from_dict(my_dict):
    keys_to_remove = ['age', 'city']
    for key in keys_to_remove:
        if key in my_dict:
           removed_value = my_dict.pop(key)
my_dict = {'name':'Alice', 'age':25, 'city':'newyork', 'country':'usa'}
remove_keys_from_dict(my_dict)
print(my_dict)