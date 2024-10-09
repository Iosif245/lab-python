def extract_first_number(string):
    number = ''
    for char in string:
        if char.isdigit():
            number += char
        elif number:
            break
    return int(number) if number else None

input_string = input()

print(extract_first_number(input_string))
