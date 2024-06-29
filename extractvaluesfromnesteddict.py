nested_list = [
    {"a": 1, "b": {"c": 2, "d": 3}},
    {"d": 4, "e": {"f": 5, "g": 6}},
    {"g": 7, "h": {"i": 8, "j": 9}},
]
def extract_values(key, nested_list):
    result = []
    def extract_values_helper(nested_list):
        for item in nested_list:
            if key in item:
                result.append(item[key])
            for k, v in item.items():
                if isinstance(v, dict):
                    extract_values_helper([v])
    extract_values_helper(nested_list)
    return result
print(extract_values("a", nested_list))