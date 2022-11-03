def count_items(item_list):
    """Recursion function count items from list"""
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_items(item)
        else:
            count += 1
    return count


c = count_items([1, 2, 3, 4, [1, 3, 4], [7, 8, 9]])
print(c)
