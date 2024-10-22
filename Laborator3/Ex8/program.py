def loop(mapping):
    data = []
    visited = set()
    current_key = 'start'

    while current_key not in visited:
        visited.add(current_key)
        current_value = mapping[current_key]
        data.append(current_value)
        current_key = current_value

    return data

input_mapping = {
    'start': 'a',
    'b': 'a',
    'a': '6',
    '6': 'z',
    'x': '2',
    'z': '2',
    '2': '2',
    'y': 'start'
}

result = loop(input_mapping)
print(result)