from collections import Counter

def find_items_with_exact_count(number, *lists_to_search):
    all_items = [item for sublist in lists_to_search for item in sublist]
    item_count = Counter(all_items)
    return [item for item, count in item_count.items() if count == number]

lists = [[1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]]
x = 2
result = find_items_with_exact_count(x, *lists)
print(result)
