def count_characters(string):
    char_count = {}

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

input_string = "Ana has apples."
result = count_characters(input_string)
print(result)
