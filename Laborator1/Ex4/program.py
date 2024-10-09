def convert_string_into_lowercase_with_underscores(string):
    new_string = ""
    for char in string:
        if char.isupper():
            if new_string != "":
                new_string += "_" + char.lower()
            else:
                new_string += char.lower()
        else:
            new_string += char
    return new_string

camel_case_string = input()

print(convert_string_into_lowercase_with_underscores(camel_case_string))
