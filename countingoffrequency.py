def count_frequency(my_list):
    dict = {}
    for element in my_list:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict    

my_list = [1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 1, 6, 6, 7, 8, 9, 9]
print(count_frequency(my_list))