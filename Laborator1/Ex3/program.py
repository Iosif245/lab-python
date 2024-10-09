first_string = input()
second_string = input()

def print_occurrences(string1, string2):
    occurrences = string2.count(string1)
    print(occurrences)

print_occurrences(first_string, second_string)