def set_operations(a, b):

    set_a = set(a)
    set_b = set(b)

    intersect = list(set_a.intersection(set_b))
    union = list(set_a.union(set_b))
    diff_a_b = list(set_a.difference(set_b))
    diff_b_a = list(set_b.difference(set_a))

    return intersect, union, diff_a_b, diff_b_a

first_input = input("Enter the first list of numbers: ")
second_input = input("Enter the second list of numbers: ")

result = set_operations(first_input, second_input)
print("Intersection:", result[0])
print("Union:", result[1])
print("a - b:", result[2])
print("b - a:", result[3])
