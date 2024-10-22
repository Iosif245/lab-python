def sort_by_third_char(data):
    return sorted(data, key=lambda x: x[1][2])

tuples_list = [('abc', 'bcd'), ('abc', 'zza')]
result = sort_by_third_char(tuples_list)
print(result)
