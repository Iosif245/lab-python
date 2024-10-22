def count_unique_and_duplicates(lst):
    unique_elements = set(lst)
    total_elements = len(lst)
    unique_count = len(unique_elements)

    duplicate_count = total_elements - unique_count

    return unique_count, duplicate_count

my_list = [1, 2, 2, 3, 4, 4, 4, 5]
result = count_unique_and_duplicates(my_list)
print(result)
