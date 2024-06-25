items = ["apple", "apricot", "banana", "blackberry", "blueberry", "cherry", "cranberry"]
def group_items(items):
    result = {}
    for item in items:
        key = item[0]
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result
print(group_items(items))