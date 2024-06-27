def mirror_char(input_string):
    mirror_dict = {}
    length = len(input_string)
    for i in range(length // 2):
        mirror_dict[input_string[i]] = input_string[length - i - 1]
        mirror_dict[input_string[length - i - 1]] = input_string[i]
    return mirror_dict
input_string = "abcefghi"
print(mirror_char(input_string))    