def create_tuples(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []
    for i in range(max_length):
        tuple_element = []
        for lst in lists:
            if i < len(lst):
                tuple_element.append(lst[i])
            else:
                tuple_element.append(None)
        result.append(tuple(tuple_element))
    return result

lists1 = [1, 2, 3]
lists2 = [5, 6, 7]
lists3 = ["a", "b", "c"]

data = create_tuples(lists1, lists2, lists3)
print(data)
