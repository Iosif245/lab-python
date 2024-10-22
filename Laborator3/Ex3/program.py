def compare_dicts(dict1, dict2):
    if type(dict1) is not type(dict2):
        return False

    if isinstance(dict1, dict):
        if dict1.keys() != dict2.keys():
            return False
        return all(compare_dicts(dict1[key], dict2[key]) for key in dict1)

    if isinstance(dict1, (list, set)):
        return sorted(dict1) == sorted(dict2)

    return dict1 == dict2

input_dict1 = {'a': 1, 'b': {'c': 2}}
input_dict2 = {'b': {'c': 2}, 'a': 1}
print(compare_dicts(input_dict1, input_dict2))

input_dict3 = {'a': 1, 'b': {'c': 3}}
print(compare_dicts(input_dict1, input_dict3))