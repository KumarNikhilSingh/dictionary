from collections import Counter
def can_form_or_not(source_string, target_string):
    source_string_counter = Counter(source_string)
    target_string_counter = Counter(target_string)

    for char, freq in target_string_counter.items():
        if source_string_counter[char] < freq:
            return False
    return True 
print(can_form_or_not("aabbcc", "abc"))
print(can_form_or_not("aabbcc", "abcd"))
