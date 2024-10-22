def set_operations(*sets):
    result = {}
    sets = list(sets)

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]

            union = a | b
            intersection = a & b
            difference_ab = a - b
            difference_ba = b - a

            result[f"{a} | {b}"] = union
            result[f"{a} & {b}"] = intersection
            result[f"{a} - {b}"] = difference_ab
            result[f"{b} - {a}"] = difference_ba

    return result

sets = {1, 2}, {2, 3}

result = set_operations(*sets)
for operation, outcome in result.items():
    print(f"{operation}: {outcome}")
